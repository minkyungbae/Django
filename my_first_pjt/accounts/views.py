from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import update_session_auth_hash

# 로그인
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            auth_login(request, form.get_user())   # 로그인 하기
            next_url = request.GET.get("next") or "index"
            return redirect(next_url)
    
    else:    
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

# 로그아웃
@require_POST
def logout(request):
    auth_logout(request)    # 로그아웃 하기
    return redirect('index')


# 회원가입
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)   # 바인딩 form
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 로그인 하기
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "accounts/signup.html", context)

# 회원탈퇴
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("index")

# 회원 정보 수정
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        # request가 POST인 것들 중에서만 선택.
        # form을 change할 내용을 instance를 통해 user로 채우겠다.
        form = CustomUserChangeForm(request.POST, instance=request.user) 
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)

# 비밀번호 수정
@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)

