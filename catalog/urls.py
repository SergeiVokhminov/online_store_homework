from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog, contacts, entrance, home, product_info, registration, add_product

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("catalog/", catalog, name="catalog"),
    path("contacts/", contacts, name="contacts"),
    path("entrance/", entrance, name="entrance"),
    path("registration/", registration, name="registration"),
    path("product/<int:pk>/", product_info, name="product"),
    path("add_product", add_product, name="add_product")
]
