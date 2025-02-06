from django.shortcuts import render, redirect, get_object_or_404
from . models import Categorie, Produit 
from . forms import formCategorie, formProduit
# Create your views here.

def reponseHtml(request):
    return render(request, 'acceuil.html')

def reponseHtml2(request):
    return render(request, 'acceuil3.html')


#/categorie/ listeCategorie: URL menant à la page de la liste des categories 
#Methode d'affichage de la liste des Categories 
def listeCategorie(request):
    listcategories = Categorie.objects.all()
    return render(request, 'categorie/listeCategorie.html', {'listcategories': listcategories})


#/categorie/ ajoutcategorie:  URL menant à la page d'ajout d'une categorie
#Methode d'ajout d'un categorie
def ajoutCategorie(request):
    #Requête POST 
    if request.method == 'POST':
        #1 Récuperer les données
        categorie = formCategorie(request.POST, request.FILES)
        #2 Validé les données
        if categorie.is_valid():
            #3 Preparation des données 
            noms = categorie.cleaned_data['nom']
            descriptions = categorie.cleaned_data['description']
            image = categorie.cleaned_data['image']
            # 4 Création et sauvegarde d'une categorie
            oCat1 = Categorie(nom=noms, description=descriptions, image=image)
            oCat1.save()
            #5 Rediriger vers page de liste des categories
            return redirect("listeCateg")
    else:
        #Formulaire vide pour requête GET 
        categorie = formCategorie()
    return render(request, 'categorie/ajoutCategorie.html', {'categories': categorie})



#Methode suppression d'un client 
def supprimerCategorie(request, id):
    if request.method == 'GET':
        # id = request.GET.get('id')
        categorie = get_object_or_404(Categorie, id=id)
        categorie.delete()
        return redirect("listeCateg")
    
    
def modifierCategorie(request, id):
    # Récupérer la catégorie ou renvoyer une erreur 404 si elle n'existe pas
    categorie = get_object_or_404(Categorie, id=id)
    
    if request.method == 'POST':
        form = formCategorie(request.POST, request.FILES)
        if form.is_valid():
            # Mettre à jour la catégorie existante
            categorie.nom = form.cleaned_data['nom']
            categorie.description = form.cleaned_data['description']
            categorie.image = form.cleaned_data['image']
            categorie.save()
            return redirect("listeCateg")  # Redirection après modification
    else:
        # Pré-remplir le formulaire avec les valeurs actuelles de la catégorie
        form = formCategorie(initial={
            'nom': categorie.nom,
            'description': categorie.description,
            # 'image': None
            'image': categorie.image
        })
    
    # Passer `categorie` au template
    return render(request, 'categorie/modifierCategorie.html', {'form': form, 'categorie': categorie})


def listeProduits(request): 
    listproduits = Produit.objects.all()
    content = {'listproduits': listproduits}
    return render(request, 'produit/produitListe.html', content)
    
    
    
#/produit/ listeProduit: URL menant à la page de la liste des Produit 
#Methode d'affichage de la liste des produits 
def listeProduitParCategorie(request, id):
    if request.method == 'GET':
        categorie = get_object_or_404(Categorie, id=id)
        listproduits = Produit.objects.filter(categorie=id)
        return render(request, 'produit/listeProduitParCategorie.html', {'listproduits': listproduits, 'categorie': categorie})


def ajoutProduit(request):
    #Requête POST 
    if request.method == 'POST':
        
        #1 Récuperer les données
        
        produit = formProduit(request.POST, request.FILES)
        
        #2 Validé les données
        
        if produit.is_valid():
            
            #3 Preparation des données
            
            categories = produit.cleaned_data['categorie']
            noms = produit.cleaned_data['nom']
            descriptions = produit.cleaned_data['description']            
            prix = produit.cleaned_data['prix']
            images = produit.cleaned_data['image']
            quantites = produit.cleaned_data['quantite']
            
            # 4 Création et sauvegarde d'un produit
            oProduit1 = Produit(categorie=categories, nom=noms, description=descriptions, image =images, prix=prix, quantite=quantites)
            oProduit1.save()
                       
            return redirect("listeProduit" , id=categories.id)
    else:
        #Requête GET
        produit = formProduit()
    return render(request, 'produit/ajoutProduit.html', {'produits': produit})


def supprimerProduit(request, id):
    #id = request.GET.get('id')
    # id = request.GET.get('id') pas important comme id est déjà en parmetre!!
    produit = get_object_or_404(Produit, id=id)
    produit.delete()
    categorie_id = produit.categorie.id  # Stocker l'ID de la catégorie avant de supprimer
    return redirect("listeProduit", categorie_id)
