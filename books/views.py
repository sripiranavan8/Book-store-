from django.shortcuts import render
# import json

from books.models import Book

# Create your views here.
# booksData = open(
#     '/home/sripiranavan/Development/python/django/bookstore-project/books.json').read()

# data = json.loads(booksData)


def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)


def show(request, id):
    singleBook = Book.objects.get(pk=id)
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)
