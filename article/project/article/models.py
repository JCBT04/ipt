from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Article (models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     author = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
          return self.title
     
class Comment (models.Model):
     article = models.ForeignKey(Article, on_delete=models.CASCADE)
     comment = models.TextField()
     date = models.DateField(auto_now_add=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
        return f'Comment by {self.user.username} on {self.article.title}'