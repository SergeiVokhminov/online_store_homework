from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Category, Product


class HomeView(TemplateView):
    template_name = "catalog/home.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class CategoryListView(ListView):
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
