from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView, View

from catalog.forms import ProductForm
from catalog.models import Category, Product
from catalog.services import get_products_list_by_category


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "catalog/product_list.html"

    def get_queryset(self, *args, **kwargs):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)
        return queryset


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
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
    template_name = "catalog/product_form.html"
    # fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog:product_list")

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        if request.user != product.owner:
            return HttpResponseForbidden("У вас нет прав для редактирования продукта.")

        # return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = 'catalog.delete_product'


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if not request.user.has_perm("can_unpublish_product"):
            return HttpResponseForbidden("У вас недостаточно прав для снятия товара с публикации!")

        product.is_published = False
        product.save()

        return redirect('catalog:product_list')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "catalog/category_list.html"
    # context_object_name = "category"


class ProductCategoryListView(ListView):
    model = Category
    template_name = "catalog/category_product.html"
    context_object_name = "category"

    def get_queryset(self, *args, **kwargs):
        queryset = get_products_list_by_category(self.kwargs.get('pk'))

        return queryset

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
