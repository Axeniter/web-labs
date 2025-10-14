from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Программирование'),
        ('math', 'Математика'),
        ('graphic', 'Компьютерная графика'),
        ('sports', 'Спорт'),
        ('other', 'Другое'),
    ]

    id = models.BigAutoField()(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_date']
    
class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ["-created_at"]