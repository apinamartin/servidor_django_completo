from django.db import models

class Pokemon(models.Model):
    dexNumber = models.IntegerField()
    name = models.CharField(max_length=15)
    ability = models.CharField(max_length=30)
