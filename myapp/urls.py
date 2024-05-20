from django.urls import path
from . import views

urlpatterns = [
    path('', views.package_list, name='package_list'),
    path('package/<int:pk>/', views.package_detail, name='package_detail'),
    path('package/new/', views.package_create, name='package_create'),
    path('package/<int:pk>/edit/', views.package_update, name='package_update'),
    path('package/<int:pk>/delete/', views.package_delete, name='package_delete'),
]
