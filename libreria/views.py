from http.client import HTTPResponse
from django.views.generic import *
from django.shortcuts import render
from .models import *
from django.http import HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Autor
class AutorPageView(LoginRequiredMixin, ListView):
    template_name = 'autor.html'
    model = Autor
    context_object_name = 'Todos_Los_Autores'
    login_url = 'account_login'

class AutorPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'autor_detalle.html'
    model = Autor
    context_object_name = 'Detalle_Autor'
    login_url = 'account_login'


class AutorPageCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'autor_nuevo.html'
    model = Autor
    fields = ('Nombre','ApellidosP','ApellidosM','FechaNac','Genero','Edad','Foto')
    login_url = 'account_login'
    permission_required = 'libreria.Admin_autor'

    def form_valid(self, form):
        form.instance.QuienRegistroAutor = self.request.user
        return super().form_valid(form)


class AutorPageUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'autor_editar.html'
    model = Autor
    fields = ('Nombre','ApellidosP','ApellidosM','FechaNac','Genero','Edad','Foto')
    login_url = 'account_login'
    permission_required = 'libreria.Admin_autor'

    #def dispatch(self, request, *args, **kwargs):
    #    obj = self.get_object()
    #    if obj.QuienRegistroAutor != self.request.user:
    #        raise PermissionDenied
    #    return super().dispatch(request, *args, **kwargs)

class AutorPageDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = '/autores/'
    template_name = 'autor_delete.html'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):      
        if request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Biblioteca
class BibliotecaPageView(LoginRequiredMixin, ListView):
    template_name = 'biblioteca.html'
    model = Biblioteca
    context_object_name = 'Todas_Las_Bibliotecas'
    login_url = 'account_login'

class BibliotecaPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'biblioteca_detalle.html'
    model = Biblioteca
    context_object_name = 'Detalle_Biblioteca'
    login_url = 'account_login'

class BibliotecaPageCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'biblioteca_nuevo.html'
    model = Biblioteca
    fields = ('Nombre', 'Direccion', 'Telefono', 'HorarioApertura', 'HorarioCierre')
    login_url = 'account_login'
    permission_required = 'libreria.Admin_biblioteca'

    def form_valid(self, form):
        form.instance.QuienRegistroBiblioteca = self.request.user
        return super().form_valid(form)

class BibliotecaPageUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'biblioteca_editar.html'
    model = Biblioteca
    fields = ('Nombre', 'Direccion', 'Telefono', 'HorarioApertura', 'HorarioCierre')
    login_url = 'account_login'
    permission_required = 'libreria.Admin_biblioteca'

    #def dispatch(self, request, *args, **kwargs):
    #    obj = self.get_object()
    #    if obj.QuienRegistroBiblioteca != self.request.user:
    #        raise PermissionDenied
    #    return super().dispatch(request, *args, **kwargs)

class BibliotecaPageDelete(LoginRequiredMixin, DeleteView):
    model = Biblioteca
    success_url = '/bibliotecas/'
    template_name = 'biblioteca_delete.html'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):      
        if request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Editorial
class EditorialPageView(LoginRequiredMixin, ListView):
    template_name = 'editorial.html'
    model = Editorial
    context_object_name = 'Todas_Las_Editoriales'
    login_url = 'account_login'

class EditorialPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'editorial_detalle.html'
    model = Editorial
    context_object_name = 'Detalle_Editorial'
    login_url = 'account_login'


class EditorialPageCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'editorial_nuevo.html'
    model = Editorial
    fields = ('Nombre', 'FechaCreacion', 'Logo', 'Ubicacion')
    login_url = 'account_login'
    permission_required = 'libreria.Admin_editorial'

    def form_valid(self, form):
        form.instance.QuienRegistroEditorial = self.request.user
        return super().form_valid(form)

class EditorialPageUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'editorial_editar.html'
    model = Editorial
    fields = ('Nombre', 'FechaCreacion', 'Logo', 'Ubicacion')
    login_url = 'account_login'
    permission_required = 'libreria.Admin_editorial'

    #def dispatch(self, request, *args, **kwargs):
    #    obj = self.get_object()
    #    if obj.QuienRegistroEditorial != self.request.user:
    #        raise PermissionDenied
    #    return super().dispatch(request, *args, **kwargs)

class EditorialPageDelete(LoginRequiredMixin, DeleteView):
    model = Editorial
    success_url = '/editoriales/'
    template_name = 'editorial_delete.html'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):      
        if request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Libro
class LibroPageView(LoginRequiredMixin, ListView):
    template_name = 'libro.html'
    model = Libro
    context_object_name = 'Todos_Los_Libros'
    login_url = 'account_login'

