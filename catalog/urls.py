from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (CategoryListView, ProductListView, ContactsView, ProductUpdateView, ProductDeleteView,
                           entrance, HomeView, ProductDetailView, registration, ProductCreateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("entrance/", entrance, name="entrance"),
    path("registration/", registration, name="registration")
]
