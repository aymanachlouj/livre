from django.contrib import admin
from .models import Livre

class LivreAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Livre, LivreAdmin)