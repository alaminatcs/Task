from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'meals'),
    path('contact/', views.contact, name = 'contact'),
    path('order/', views.order, name = 'order'),
    path('form/', views.formCall, name = 'form')
]
