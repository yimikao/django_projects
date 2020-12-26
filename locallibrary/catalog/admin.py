from django.contrib import admin

# Register your models here.
from .models import Book, BookInstance, Author, Genre, Language

#admin.site.register(Book)
#3admin.site.register(BookInstance)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(Language)


class BookInline(admin.TabularInline):
    extra = 0
    model = Book
    exclude = ['summary','genre']
#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

#Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    extra = 0
    model = BookInstance

#Define and register the admin classes for Book using @register decorator(same as admin.site.reg())
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #pass
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


#Define and register the admin classes for BookInstance using decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    #pass
    list_display = ('id', 'book', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')})
    )

