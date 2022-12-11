from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Biblioteca(models.Model):
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=300)
    Telefono = models.CharField(max_length=10)
    HorarioApertura = models.TimeField()
    HorarioCierre = models.TimeField()
    QuienRegistroBiblioteca = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('biblioteca')

    class Meta:
        permissions = [
            ('Admin_biblioteca', 'Puede: Editar y Crear Bibliotecas')
        ]

class Autor(models.Model):
    Nombre = models.CharField(max_length=100)
    ApellidosP = models.CharField(max_length=100)
    ApellidosM = models.CharField(max_length=100)
    FechaNac = models.DateField()

    Seleccionar = 'Seleccionar'
    Masculino = 'Masculino'
    Femenino = 'Femenino'

    TipoDeGenero = [
        (Seleccionar, 'Seleccionar'),
        (Masculino, 'Masculino'),
        (Femenino, 'Femenino'),
    ]
    Genero = models.CharField(max_length=20, choices=TipoDeGenero, default = 'Seleccionar')

    Edad = models.IntegerField()
    Foto = models.ImageField(upload_to='poster/', blank=True)
    QuienRegistroAutor = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('autor')

    class Meta:
        permissions = [
            ('Admin_autor', 'Puede: Editar y Crear Autores')
        ]

class Editorial(models.Model):
    Nombre = models.CharField(max_length=150)
    FechaCreacion = models.DateField()
    Logo = models.ImageField(upload_to='poster/', blank=True)
    Ubicacion = models.CharField(max_length=300)
    QuienRegistroEditorial = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('editorial')

    class Meta:
        permissions = [
            ('Admin_editorial', 'Puede: Editar y Crear Editoriales')
        ]

class GeneroLiterario(models.Model):
    Nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre


class Libro(models.Model):
    Nombre = models.CharField(max_length=150)
    NumSerie = models.IntegerField()
    Editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    Precio = models.IntegerField()
    Genero = models.ForeignKey(GeneroLiterario, on_delete=models.CASCADE)
    Portada = models.ImageField(upload_to='poster/', blank=True)
    QuienRegistroLibro = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('libro')

    class Meta:
        permissions = [
            ('Admin_libro', 'Puede: Editar y Crear Libros')
        ]

class Compras(models.Model):
    NombreUsuario = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    NombreLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return self.NombreLibro
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Comentarios
#---------------------------------------------------------------------------------------------------------
class ComentariosAutor(models.Model):
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE, related_name='comentariosAutor',)
    comentario = models.CharField(max_length=200)
    creador = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('autor_detalle', args=[str(self.autor_id)])
#---------------------------------------------------------------------------------------------------------
class ComentariosBiblioteca(models.Model):
    biblioteca = models.ForeignKey(Biblioteca, on_delete = models.CASCADE, related_name='comentariosBiblioteca',)
    comentario = models.CharField(max_length=200)
    creador = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('biblioteca_detalle', args=[str(self.biblioteca_id)])
#---------------------------------------------------------------------------------------------------------
class ComentariosEditorial(models.Model):
    editorial = models.ForeignKey(Editorial, on_delete = models.CASCADE, related_name='comentariosEditorial',)
    comentario = models.CharField(max_length=200)
    creador = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('editorial_detalle', args=[str(self.editorial_id)])
#---------------------------------------------------------------------------------------------------------
class ComentariosLibro(models.Model):
    libro = models.ForeignKey(Libro, on_delete = models.CASCADE, related_name='comentarios',)
    comentario = models.CharField(max_length=200)
    creador = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('libro_detalle', args=[str(self.libro_id)])