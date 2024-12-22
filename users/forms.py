from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "phone_number", "avatar", "country", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите адрес электронной почты"}
        )
        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите номер телефона"}
        )
        self.fields["avatar"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Загрузите Ваш аватар"}
        )
        self.fields["country"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите Вашу страну проживания"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number
