from django.db import models

class Usuario(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]

    nome = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)