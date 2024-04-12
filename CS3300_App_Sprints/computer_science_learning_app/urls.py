from django.contrib import admin
from django.urls import path,include
from .views import IndexView, UsersysListView, UsersysDetailView, UsersysCreateView, UsersysUpdateView, GameListView, GameDetailView, GameCreateView, GameUpdateView, LearningResourceListView, LearningResourceDetailView, LearningResourceCreateView, LearningResourceUpdateView, ProgressListView, ProgressDetailView, ProgressCreateView, ProgressUpdateView, PerformanceReportListView, PerformanceReportDetailView, PerformanceReportCreateView, PerformanceReportUpdateView, usersys_delete, game_delete, learning_resource_delete, progress_delete, performance_report_delete
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login_view, name='login'),
    path('accounts', include('django.contrib.auth.urls')),
    path('accounts/register', views.registerPage, name = 'register_page'),
    # path('accounts/login', views.loginPage, name = 'login_page'),

    # Users URLs
    path('users/', UsersysListView.as_view(), name='usersys_list'),
    path('users/<int:pk>/', UsersysDetailView.as_view(), name='usersys_detail'),
    path('users/create/', UsersysCreateView.as_view(), name='usersys_create'),
    path('users/<int:pk>/edit/', UsersysUpdateView.as_view(), name='usersys_edit'),
    path('users/delete/<int:pk>/', usersys_delete, name='usersys_delete'),
    
    # Games URLs
    path('games/', GameListView.as_view(), name='game_list'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('games/create/', GameCreateView.as_view(), name='game_create'),
    path('games/<int:pk>/update/', GameUpdateView.as_view(), name='game_update'),
    path('games/<int:pk>/delete/', game_delete, name='game_delete'),

    # Learning Resources URLs
    path('learning_resources/', LearningResourceListView.as_view(), name='learning_resource_list'),
    path('learning_resources/<int:pk>/', LearningResourceDetailView.as_view(), name='learning_resource_detail'),
    path('learning_resources/create/', LearningResourceCreateView.as_view(), name='learning_resource_create'),
    path('learning_resources/<int:pk>/update/', LearningResourceUpdateView.as_view(), name='learning_resource_update'),
    path('learning_resources/<int:pk>/delete/', learning_resource_delete, name='learning_resource_delete'),

    # Progress URLs
    path('progress/', ProgressListView.as_view(), name='progress_list'),
    path('progress/<int:pk>/', ProgressDetailView.as_view(), name='progress_detail'),
    path('progress/create/', ProgressCreateView.as_view(), name='progress_create'),
    path('progress/<int:pk>/update/', ProgressUpdateView.as_view(), name='progress_update'),
    path('progress/<int:pk>/delete/', progress_delete, name='progress_delete'),

    # Performance Report URLs
    path('performance_reports/', PerformanceReportListView.as_view(), name='performance_report_list'),
    path('performance_reports/<int:pk>/', PerformanceReportDetailView.as_view(), name='performance_report_detail'),
    path('performance_reports/create/', PerformanceReportCreateView.as_view(), name='performance_report_create'),
    path('performance_reports/<int:pk>/update/', PerformanceReportUpdateView.as_view(), name='performance_report_update'),
    path('performance_reports/<int:pk>/delete/', performance_report_delete, name='performance_report_delete'),

]
