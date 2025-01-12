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

