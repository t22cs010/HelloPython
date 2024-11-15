from django.db import models

# Create your models here.
class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', '月'),
        ('Tuesday', '火'),
        ('Wednesday', '水'),
        ('Thursday', '木'),
        ('Friday', '金'),
        ('Saturday', '土'),
        ('Sunday', '日'),
    ]

    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    activity = models.CharField(max_length=100)

    def __str__(self):
        
        
        return f"{self.day}: {self.activity}"