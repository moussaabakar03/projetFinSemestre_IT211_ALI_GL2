import re
from django.db import models
from django.forms import ValidationError

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='categories', null=True, blank=True)
    
    def __str__(self):
        return self.nom
    
    # def save(self, *args, **kwargs):
    #     if not re.search(r'[a-zA-Z]', self.nom):  # Vérifie s'il y a au moins une lettre
    #         raise ValidationError("Le champ 'nom' ne peut pas contenir uniquement des chiffres.")
    #     super().save(*args, **kwargs)
          
class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='produits', null=True, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField()
    dateAjoutProduit = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nom}"

class PanierClient(models.Model):
    nomClient = models.CharField(max_length=255)
    achats = models.ManyToManyField(Produit, through='Achat')
    
    def __str__(self):
        return f"{self.id} {self.nomClient}"

class Achat(models.Model):
    MODE_PAIEMENT_CHOICES = [
        ('En spece', 'En spece'),
        ('carte_credit', 'Carte de crédit'),
        ('tmoney', 'TMoney'),
        ('flooz', 'Flooz')
    ]
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='achats')
    panierDuClient = models.ForeignKey(PanierClient, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prixUnitaire = models.DecimalField(max_digits=10, decimal_places=2)
    dateAchat = models.DateTimeField(auto_now_add=True)
    modePayement = models.CharField(
        max_length=20, 
        choices=MODE_PAIEMENT_CHOICES, 
        default='En spece'
    )
    prixTotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.prixUnitaire:  # Vérifier si le prixUnitaire n'est pas encore défini
            self.prixUnitaire = self.produit.prix  # Récupérer le prix du produit
        
        if self.quantite is not None:
            self.prixTotal = self.prixUnitaire * self.quantite  # Calculer le prix total
            
            
        # achat_existant = Achat.objects.filter(
        #     produit=self.produit, 
        #     panierDuClient=self.panierDuClient
        # ).first()

        # if achat_existant:
        #     # Si l'achat existe, augmenter la quantité et mettre à jour le prix total
        #     achat_existant.quantite += self.quantite
        #     achat_existant.prixTotal = achat_existant.quantite * achat_existant.prixUnitaire
        #     achat_existant.save()
        # else:
        #     # Calcul du prix total pour un nouvel achat
        #     self.prixTotal = (self.quantite) * self.prixUnitaire
        super().save(*args, **kwargs)
        
    # Réduire la quantité du produit après achat
        self.reduireQuantiteProduit()
        
        
    def reduireQuantiteProduit(self):
    #     """ Réduit la quantité du produit acheté du stock disponible. """
        if self.quantite is not None and self.quantite <= self.produit.quantite and self.produit.quantite > 0 and self.quantite > 0:
            self.produit.quantite -= self.quantite
            self.produit.save()
    
    def augmenterQuantiteProduitSuppAchat(self):
        if self.produit:
            self.produit.quantite += self.quantite
            self.produit.save()
            
    def delete(self, *args, **kwargs):
        self.augmenterQuantiteProduitSuppAchat()
        super().delete(*args, **kwargs)    
        
    def update(self, *args, **kwargs):
        if self.produit:
            self.produit.quantite += self.quantite
            self.produit.save()
        super().update(*args, **kwargs)
    
    # def delete(self, *args, **kwargs):
    #     # self.augmenterQuantiteProduitSuppAchat()
    #     if self.produit:
    #         self.produit.quantite += self.quantite
    #         self.produit.save()
    #     super().delete(*args, **kwargs)   
      
    def __str__(self):
        return self.produit.nom, "quantité: ", self.quantite, "date achat: ", self.dateAchat, "mode payement: ", self.modePayement
    
    
class Facture (models.Model):
    prixTotal = models.DecimalField(max_digits=10, decimal_places=2)
    dateFacture = models.DateTimeField(auto_now_add=True)
    # nomClient = models.CharField(max_length=255)
    
