from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', help_text='Введите название', blank=True,
                            null=True)
    description = models.TextField(max_length=250, verbose_name='Описание', help_text='Введите описание', blank=True,
                                   null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', help_text='Введите название')
    description = models.TextField(max_length=250, verbose_name='Описание', help_text='Введите описание')
    image = models.ImageField(upload_to='media/photo', blank=True, null=True, verbose_name='Фото',
                              help_text='Загрузите фотографию')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='Категория',
                                 help_text='Введите категорию', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена за покупку', help_text='Введите цену', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', help_text='Введите дату создания', blank=True,
                                      auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
