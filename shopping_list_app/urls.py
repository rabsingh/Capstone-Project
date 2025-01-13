from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.item_list, name='item_list'),
    path('add/', views.add_item, name='add_item'),
    path('register/', views.register, name='register'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path(
        'update-status/<int:item_id>/',
        views.update_authorised_status,
        name='update_status'
    ),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
]
