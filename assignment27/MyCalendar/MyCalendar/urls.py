from django.urls import path, include

urlpatterns = [
    path('calendar/', include('calendar1.urls')),
    path('user/', include('user.urls')),
]