from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . models import Categorie, Produit, PanierClient, Achat
from . forms import formCategorie, formProduit, PannierClient, formAchat, formFactureClient
# Create your views here.


#/categorie/ listeCategorie: URL menant à la page de la liste des categories 
#Methode d'affichage de la liste des Categories 
def listeCategorie(request):
    listcategories = Categorie.objects.all().order_by('id')
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


# def listeProduits(request): 
#     listproduits = Produit.objects.all().order_by('id')
#     content = {'listproduits': listproduits}
#     return render(request, 'produit/produitListe.html', content)

def listeProduits(request):
    if request.method == "POST":
        nom1 = request.POST.get("produit")
        produits = Produit.objects.all().order_by('id')
        produit = produits.filter(nom__icontains=nom1)
        context = {"listeProduit": produit}
        return render(request, "produit/produitListe.html", context)
    else:
        produits = Produit.objects.all().order_by('id')
        context = {"listeProduit": produits}
        return render(request, "produit/produitListe.html", context)  
    
#/produit/ listeProduit: URL menant à la page de la liste des Produit 
#Methode d'affichage de la liste des produits 
def listeProduitParCategorie(request, id):
    if request.method == 'GET':
        categorie = get_object_or_404(Categorie, id=id)
        listproduits = Produit.objects.filter(categorie=id).order_by('id')
        return render(request, 'produit/listeProduitParCategorie.html', {'listproduits': listproduits, 'categorie': categorie})


#Méthode permettant d'ajouter un produit
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

#Méthode permettant de supprimer un produit
def supprimerProduit(request, id):
    #id = request.GET.get('id')
    # id = request.GET.get('id') pas important comme id est déjà en parmetre!!
    produit = get_object_or_404(Produit, id=id)
    produit.delete()
    categorie_id = produit.categorie.id  # Stocker l'ID de la catégorie avant de supprimer
    return redirect("listeProduit", categorie_id)


#Méthode permettant de modifier un produit
def modifierProduit(request, id):
    # Requête GET
    produits= Produit.objects.get(id = id)
    
    if request.method == 'POST':
        # Requête POST
        produit = formProduit(request.POST, request.FILES)
        
        if produit.is_valid():
            # 3 Preparation des données
            image = produit.cleaned_data['image']
            nom = produit.cleaned_data['nom']
            description = produit.cleaned_data['description']
            categorie = produit.cleaned_data['categorie']
            prix = produit.cleaned_data['prix']
            quantite = produit.cleaned_data['quantite']

            produits.image = image
            produits.nom = nom
            produits.description = description
            produits.categorie = categorie
            produits.prix = prix
            produits.quantite = quantite
            
            produits.save()
            return redirect("listeProduits")
    else:
        # Requête GET
        produit = formProduit(initial= {'image': produits.image, 'nom': produits.nom, 'description': produits.description, 'categorie': produits.categorie, 'prix': produits.prix, 'quantite': produits.quantite})
        # content = {'produit': produit}
    return render(request, 'produit/modifierProduit.html', {'produit': produit, 'produits': produits})

#Méthode permettant de creer un pannier
def produitPannier(request):
    if request.method == "POST":
        nomProduit = request.POST.get("produit", "").strip()  # Éviter les espaces inutiles
        if nomProduit:
            prodPannier = Produit.objects.all().order_by('id')
            prodPanniers = prodPannier.filter(nom__icontains = nomProduit)
            return render(request, 'pannier/produitPannier.html', {'prodPannier': prodPanniers})
        else:
            prodPanniers = Produit.objects.all().order_by('id')
            return render(request, 'pannier/produitPannier.html', {'prodPannier': prodPanniers})

    prodPanniers = Produit.objects.all().order_by('id')
    return render(request, 'pannier/produitPannier.html', {'prodPannier': prodPanniers})


def ajoutPannier(request):
    if request.method == 'POST':
        pannier = PannierClient(request.POST)
        if pannier.is_valid():
            nom = pannier.cleaned_data['nomClient']
            
            oPannier1 = PanierClient(nomClient=nom)
            oPannier1.save()
            
            return redirect('produitPannier')
    else:
        pannier = PannierClient()
        
    return render(request, 'pannier/pannierClient.html', {'pannier': pannier})


