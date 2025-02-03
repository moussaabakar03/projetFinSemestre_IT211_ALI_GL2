from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('listeCategorie/', views.listeCategorie, name='listeCateg'),
    # path('listeCate/', views.listeCategorie, name='listeCate'),
    path('ajoutCateg/', views.ajoutCategorie, name='ajoutCateg'),
    path('suppCatego/<int:id>/', views.supprimerCategorie, name='suppCategorie')
    # path('acceuil2/', views.reponseHtml2)    
]
