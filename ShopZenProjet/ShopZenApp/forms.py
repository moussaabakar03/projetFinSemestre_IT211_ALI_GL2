from django import forms
from . models import Achat, Categorie, Produit, PanierClient

class formCategorie(forms.Form):
    nom = forms.CharField(max_length=100, label='Nom de la categorie')
    description = forms.CharField(max_length=100, label='Description de la categorie')
    image = forms.ImageField(label='Image de la categorie', required=False)
    

class formProduit(forms.Form):
    categorie = forms.ModelChoiceField(label ="Categorie ", queryset=Categorie.objects.all())
    nom = forms.CharField(label ="Nom ", max_length=255)
    description = forms.CharField(label ="Description ", widget= forms.Textarea())
    image = forms.ImageField(label ="Image", required=False)
    prix = forms.DecimalField(label ="Prix ", max_digits=10, decimal_places=2)
    quantite = forms.IntegerField(label ="Quantite ")


class PannierClient(forms.Form):
    nomClient = forms.CharField(label= "Nom du client ", max_length= 260, required= False)
    

class formAchat(forms.Form):
    produit = forms.ModelChoiceField(label= "Produit", queryset=Produit.objects.all())
    panierDuClient = forms.ModelChoiceField(label= "Numero pannier du client:", queryset=PanierClient.objects.all())
    quantite = forms.IntegerField()
    # prixUnitaire = forms.DecimalField(label ="Prix unitaire ", max_digits=10, decimal_places=2)
    # dateAchat = forms.DateTimeField(auto_now_add=True)
    modePayement = forms.CharField(max_length=255)
    # Utiliser ChoiceField pour afficher une liste déroulante
    modePayement = forms.ChoiceField(
        choices=Achat.MODE_PAIEMENT_CHOICES,  # Utilisation des choices définies dans le modèle
        label= "Mode de payement "
    )
    # prixTotal = forms.DecimalField(label ="Prix total ", max_digits=10, decimal_places=2)

    
class formFactureClient(forms.Form):
    panierDuClient = forms.ModelChoiceField(label= "Identifiant pannier du client:", queryset=PanierClient.objects.all())