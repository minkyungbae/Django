from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, "index.html")

def data_throw(request):
    return render(request, "data_throw.html")

def data_catch(request):
    message = request.GET.get("message")
    context = {"message": message}
    return render(request, "data_catch.html", context)


def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    content = {"articles": articles}
    return render(request, "articles.html", content)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "article_detail.html", context)

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    article = Article.objects.create(title=title, content=content)
    article.save()
    return redirect('article_detail', article.pk)

def new_article(request):
    return render(request, "new_article.html")

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect("articles")
    
    return redirect('article_detail', pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "edit.html", context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    article.save()
    return redirect("article_detail", article.pk)