#Méthode permettant d'ajouter un produit au pannier
def ajoutProduitPannier(request, id):
    # Requête GET
    produits = Produit.objects.get(id=id)
    
    # recuperer le dernier pannier crée
    dernier_panier = PanierClient.objects.order_by('-id').first()
    if request.method == 'POST':
         # Requête POST
        oFormAchat = formAchat(request.POST)
        if oFormAchat.is_valid():
            # 3 Preparation des données
            produit = oFormAchat.cleaned_data['produit']
            panierDuClient = oFormAchat.cleaned_data['panierDuClient']
            quantite = oFormAchat.cleaned_data['quantite']
            # prixUnitaire = oFormAchat.cleaned_data['prixUnitaire']
            modePayement = oFormAchat.cleaned_data['modePayement']
            # prixTotal = oFormAchat.cleaned_data['prixTotal']
            
            oAchat = Achat(produit = produit, panierDuClient = panierDuClient, quantite=quantite, modePayement = modePayement)
            # idProduit.produit = produit
            # idProduit.panierDuClient = panierDuClient
            produits.quantite = quantite
            # produits.modePayement = modePayement
            
            oAchat.save()
            return redirect('produitPannier')
    else:
        # Requête GET
        # Pré-remplir le formulaire avec le panier ayant l'ID maximal
        oFormAchat = formAchat(initial={'produit': id, 'panierDuClient': dernier_panier, 'quantite': produits.quantite, 'modePayement': 'Carte de crédit'})
        
    return render(request, 'pannier/ajouterProduitPannier.html', {'oFormAchat': oFormAchat, 'id': id})
            
            
def listeAchat(request):
    if request.method == "POST":
        id_pannier = request.POST.get("idPannier").strip() # Supprime les espaces avant et après, pour éviter des erreurs.

        if id_pannier.isdigit():  # Vérifier si c'est un nombre valide
            achats = Achat.objects.filter(panierDuClient=id_pannier).order_by('id')
        else:
            achats = Achat.objects.all().order_by('id')

        return render(request, 'achat/listeAchat.html', {'achat': achats})
    
    # Si ce n'est pas un POST, afficher toutes les données
    achats = Achat.objects.all().order_by('id')
    return render(request, 'achat/listeAchat.html', {'achat': achats})



# def listeAchat(request):
#     if request.method == "POST":
#         idPaniers = request.POST.get("idPannier")
#         if idPaniers.isdigit():
#             achats = Achat.objects.all().order_by('id')
#             achat = achats.filter(panierDuClient = idPaniers)
#             context = {'achat': achat}
#             return render(request, 'achat/listeAchat.html', context)
#         else:
#             achats = Achat.objects.all().order_by('id')
#     else:
#         achats = Achat.objects.all().order_by('id')
#     return render(request, 'achat/listeAchat.html',  {'achat': achats})



def supprimerAchat(request, id):
    idAchat = Achat.objects.get(id=id)
    idAchat.delete()
    return redirect("listeAchat")


#Méthode permettant de modifier un achat au pannier
def modifierAchat(request, id):
    # Requête GET
    idAchat = Achat.objects.get(id=id)
    #1 Récuperer les données
    if request.method == "POST":
        formulaireAchat = formAchat(request.POST)
        #2 Validé les données
        if formulaireAchat.is_valid():
        #3 Preparation des données  
            quantite = formulaireAchat.cleaned_data['quantite']
  

def idClientFacture(request):
    dernier_panier = PanierClient.objects.order_by('-id').first()

    if request.method == 'POST':
        pannier = formFactureClient(request.POST)
        if pannier.is_valid():
            id_panier = pannier.cleaned_data['panierDuClient'].id  # ID sélectionné
            return redirect("imprimerFactures", id=id_panier)  # Redirige vers la facture du panier sélectionné
    else:
    # Si GET, affiche le formulaire avec le dernier panier sélectionné
        pannier = formFactureClient(initial={'panierDuClient': dernier_panier})
    return render(request, 'facture/choixClient.html', {'pannier': pannier, 'idPannier': dernier_panier})

def imprimerFactures(request, id):
    panniers = Achat.objects.filter(panierDuClient=id)
    total= sum(achat.prixTotal for achat in panniers)
    return render(request, 'facture/imprimerFacture.html', {'panniers': panniers, 'prixTotal': total, 'idPannier': id})


