from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CostumUserChangeForm, CostumUserCreationForm
from .models import CostumUser

class CostumUserAdmin(UserAdmin):
    auth_form = CostumUserCreationForm
    model = CostumUser
    form = CostumUserChangeForm
    list_display = ['is_staff', 'username', 'email', 'edad', 'pais']

admin.site.register(CostumUser, CostumUserAdmin)