from django.urls import path, re_path
from . import views

app_name = 'product'
urlpatterns = (
    path('', views.home, name='product'),
    path('product/<str:slug>/', views.home, name='category'),
    path('<str:slug>/', views.product_detail, name='product_detail'),
)
