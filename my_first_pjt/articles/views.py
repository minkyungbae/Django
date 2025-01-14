from django.shortcuts import render
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

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    article = Article(title=title, content=content)
    article.save()
    
    return render(request, "create.html")

def new_article(request):
    return render(request, "new_article.html")
