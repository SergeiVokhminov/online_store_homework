from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View

from catalog.forms import ProductForm
from catalog.models import Category, Product


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    # fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    permission_required = 'catalog.delete_product'


class UnpublishProductView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас недостаточно прав для снятия продукта с публикации")

        product.is_published = False
        product.save()

        return redirect('catalog:product', pk=product.id)


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "catalog/category_list.html"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"""</div> Добрый день, {name}! Ваш номер: {phone}<div>
                                <div> Ваше сообщение: {message} <div>
                                <div> Ваши данные были успешно отправлены!</div>"""
        )

class EntranceView(TemplateView):
    template_name = "catalog/entrance.html"


class RegistrationView(TemplateView):
    template_name = "catalog/registration.html"
