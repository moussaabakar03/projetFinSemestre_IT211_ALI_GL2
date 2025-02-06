from django import forms
from . models import Categorie

class formCategorie(forms.Form):
    nom = forms.CharField(max_length=100, label='Nom de la categorie')
    description = forms.CharField(max_length=100, label='Description de la categorie')
    image = forms.ImageField(label='Image de la categorie')
    

class formProduit(forms.Form):
    categorie = forms.ModelChoiceField(label ="Categorie ", queryset=Categorie.objects.all())
    nom = forms.CharField(label ="Nom ", max_length=255)
    description = forms.CharField(label ="Description ", widget= forms.Textarea())
    image = forms.ImageField(label ="Image ")
    prix = forms.DecimalField(label ="Prix ", max_digits=10, decimal_places=2)
    quantite = forms.IntegerField(label ="Quantite ")
    