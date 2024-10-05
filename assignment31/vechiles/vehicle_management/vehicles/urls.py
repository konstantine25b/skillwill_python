from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('add/', views.vehicle_add, name='vehicle_add'),
    path('<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
]
