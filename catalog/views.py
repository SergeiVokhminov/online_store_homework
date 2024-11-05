from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "catalog/home.html")


def catalog(request):
    return render(request, "catalog/catalog.html")


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
