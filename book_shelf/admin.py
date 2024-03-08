from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description',)




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_books')

    def display_books(self, obj):
        """
        Affiche les livres associés à chaque auteur
        """
        return " / ".join([book.title for book in obj.get_books()]) 

 
