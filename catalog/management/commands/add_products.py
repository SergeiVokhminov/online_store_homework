from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Загружает данные в БД из fixture.json, предварительно очистив БД."

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("БД успешно заполнена данными из fixture"))
