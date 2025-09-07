from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    body = models.TextField(verbose_name="Matn")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Yaratilgan vaqti")

    STATUS_CHOICES = [
        ('draft', 'Qoralama'),
        ('published','Nashr etilgan'),
        ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Holat")
 
    image = models.ImageField(
        upload_to='posts/%Y/%m/$d/', 
        blank=True,
        null=True,
        verbose_name='Rasm')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    def __str__(self):
        return self.title
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.email}"
