# Generated by Django 5.1.2 on 2024-11-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_description_alter_product_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(
                blank=True, help_text="Введите описание категории", null=True, verbose_name="Описание категории"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, help_text="Введите описание товара", null=True, verbose_name="Описание товара"
            ),
        ),
    ]