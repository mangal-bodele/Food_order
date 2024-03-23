from django.db import models

class FoodOrder(models.Model):
    ORDER = [('DOSA','dosa'),('IDLI','Idli'),('POHA','poha'),('TEA','tea')]
    person_name = models.CharField(max_length=20)
    order = models.TextField(choices=ORDER)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    time_of_order  = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField()
