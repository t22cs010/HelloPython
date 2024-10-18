from django.db import models #表をつくるための道具を持ってくる
from django.utils import timezone #時間を扱うための道具を持ってくる

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title