from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from shopping_list_app import views as app_views

urlpatterns = [
    path('', app_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('shopping/', include('shopping_list_app.urls')),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),
    path('register/', app_views.register, name='register'),
]
