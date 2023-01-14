
from django.contrib import admin
from django.urls import path
from webapp.views import ProductList, ProductDetail, ProductCreate, ProductDelete, ProductUpdate, ReviewCreate, \
    ReviewDeleteView, ReviewUpdateView
from django.views.generic import RedirectView

app_name = 'webapp'


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='webapp:index')),
    path('index/', ProductList.as_view(), name='index'),
    path('product/<int:pk>/view/', ProductDetail.as_view(), name='product_view'),
    path('product/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('product/add/', ProductCreate.as_view(), name='product_add'),
    path('product/<int:pk>/review/add/', ReviewCreate.as_view(), name='product_review_add'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete'),
    path('redirect_view/', RedirectView.as_view())
]
