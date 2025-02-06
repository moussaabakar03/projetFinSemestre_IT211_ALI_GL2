from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('listeCategorie/', views.listeCategorie, name='listeCateg'),
    # path('listeCate/', views.listeCategorie, name='listeCate'),
    path('ajoutCateg/', views.ajoutCategorie, name='ajoutCateg'),
    path('suppCatego/<int:id>/', views.supprimerCategorie, name='suppCategorie'),
    path('modifierCategorie/<int:id>/', views.modifierCategorie, name='modifierCategorie'),
    path('listeProduits/', views.listeProduits, name='listeProduits'),
    path('listeProduitParCategorie/<int:id>/', views.listeProduitParCategorie, name='listeProduit'),
    path('ajoutProduit/', views.ajoutProduit, name='ajoutProduit'),
    path('supprimerProduit/<int:id>/', views.supprimerProduit, name='supprimerProduit')
]