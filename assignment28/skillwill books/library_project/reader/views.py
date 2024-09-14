from django.shortcuts import render
from .models import Reader
from book.models import Book

def reader_dashboard(request):
    reader = Reader.objects.get(user=request.user)
    books = Book.objects.filter(genre=reader.favorite_genre)
    return render(request, 'reader_dashboard.html', {'reader': reader, 'books': books})
