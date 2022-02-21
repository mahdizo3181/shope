from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.home, name='product'),
    path('product/<slug:slug>/', views.home, name='category_filter '),
    path('<slug:slug>/', views.product_detail, name='product_detail')
]
