from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    category_cd = models.CharField(max_length=20, unique=True)
    category_nm = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.category_nm


class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, null=True)
    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
