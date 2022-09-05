from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from common import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users', views.users),  
    path('signup', views.signup),  
    path('index', views.index),  # '/' 에 해당되는 path
    path('', views.index)  # '/' 에 해당되는 path
]

