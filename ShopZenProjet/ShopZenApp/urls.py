from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listeCategorie, name='listeCateg'),
    path('ajoutCateg/', views.ajoutCategorie, name='ajoutCateg'),
    path('suppCatego/<int:id>/', views.supprimerCategorie, name='suppCategorie'),
    path('modifierCategorie/<int:id>/', views.modifierCategorie, name='modifierCategorie'),
    
    
    path('listeProduits/', views.listeProduits, name='listeProduits'),
    path('listeProduitParCategorie/<int:id>/', views.listeProduitParCategorie, name='listeProduit'),
    path('ajoutProduit/', views.ajoutProduit, name='ajoutProduit'),
    path('supprimerProduit/<int:id>/', views.supprimerProduit, name='supprimerProduit'),
    path('modifierProduit/<int:id>/', views.modifierProduit, name='modifierProduit'),
    # path('filtrerProduit/<str:nom>/', views.filtrerProduit, name='filtrerProduit'),
    
    
    path('produitPannier/', views.produitPannier, name='produitPannier'),
    path('ajoutPannier/', views.ajoutPannier, name='ajoutPannier'),
    path('ajoutProduitPannier/<int:id>/', views.ajoutProduitPannier, name='ajoutProduitPannier'), 
    
    
    path('listeAchat/', views.listeAchat, name='listeAchat'),
    path('supprimerAchat/<int:id>/', views.supprimerAchat, name='supprimerAchat'),
    
    
    
    path('idClientFacture/', views.idClientFacture, name='idClientFacture'),
    path('imprimerFactures/<int:id>/', views.imprimerFactures, name='imprimerFactures'),
    
]