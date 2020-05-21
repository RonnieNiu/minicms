from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.models import Column, Article
#$ Create your views here.

def index(request):
    #columns = Column.objects.all()
    #return render(request,'index.html',{'columns':columns})
    
    
    nav_display = Column.objects.filter(nav_display=True)
    home_display = Column.objects.filter(home_display=True)
    
    return render(request,'index.html',{'nav_display':nav_display,
            'home_display':home_display})

def column_detail(request,column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request,'news/column.html',{'column':column})
    

def article_detail(request,pk,article_slug):
    #article = Article.objects.filter(slug=article_slug)[0]
    article = Article.objects.get(pk=pk)
    if article.slug != article_slug:
        return redirect(article)

    return render(request,'news/article.html',{'article':article})
