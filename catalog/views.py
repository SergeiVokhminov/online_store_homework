from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView

# from catalog.forms import AddProductForm
from catalog.models import Category, Product

def home(request):
    return render(request, "catalog/home.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog: product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    success_url = reverse_lazy("catalog: product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog: product_list")


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

def entrance(request):
    return render(request, "catalog/entrance.html")

def registration(request):
    return render(request, "catalog/registration.html")
