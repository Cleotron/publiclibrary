from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by("title")
    return render(request, 'pl/book_list.html', {'books': books})
