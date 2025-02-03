from django import forms

class formCategorie(forms.Form):
    nom = forms.CharField(max_length=100, label='Nom de la categorie')
    description = forms.CharField(max_length=100, label='Description de la categorie')
    image = forms.ImageField(label='Image de la categorie')