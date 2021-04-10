from django.db import models

# models
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    dt_nascimento = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=32)
