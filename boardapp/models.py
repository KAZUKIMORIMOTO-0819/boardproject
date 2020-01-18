from django.db import models

# Create your models here.

# データベーステーブル
class BoardModel(models.Model):
    title = models.CharField(max_length = 100)    # タイトル
    content = models.TextField()                  # 内容
    author = models.CharField(max_length = 100)   # 投稿者
    images = models.ImageField(upload_to="")      # 画像用
    good = models.IntegerField(null=True, blank=True, default=0)    # いいねの数
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length = 200,null=True, blank=True, default="a") 
