from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.reader_dashboard, name='reader_dashboard'),
]
