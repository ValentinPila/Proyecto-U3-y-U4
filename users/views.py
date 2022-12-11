from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *

# Create your views here.
class SignUpView(CreateView):
    form_class = CostumUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'signup.html'