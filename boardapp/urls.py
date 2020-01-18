from django.urls import path, include
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, BoardCreate

urlpatterns = [
    path("signup/", signupfunc, name="signup"),    # signup画面への繋ぎこみ
    path("login/", loginfunc, name="login"),    # login画面への繋ぎこみ
    path("list/", listfunc, name="list"),    # list画面への繋ぎこみ
    path("logout/", logoutfunc, name="logout"),    # logoutへの繋ぎこみ
    path("detail/<int:pk>", detailfunc, name="detail"),    # detailへの繋ぎこみ
    path("good/<int:pk>", goodfunc, name="good"),
    path("read/<int:pk>", readfunc, name="read"),
    path("create/", BoardCreate.as_view(), name="create"),
]
