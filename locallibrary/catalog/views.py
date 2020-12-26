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

from django.contrib.auth.mixins import LoginRequiredMixin

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
    # redirect_field_name = 'redirect_to'

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author
    # redirect_field_name = 'redirect_to'

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books to loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
        