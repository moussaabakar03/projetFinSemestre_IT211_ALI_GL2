from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('acceuil/', views.reponseHtml),
    path('acceuil2/', views.reponseHtml2)    
]
