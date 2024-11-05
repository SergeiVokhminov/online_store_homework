# Generated by Django 5.1.2 on 2024-11-04 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(help_text="Введите категорию товара", max_length=100, verbose_name="Категория"),
                ),
                (
                    "description",
                    models.TextField(help_text="Введите описание категории", verbose_name="Описание категории"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название продукта/товара", max_length=100, verbose_name="Продукт/товар"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание продукта/товара", verbose_name="Описание продукта/товара"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение продукта/товара",
                        null=True,
                        upload_to="media/photo",
                        verbose_name="Изображение продукта/товара",
                    ),
                ),
                ("price", models.FloatField(help_text="Введите цену продукта", verbose_name="Цена продукта/товара")),
                ("created_at", models.DateField(auto_now_add=True, null=True, verbose_name="Дата создания")),
                ("updated_at", models.DateField(auto_now=True, null=True, verbose_name="Дата последнего изменения")),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name"],
            },
        ),
    ]
