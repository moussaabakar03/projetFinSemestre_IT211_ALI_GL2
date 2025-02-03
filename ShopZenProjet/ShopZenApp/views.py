from django.shortcuts import render, redirect, get_object_or_404
from . models import Categorie
from . forms import formCategorie
# Create your views here.

def reponseHtml(request):
    return render(request, 'acceuil.html')

def reponseHtml2(request):
    return render(request, 'acceuil3.html')

def listeCategorie(request):
    listcategories = Categorie.objects.all()
    return render(request, 'listeCategorie.html', {'listcategories': listcategories})

def ajoutCategorie(request):
    if request.method == 'POST':
        categorie = formCategorie(request.POST, request.FILES)
        if categorie.is_valid():
            noms = categorie.cleaned_data['nom']
            descriptions = categorie.cleaned_data['description']
            image = categorie.cleaned_data['image']
            
            oCat1 = Categorie(nom=noms, description=descriptions, image=image)
            oCat1.save()
            return redirect("listeCateg")
    else:
        categorie = formCategorie()
    return render(request, 'categorie/ajoutCategorie.html', {'categories': categorie})

def supprimerCategorie(request, id):
    if request.method == 'GET':
        # id = request.GET.get('id')
        categorie = get_object_or_404(Categorie, id=id)
        categorie.delete()
        return redirect("listeCateg")
    