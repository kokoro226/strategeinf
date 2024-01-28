from django.db import models

from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリー',
        max_length=20)
    
    def __str__(self):
        return self.title
class PhotoPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリー',
        on_delete=models.PROTECT
        )
    
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    
    comment = models.TextField(
        verbose_name='コメント',
        )
    
    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to = 'photos'
        )
    image2 = models.ImageField(
        verbose_name='イメージ２',
        upload_to = 'photos',
        blank=True,
        null=True
        )
    image3 = models.ImageField(
        verbose_name='イメージ3',
        upload_to = 'photos',
        blank=True,
        null=True
        )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    
    def __str__(self):
        return self.title
    
class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')