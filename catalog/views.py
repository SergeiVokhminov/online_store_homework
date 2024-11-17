from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/home.html", context)


def catalog(request):
    categories = Category.objects.all()
    context = {"category": categories}
    return render(request, "catalog/catalog.html", context)


def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_info.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(
            f"""</div> Добрый день, {name}! Ваш номер: {phone}<div>
                                <div> Ваше сообщение: {message} <div>
                                <div> Ваши данные были успешно отправлены!</div>"""
        )

    return render(request, "catalog/contacts.html")


def entrance(request):
    return render(request, "catalog/entrance.html")


def registration(request):
    return render(request, "catalog/registration.html")
