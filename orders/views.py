from django.views.generic import *
from django.conf import settings
import stripe
from django.shortcuts import render
from django.contrib.auth.models import Permission
from libreria.models import Libro
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class OrderLibro(LoginRequiredMixin, DetailView):
    template_name = 'orders/pago_libro.html'
    model = Libro
    context_object_name = 'Libro'
    login_url = 'account_login'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs) 
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context['api_key'] = settings.STRIPE_TEST_SECRET_KEY
        return context

def charge(request):
    if request.method == 'POST':
        precio = int(request.POST['Precio'])*100
        nombre = request.POST['Nombre']

        charge = stripe.Charge.create(
            amount = precio,
            currency = 'usd',
            description = 'Pago del libro: '+nombre+' es: $'+str(precio),
            source = request.POST['stripeToken'],
            api_key = settings.STRIPE_TEST_SECRET_KEY
                                        )
    return render(request, 'orders/charge.html')

class OrdersPageView(TemplateView):
    model = Libro
    context_object_name = 'Todos_Libros'
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs) 
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context['api_key'] = settings.STRIPE_TEST_SECRET_KEY
        return context