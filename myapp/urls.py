from django.urls import path
from . import views
from myapp.views import ViewPackages

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('add-package/', views.addPackage, name='add-package'),
    path('view-packages/',ViewPackages.as_view(),name ='view-packages'),
]