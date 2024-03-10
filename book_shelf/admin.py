from django.contrib import admin
from .models import Book, Author, Cart

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description',)



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'display_books')  
        # Ajoutez les autres champs que vous souhaitez afficher
    filter_horizontal = ('books',)  # Permet de sélectionner les livres dans l'interface d'administration


    def display_books(self, obj):
        return ", ".join([book.title for book in obj.books.all()])  # Assurez-vous que le champ s'appelle "books" dans votre modèle Cart

    display_books.short_description = 'Books'  # Définir un libellé personnalisé pour l'en-tête de la colonne




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_books')

    def display_books(self, obj):
        """
        Affiche les livres associés à chaque auteur
        """
        return " / ".join([book.title for book in obj.get_books()]) 

 
