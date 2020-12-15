from django.shortcuts import render

# Create your views here.
from catalog.models import Book, BookInstance, Author, Genre

def index(request):
    """View function for home page of site"""

    #Generate counts for some of the main objects
    num_books = Book.objects.all().count()
    num_books_instances = BookInstance.objects.all().count()

    #availabe books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    #the 'all()' is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_books_instances': num_books_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    #Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)