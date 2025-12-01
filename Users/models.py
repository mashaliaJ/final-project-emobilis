from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)

    image = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField()

    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)

    bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.name
