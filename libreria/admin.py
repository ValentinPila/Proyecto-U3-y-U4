from django.contrib import admin
from .models import *

# Register your models here.
class ComentarioInLine(admin.StackedInline):
    model = ComentariosLibro

class LibroAdmin(admin.ModelAdmin):
    inlines = [ComentarioInLine]

admin.site.register(Biblioteca)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(GeneroLiterario)
admin.site.register(Libro)
admin.site.register(Compras)