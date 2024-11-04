from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория", help_text="Введите категорию товара")
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Товар", help_text="Введите название товара")
    description = models.TextField(
        verbose_name="Описание товара", help_text="Введите описание товара", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="media/photo",
        blank=True,
        null=True,
        verbose_name="Изображение товара",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        related_name="products",
        blank=True,
        null=True,
    )
    price = models.FloatField(verbose_name="Цена товара", help_text="Введите цену товара")
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True, blank=True, null=True)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
