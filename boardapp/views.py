from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

### signup用メソッド
def signupfunc(request):
    if request.method == "POST":
        username2 = request.POST["username"]
        password2 = request.POST["password"]
        try:
            User.objects.get(username=username2)      # 既存のusernameが既にある場合
            return render(request, "signup.html", {"error":"このユーザは登録されています"})
        except:
            user = User.objects.create_user(username2, '', password2)        
            return render(request, "login.html", {"some":100})

    return render(request, "signup.html", {"some":100})

### login用メソッド
def loginfunc(request):
    if request.method == "POST":
        username2 = request.POST["username"]
        password2 = request.POST["password"]
        user = authenticate(request, username=username2, password=password2)
        if user is not None:       # ログインできる場合
            login(request, user)
            return redirect("list")
        else:                      # ログインできない場合
            return redirect("signup")
    return render(request, "login.html")

### list用メソッド
@login_required      # ログイン状態を判定する
def listfunc(request):
    object_list = BoardModel.objects.all()       # BoardModelのデータを読み込み
    return render(request, "list.html", {"object_list":object_list})

def logoutfunc(request):
    logout(request)
    return redirect("login")

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, "detail.html", {"object":object})

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect("list")

def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()     # ユーザの名前の取得
    if post2 in post.readtext:
        return redirect("list")
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect("list")

### CrateView
class BoardCreate(CreateView):
    template_name = "create.html"
    model = BoardModel
    fields = ("title", "content", "author", "images")
    success_url = reverse_lazy("list")
