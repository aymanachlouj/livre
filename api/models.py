from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Livre(models.Model):
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='files/cover')

    def __str__(self):
        return self.titre

class PanierElement(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.livre.titre}"