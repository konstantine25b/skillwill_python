from django.shortcuts import render
from .models import UserProfile

def user_view(request, user_id):
    user = UserProfile.objects.get(id=user_id)
    age = user.calculate_age()
    return render(request, 'user.html', {'user': user, 'age': age})
