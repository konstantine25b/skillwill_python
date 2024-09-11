from django.urls import path
from . import views

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/', views.calendar_view, name='calendar_view'),
]