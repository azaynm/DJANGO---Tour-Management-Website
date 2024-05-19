from django.urls import path
from . import views
from myapp.views import ViewPackages, AddPackage, UpdatePackage, DeletePackage

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('packages/', ViewPackages.as_view(), name='view_packages'),
    path('packages/add/', AddPackage.as_view(), name='add_package'),
    path('packages/update/<int:pk>/', UpdatePackage.as_view(), name='update_package'),
    path('packages/delete/<int:pk>/', DeletePackage.as_view(), name='delete_package'),
]