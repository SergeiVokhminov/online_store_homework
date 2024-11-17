from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import catalog, contacts, home, product_info, entrance, registration

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("catalog/", catalog, name="catalog"),
    path("contacts/", contacts, name="contacts"),
    path("entrance/", entrance, name="entrance"),
    path("registration/", registration, name="registration"),
    path("product/<int:pk>/", product_info, name="product")
]
