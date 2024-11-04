from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import catalog, contacts, home

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("catalog/", catalog, name="catalog"),
    path("contacts/", contacts, name="contacts"),
]
