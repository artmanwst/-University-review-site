from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
class Post(models.Model):
    text=models.TextField()
    pub_date=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='posts')
class Uni(models.Model):
    Name=models.CharField(max_length=200)
    description=models.TextField(max_length=800)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.text