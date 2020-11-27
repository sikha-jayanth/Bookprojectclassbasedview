from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from books.models import Book
from django.urls import reverse_lazy

# Create your views here.
class listBooks(ListView):
    model=Book
    context_object_name = "books"

class CreateBook(CreateView):
    model=Book
    fields=["Book_name","author","pages","price"]
    success_url=reverse_lazy("listview")

class BookDetails(DetailView):
    model=Book

class DeleteBook(DeleteView):
    model=Book
    success_url=reverse_lazy("listview")

class UpdateBook(UpdateView):
    model=Book
    template_name="books/book_edit.html"
    fields=["Book_name","author","pages","price"]
    success_url=reverse_lazy("listview")


