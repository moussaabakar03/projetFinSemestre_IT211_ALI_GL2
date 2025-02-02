from django.shortcuts import render

# Create your views here.

def reponseHtml(request):
    return render(request, 'acceuil.html')

def reponseHtml2(request):
    return render(request, 'acceuil3.html')