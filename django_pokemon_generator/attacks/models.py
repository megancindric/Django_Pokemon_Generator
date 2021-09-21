from django.db import models

# Create your models here.
class Attacks(models.Model):
    attack_name = models.Charfield(max_length = 20)
    attack_power = models.IntegerField(max_length = 3)
    attack_type = models.CharField(max_length = 20)
    attack_description = models.TextField(max_length = 200)
    status_condition = models.TextField(max_length = 10)
    status_condition_chance = models.DecimalField(max = 1)


def __str__(self):
    return self.attack_name