class LibroPageDetail(LoginRequiredMixin, DetailView):
    template_name = 'libro_detalle.html'
    model = Libro
    context_object_name = 'Detalle_Libro'
    login_url = 'account_login'

class LibroPageCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'libro_nuevo.html'
    model = Libro
    fields = ('Nombre', 'NumSerie', 'Editorial', 'Autor', 'Biblioteca', 'Precio', 'Genero', 'Portada')
    login_url = 'account_login'
    permission_required = 'libreria.Admin_libro'

    def form_valid(self, form):
        form.instance.QuienRegistroLibro = self.request.user
        return super().form_valid(form)

class LibroPageUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'libro_editar.html'
    model = Libro
    fields = ('Nombre', 'NumSerie', 'Editorial', 'Autor', 'Biblioteca', 'Precio', 'Genero', 'Portada')
    login_url = 'account_login'
    permission_required = 'libreria.Admin_libro'

    #def dispatch(self, request, *args, **kwargs):
    #    obj = self.get_object()
    #    if obj.QuienRegistroLibro != self.request.user:
    #        raise PermissionDenied
    #    return super().dispatch(request, *args, **kwargs)

class LibroPageDelete(LoginRequiredMixin, DeleteView):
    model = Libro
    success_url = '/libros/'
    template_name = 'libro_delete.html'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):      
        if request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Comentarios: Autor
class ComentariosAutorPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentarios_autor_nuevo.html'
    model = ComentariosAutor
    fields = ('comentario',)
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        form.instance.autor_id = self.kwargs['pk']
        return super().form_valid(form)

class ComentariosAutorPageDelete(LoginRequiredMixin, DeleteView):
    model = ComentariosAutor
    success_url = '/autores/'
    template_name = 'comentarios_autor_delete.html'
    context_object_name = 'ComentarioAutor'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Comentarios: Biblioteca
class ComentariosBibliotecaPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentarios_biblioteca_nuevo.html'
    model = ComentariosBiblioteca
    fields = ('comentario',)
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        form.instance.biblioteca_id = self.kwargs['pk']
        return super().form_valid(form)

class ComentariosBibliotecaPageDelete(LoginRequiredMixin, DeleteView):
    model = ComentariosBiblioteca
    success_url = '/bibliotecas/'
    template_name = 'comentarios_biblioteca_delete.html'
    context_object_name = 'ComentarioBiblioteca'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Comentarios: Editorial
class ComentariosEditorialPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentarios_editorial_nuevo.html'
    model = ComentariosEditorial
    fields = ('comentario',)
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        form.instance.editorial_id = self.kwargs['pk']
        return super().form_valid(form)

class ComentariosEditorialPageDelete(LoginRequiredMixin, DeleteView):
    model = ComentariosEditorial
    success_url = '/editoriales/'
    template_name = 'comentarios_editorial_delete.html'
    context_object_name = 'ComentarioEditorial'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Comentarios: Libro
class ComentariosLibroPageCreate(LoginRequiredMixin, CreateView):
    template_name = 'comentarios_libro_nuevo.html'
    model = ComentariosLibro
    fields = ('comentario',)
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        form.instance.libro_id = self.kwargs['pk']
        return super().form_valid(form)

class ComentariosLibroPageDelete(LoginRequiredMixin, DeleteView):
    model = ComentariosLibro
    success_url = '/libros/'
    template_name = 'comentarios_libro_delete.html'
    context_object_name = 'Comentario'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseNotFound('<h1>Pagina no encontrada</h1>')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Busquedas

class ResultadoLibroBusquedaListView(LoginRequiredMixin, ListView):
    model = Libro
    template_name  = 'libro_resul_busqueda.html'
    context_object_name = 'Busqueda_Libros'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Libro.objects.filter(Q(Nombre__icontains = query ))

class ResultadoEditorialBusquedaListView(LoginRequiredMixin, ListView):
    model = Editorial
    template_name  = 'editorial_resul_busqueda.html'
    context_object_name = 'Busqueda_Editoriales'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Editorial.objects.filter(Q(Nombre__icontains = query ))

class ResultadoBibliotecaBusquedaListView(LoginRequiredMixin, ListView):
    model = Biblioteca
    template_name  = 'biblioteca_resul_busqueda.html'
    context_object_name = 'Busqueda_Bibliotecas'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Biblioteca.objects.filter(Q(Nombre__icontains = query ))

class ResultadoAutorBusquedaListView(LoginRequiredMixin, ListView):
    model = Autor
    template_name  = 'autor_resul_busqueda.html'
    context_object_name = 'Busqueda_Autores'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Autor.objects.filter(Q(Nombre__icontains = query ))