from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'catalog/home.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Добрый день, {name}! Ваши данные были успешно отправлены!")

    return render(request, "catalog/contacts.html")
