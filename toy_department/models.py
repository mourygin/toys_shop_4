from django.db import models

# Create your models here.
class Toy(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    weight = models.DecimalField(decimal_places=2, max_digits=2)
    description = models.CharField(max_length=1024, null=True, blank=True)
    age_limited = models.BooleanField(default=False)
    in_stock = models.IntegerField()

    def __str__(self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=11)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy, related_name='toys')

    def __str__(self):
        return self.name