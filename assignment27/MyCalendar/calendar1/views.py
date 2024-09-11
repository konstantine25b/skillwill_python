from django.shortcuts import render
from .models import Calendar1

def calendar_view(request, year, month, day):
    date = Calendar1.objects.create(year=year, month=month, day=day)
    return render(request, 'calendar.html', {'date': date})