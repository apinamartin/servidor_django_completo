from django.db import models

class Ability(models.Model):
    aName = models.CharField(max_length=30)
    description = models.CharField(max_length=100)