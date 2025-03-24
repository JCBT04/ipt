from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class Todo (models.Model):
     status_choices = [
          ('done', 'Done'),
          ('pending', 'Pending'),
          ('edit', 'Edit')
     ]

     user_id = models.ForeignKey(user, on_delete=models.PROTECT)
     title = models.CharField(max_length=100)
     description = models.TextField()
     status = models.CharField(max_length=10, choices=status_choices)
     create_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateField(auto_now=True)

     def __str__(self):
          return self.title