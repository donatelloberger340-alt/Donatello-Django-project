from django.shortcuts import render, get_object_or_404
from .models import Article


def accueil(request):
    return render(request, 'articles/accueil.html')

def contact(request):
    return render(request, 'articles/contact.html')

def menu(request):
    return render(request, 'articles/menu.html')

def about(request):
    return render(request, 'articles/about.html')

def liste_articles(request):
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'articles/articles.html', {'articles': articles})

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/detail.html', {'article': article})
