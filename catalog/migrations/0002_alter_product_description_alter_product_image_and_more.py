# Generated by Django 5.1.2 on 2024-11-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(help_text="Введите описание товара", verbose_name="Описание товара"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите изображение товара",
                null=True,
                upload_to="media/photo",
                verbose_name="Изображение товара",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(help_text="Введите название товара", max_length=100, verbose_name="Товар"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.FloatField(help_text="Введите цену товара", verbose_name="Цена товара"),
        ),
    ]
