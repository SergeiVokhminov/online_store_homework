from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (HomeView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, ContactsView, CategoryListView, UnpublishProductView,
                           ProductCategoryListView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", (ProductDetailView.as_view()), name="product"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
    path("category_products/<int:pk>/", ProductCategoryListView.as_view(), name="category_products"),
    path("unpublish/<int:pk>/", UnpublishProductView.as_view(), name="unpublish_product"),
]
