# car_animal_app/urls.py
from django.urls import path
from .views import CarListCreateView, CarDetailView, AnimalListCreateView, AnimalDetailView

urlpatterns = [
    # Car URLs
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),

    # Animal URLs
    path('animals/', AnimalListCreateView.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
]
