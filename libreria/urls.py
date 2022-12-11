from django.urls import path 

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    #Autor
    path('autores/', AutorPageView.as_view(), name='autor'),
    path('autores/<int:pk>/', AutorPageDetail.as_view(), name='autor_detalle'),
    path('autores/nuevo/', AutorPageCreate.as_view(), name='autor_nuevo'),
    path('autores/<int:pk>/Editar', AutorPageUpdate.as_view(), name='autor_editar'),
    path('autores/<int:pk>/delete', AutorPageDelete.as_view(), name='autor_delete'),
    path('autores/<int:pk>/comentarios/nuevo/', ComentariosAutorPageCreate.as_view(), name='comentarios_autor_nuevo'),
    path('autores/<int:pk>/comentarios/delete/', ComentariosAutorPageDelete.as_view(), name='comentarios_autor_delete'),
    path('autores/busquedaAutor', ResultadoAutorBusquedaListView.as_view(), name='busqueda_autor'),

    #Biblioteca
    path('bibliotecas/', BibliotecaPageView.as_view(), name='biblioteca'),
    path('bibliotecas/<int:pk>/', BibliotecaPageDetail.as_view(), name='biblioteca_detalle'),
    path('bibliotecas/nuevo/', BibliotecaPageCreate.as_view(), name='biblioteca_nuevo'),
    path('bibliotecas/<int:pk>/Editar', BibliotecaPageUpdate.as_view(), name='biblioteca_editar'),
    path('bibliotecas/<int:pk>/delete', BibliotecaPageDelete.as_view(), name='biblioteca_delete'),
    path('bibliotecas/<int:pk>/comentarios/nuevo/', ComentariosBibliotecaPageCreate.as_view(), name='comentarios_biblioteca_nuevo'),
    path('bibliotecas/<int:pk>/comentarios/delete/', ComentariosBibliotecaPageDelete.as_view(), name='comentarios_biblioteca_delete'),
    path('bibliotecas/busquedaBiblioteca', ResultadoBibliotecaBusquedaListView.as_view(), name='busqueda_biblioteca'),

    #Editorial
    path('editoriales/', EditorialPageView.as_view(), name='editorial'),
    path('editoriales/<int:pk>/', EditorialPageDetail.as_view(), name='editorial_detalle'),
    path('editoriales/nuevo/', EditorialPageCreate.as_view(), name='editorial_nuevo'),
    path('editoriales/<int:pk>/Editar', EditorialPageUpdate.as_view(), name='editorial_editar'),
    path('editoriales/<int:pk>/delete', EditorialPageDelete.as_view(), name='editorial_delete'),
    path('editoriales/<int:pk>/comentarios/nuevo/', ComentariosEditorialPageCreate.as_view(), name='comentarios_editorial_nuevo'),
    path('editoriales/<int:pk>/comentarios/delete/', ComentariosEditorialPageDelete.as_view(), name='comentarios_editorial_delete'),
    path('editoriales/busquedaEditorial', ResultadoEditorialBusquedaListView.as_view(), name='busqueda_editorial'),

    #Libro
    path('libros/', LibroPageView.as_view(), name='libro'),
    path('libros/<int:pk>/', LibroPageDetail.as_view(), name='libro_detalle'),
    path('libros/nuevo/', LibroPageCreate.as_view(), name='libro_nuevo'),
    path('libros/<int:pk>/Editar', LibroPageUpdate.as_view(), name='libro_editar'),
    path('libros/<int:pk>/delete', LibroPageDelete.as_view(), name='libro_delete'),
    path('libros/<int:pk>/comentarios/nuevo/', ComentariosLibroPageCreate.as_view(), name='comentarios_nuevo'),
    path('libros/<int:pk>/comentarios/delete/', ComentariosLibroPageDelete.as_view(), name='comentarios_delete'),
    path('libros/busquedaLibro', ResultadoLibroBusquedaListView.as_view(), name='busqueda_libro'),
]