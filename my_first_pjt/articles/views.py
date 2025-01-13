from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def hello(request):
    name = "MinKyung"
    tags = ["Python", "Django", "GitHub", "html"]
    personality = ["Down to earth", "Considerate", "Empahty", "Diligent"]
    context = {
        "name": name,
        "tags": tags,
        "personality": personality
    }
    return render(request, "hello.html",context)

def data_throw(request):
    return render(request, "data_throw.html")

def data_catch(request):
    return render(request, "data_catch.html")

    
