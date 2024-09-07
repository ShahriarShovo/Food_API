from django.db import models
from order.models.item import Item

class Modifier(models.Model):
    name = models.CharField(max_length=255)
    item = models.ForeignKey(Item, related_name='modifiers', on_delete=models.CASCADE)
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name