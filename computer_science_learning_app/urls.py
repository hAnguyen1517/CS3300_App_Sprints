"""
URL configuration for computer_science_learning_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import IndexView,UsersysListView,UsersysDetailView,UsersysCreateView,UsersysUpdateView,game_list,game_detail,game_create,game_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # users urls
    path('users/', UsersysListView.as_view(), name='usersys_list'),  # Map the URL to the UsersysListView
    path('users/<int:pk>/', UsersysDetailView.as_view(), name='usersys_detail'),  # Map the URL to the UsersysDetailView
    path('users/create/', UsersysCreateView.as_view(), name='usersys_create'),
    path('users/<int:pk>/edit/', UsersysUpdateView.as_view(), name='usersys_edit'),
    # games urls
    path('games/', game_list, name='game_list'),
    path('games/<int:pk>/', game_detail, name='game_detail'),
    path('games/create/', game_create, name='game_create'),
    path('games/<int:pk>/update/', game_update, name='game_update'),
    # learning resources urls    
    path('learning_resources/', views.learning_resource_list, name='learning_resource_list'),
    path('learning_resources/<int:pk>/', views.learning_resource_detail, name='learning_resource_detail'),
    path('learning_resources/create/', views.learning_resource_create, name='learning_resource_create'),
    path('learning_resources/<int:pk>/update/', views.learning_resource_update, name='learning_resource_update'),
    path('learning_resources/<int:pk>/delete/', views.learning_resource_delete, name='learning_resource_delete'),


]
