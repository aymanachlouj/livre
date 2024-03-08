from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    """
    Author model
    """
    name = models.CharField(max_length=100, unique=True, verbose_name=_('name'))

    def __str__(self):
        return self.name
    
    def get_books(self):
        return Book.objects.filter(author=self)


class Book(models.Model):
    """
    Book model
    """
    title = models.CharField(max_length=100, verbose_name=_('title'))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('author'))
    description = models.TextField(verbose_name=_('description'), blank=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name=_('cover'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self):
        return self.title


class Cart(models.Model):
    """
    Cart model
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name=_('user'))
    books = models.ManyToManyField(Book, verbose_name=_('books'), related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.user.username

