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
        return f"{self.nom}"

class PanierClient(models.Model):
    nomClient = models.CharField(max_length=255)
    achats = models.ManyToManyField(Produit, through='Achat')
    
    def __str__(self):
        return f"{self.id} {self.nomClient}"

class Achat(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    panierDuClient = models.ForeignKey(PanierClient, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prixUnitaire = models.DecimalField(max_digits=10, decimal_places=2)
    dateAchat = models.DateTimeField(auto_now_add=True)
    modePayement = models.CharField(max_length=255)
    prixTotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.prixUnitaire:  # Vérifier si le prixUnitaire n'est pas encore défini
            self.prixUnitaire = self.produit.prix  # Récupérer le prix du produit
        
        if self.quantite is not None:
            self.prixTotal = self.prixUnitaire * self.quantite  # Calculer le prix total
            
        super().save(*args, **kwargs) 
    
      # Réduire la quantité du produit après achat
    #     self.reduireQuantiteProduit()

    # def reduireQuantiteProduit(self):
    #     """ Réduit la quantité du produit acheté du stock disponible. """
    #     if self.quantite is not None and self.produit.quantite >= self.quantite:
    #         self.produit.quantite -= self.quantite
    #         self.produit.save()
    
    # Réduire la quantité du produit après achat
        self.reduireQuantiteProduit()
    def reduireQuantiteProduit(self):
        if self.quantite is not None and self.quantite <= self.produit.quantite:
            self.produit.quantite -= self.quantite
            self.produit.save()
        
            
    def __str__(self):
        return self.produit.nom, "quantité: ", self.quantite, "date achat: ", self.dateAchat, "mode payement: ", self.modePayement
    
    
class Facture (models.Model):
    prixTotal = models.DecimalField(max_digits=10, decimal_places=2)
    dateFacture = models.DateTimeField(auto_now_add=True)
    # nomClient = models.CharField(max_length=255)
    
