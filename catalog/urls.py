from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, catalog, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("catalog/", catalog, name="catalog"),
    path("contacts/", contacts, name="contacts"),
]
