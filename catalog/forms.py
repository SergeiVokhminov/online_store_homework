from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

forbidden_words = [
    "казино", "криптовалюта", "крипта", "биржа", "дешево", "дёшево", "бесплатно", "обман", "полиция", "радар"
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "owner")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', "placeholder": "Введите название товара"}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', "placeholder": "Введите описание товара"}
        )
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control', "placeholder": "Загрузите изображение товара"}
        )
        self.fields['category'].widget.attrs.update(
            {'class': 'form-control', "placeholder": "Выберите категорию товара"}
        )
        self.fields['price'].widget.attrs.update(
            {'class': 'form-control', "placeholder": "Введите цену товара"}
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name.lower() in forbidden_words:
            raise ValidationError("Название содержит запрещенное слово!")
        elif Product.objects.filter(title=name).exists():
            raise ValidationError("Товар с таким названием уже существует!")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError("Описание содержит запрещенное слово!")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной!")
        return price
