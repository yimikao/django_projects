from django.contrib import admin

# Register your models here.
from .models import Book, BookInstance, Author, Genre, Language

admin.site.register(Book)
admin.site.register(BookInstance)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)

#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

#Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#Define and register the admin classes for Book using @register decorator(same as admin.site.reg())
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


#Define and register the admin classes for BookInstance using decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass