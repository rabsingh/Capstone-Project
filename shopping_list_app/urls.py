from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_item, name='add_item'),
    path('', views.item_list, name='item_list'),
    path('register/', views.register, name='register'), 
]
