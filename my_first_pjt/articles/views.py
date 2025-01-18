from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods


# index 만들기
def index(request):
    return render(request, "articles/index.html")

# 데이터 던지기
def data_throw(request):
    return render(request, "articles/data_throw.html")

# 데이터 받기
def data_catch(request):
    message = request.GET.get("message")
    context = {"message": message}
    return render(request, "articles/data_catch.html", context)

# articles의 목록
def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    content = {"articles": articles}
    return render(request, "articles/articles.html", content)

# 작성된 글 확인
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comments.all().order_by("-pk")
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
        }
    return render(request, "articles/article_detail.html", context)

@login_required
# 새로운 글 작성하기
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)   # 데이터 바인딩된 form, 두 번째 인자로 files을 받음
        if form.is_valid():
            article = form.save(commit=False)   # 데이터를 저장
            article.author = request.user
            article.save()
            return redirect('articles:article_detail', article.pk)   # article_detail로 리다이렉트
    else:                       # Method가 GET일 경우
        form = ArticleForm()
        
    context = {"form": form}
    return render(request, "articles/create.html", context)


@require_POST
# 글 삭제하기
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404
        article.delete()
        return redirect('articles:articles')
    
    return redirect('articles:article_detail', pk)


@login_required
@require_http_methods(["GET", "POST"])
# 글 수정하기
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)  # "instance=article" : article에 있는 내용을 채울 거임
        if form.is_valid():
            article = form.save()
            return redirect('articles:article_detail', article.pk)
        
    else:
        form = ArticleForm(instance=article)    # GET일 때도 내용이 비어있으면 안 되니, instance로 가져올 거임
        
    context = {
        "form":form,
        "article":article,
        }
    return render(request, "articles/update.html", context)

# 댓글 생성
@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect("articles:article_detail", article.pk)
