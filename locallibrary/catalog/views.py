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

    num_books_word = Book.objects.filter(title__icontains = 'the').count()
    num_genres_word = Genre.objects.filter(name__icontains = 'sport').count()
    

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_books_instances': num_books_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_word': num_books_word,
        'num_genres_word': num_genres_word,
        'num_visits': num_visits,
    }

    #Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


#For class-based view
from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
