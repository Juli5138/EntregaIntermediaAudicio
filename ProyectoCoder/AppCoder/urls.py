from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('autor/', views.autor,name='Autor'),
    path('autorApi/', views.autoresapi),
    path('profesores/',views.profesores),
]
