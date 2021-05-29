from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
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
    # try:
    #     singleBook = Book.objects.get(pk=id)
    # except Book.DoesNotExist:
    #     raise Http404('Book not found')
    singleBook = get_object_or_404(Book, pk=id)
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)
