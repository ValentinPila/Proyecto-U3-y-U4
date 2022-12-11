from django.urls import path
from .views import *

urlpatterns = [
    path('', OrdersPageView.as_view(), name='orders'),
    path('charge/', charge, name='charge'),
    path('<int:pk>/', OrderLibro.as_view(), name='pago_libro')
]