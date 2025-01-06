from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_item, name='add_item'),
    path('', views.item_list, name='item_list'),
    path('register/', views.register, name='register'), 
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update-status/<int:item_id>/', views.update_authorised_status, name='update_status'),
]
