from django.db import models

# Create your models here.

class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

