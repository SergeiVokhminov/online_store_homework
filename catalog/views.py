from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView

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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


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
