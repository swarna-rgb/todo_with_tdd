from django.db import models

# Create your models here.
class User(models.Model):
    pass
class TodoItem(models.Model):
    text = models.TextField(default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
