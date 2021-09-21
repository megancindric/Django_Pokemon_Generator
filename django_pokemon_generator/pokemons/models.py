from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.Charfield(max_length = 20)
    primary_type = models.Charfield(max_length = 20)
    secondary_type = models.Charfield(max_length = 20)
    region = models.Charfield(max_length = 20)
    description = models.TextField(max_length = 200)
    #TODO link attacks using attack_name, then can query DB to get stats when called
    primary_attack = models.CharField(max_length = 20)
    seconday_attack = models.CharField(max_length = 20)

def __str__(self):
    return self.name