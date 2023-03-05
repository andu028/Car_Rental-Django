from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]