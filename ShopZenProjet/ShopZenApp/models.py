from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories')
    
    def __str__(self):
        return self.nom

class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='produits')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    dateAjoutProduit = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Nom produit: ", self.nom, "categorie: ", self.categorie.nom, "prix Unitaire: ", self.prix, "quantité: ", self.quantite

class PanierClient(models.Model):
    nomClient = models.CharField(max_length=255)
    achats = models.ManyToManyField(Produit, through='Achat')
    
    def __str__(self):
        return self.nomClient

class Achat(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    panierDuClient = models.ForeignKey(PanierClient, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    dateAchat = models.DateTimeField(auto_now_add=True)
    modePayement = models.CharField(max_length=255)
    
    def __str__(self):
        return self.produit.nom, "quantité: ", self.quantite, "date achat: ", self.dateAchat, "mode payement: ", self.modePayement
    
    
class Facture (models.Model):
    prixTotal = models.DecimalField(max_digits=10, decimal_places=2)
    
