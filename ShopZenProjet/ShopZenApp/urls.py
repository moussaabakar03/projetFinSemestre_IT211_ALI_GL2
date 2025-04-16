from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Tableau de bord principal
    path('', views.dashBord, name='dashBord'),

    # Gestion des catégories
    path('listeCateg', views.listeCategorie, name='listeCateg'),  # Affiche la liste des catégories
    path('ajoutCateg/', views.ajoutCategorie, name='ajoutCateg'),  # Ajoute une nouvelle catégorie
    path('suppCatego/<int:id>/', views.supprimerCategorie, name='suppCategorie'),  # Supprime une catégorie par ID
    path('modifierCategorie/<int:id>/', views.modifierCategorie, name='modifierCategorie'),  # Modifie une catégorie par ID

    # Gestion des produits
    path('listeProduits/', views.listeProduits, name='listeProduits'),  # Affiche la liste des produits
    path('ProduitDiv/', views.ProduitDiv, name='ProduitDiv'),  # Affichage des produits sous forme de division (div)
    path('listeProduitParCategorie/<int:id>/', views.listeProduitParCategorie, name='listeProduit'),  # Affiche les produits d'une catégorie spécifique
    path('ajoutProduit/', views.ajoutProduit, name='ajoutProduit'),  # Ajoute un nouveau produit
    path('supprimerProduit/<int:id>/', views.supprimerProduit, name='supprimerProduit'),  # Supprime un produit par ID
    path('modifierProduit/<int:id>/', views.modifierProduit, name='modifierProduit'),  # Modifie un produit par ID
    path('modifierProduitDiv/<int:id>/', views.modifierProduitDiv, name='modifierProduitDiv'),  # Modifie l'affichage d'un produit sous forme de div
    # path('filtrerProduit/<str:nom>/', views.filtrerProduit, name='filtrerProduit'),  # Filtrer les produits par nom (commenté)

    # Gestion du panier
    path('produitPannier/', views.produitPannier, name='produitPannier'),  # Affiche les produits dans le panier
    path('ajoutPannier/', views.ajoutPannier, name='ajoutPannier'),  # Ajoute un panier
    path('ajoutProduitPannier/<int:id>/', views.ajoutProduitPannier, name='ajoutProduitPannier'),  # Ajoute un produit spécifique au panier

    # Gestion des achats  
    path('listeAchat/', views.listeAchat, name='listeAchat'),  # Affiche la liste des achats
    path('achatDetail/<int:id>/', views.achatDetail, name='achatDetail'),  
    path('divListeAchat/', views.divListeAchat, name='divListeAchat'),  # Affiche la liste des achats sous forme de division (div)
    path('supprimerAchat/<int:id>/', views.supprimerAchat, name='supprimerAchat'),  # Supprime un achat par ID
    path('modifierAchat/<int:id>/', views.modifierAchat, name='modifierAchat'),  # Modifie un achat par ID

    # Gestion des factures
    path('idClientFacture/', views.idClientFacture, name='idClientFacture'),  # Affiche l'ID du client pour la facture
    path('imprimerFactures/<int:id>/', views.imprimerFactures, name='imprimerFactures'),  # Imprime la facture d'un client spécifique
    path('factureAutoPanier/<int:id>/', views.factureAutoPanier, name='factureAutoPanier'),  # Imprime la facture d'un client spécifique
]










# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     # Tableau de bord principal
#     path('', views.dashBord, name='dashBord'),

    
#     path('listeCateg', views.listeCategorie, name='listeCateg'),
#     path('ajoutCateg/', views.ajoutCategorie, name='ajoutCateg'),
#     path('suppCatego/<int:id>/', views.supprimerCategorie, name='suppCategorie'),
#     path('modifierCategorie/<int:id>/', views.modifierCategorie, name='modifierCategorie'),
    
    
#     path('listeProduits/', views.listeProduits, name='listeProduits'),
#     path('ProduitDiv/', views.ProduitDiv, name='ProduitDiv'),
#     path('listeProduitParCategorie/<int:id>/', views.listeProduitParCategorie, name='listeProduit'),
#     path('ajoutProduit/', views.ajoutProduit, name='ajoutProduit'),
#     path('supprimerProduit/<int:id>/', views.supprimerProduit, name='supprimerProduit'),
#     path('modifierProduit/<int:id>/', views.modifierProduit, name='modifierProduit'),
#     path('modifierProduitDiv/<int:id>/', views.modifierProduitDiv, name='modifierProduitDiv'),
#     # path('filtrerProduit/<str:nom>/', views.filtrerProduit, name='filtrerProduit'),
    
    
#     path('produitPannier/', views.produitPannier, name='produitPannier'),
#     path('ajoutPannier/', views.ajoutPannier, name='ajoutPannier'),
#     path('ajoutProduitPannier/<int:id>/', views.ajoutProduitPannier, name='ajoutProduitPannier'), 
    
    
#     path('listeAchat/', views.listeAchat, name='listeAchat'),
#     path('divListeAchat/', views.divListeAchat, name='divListeAchat'),
#     path('supprimerAchat/<int:id>/', views.supprimerAchat, name='supprimerAchat'),
#     # path('modifierAchat/<int:id>/', views.modifierAchat, name='modifierAchat'),
#     path('modifierAchat/<int:id>/', views.modifierAchat, name='modifierAchat'),
    
    
    
#     path('idClientFacture/', views.idClientFacture, name='idClientFacture'),
#     path('imprimerFactures/<int:id>/', views.imprimerFactures, name='imprimerFactures'),
    
# ]