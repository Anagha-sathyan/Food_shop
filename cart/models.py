from django.db import models
from shop.models import *
# Create your models here.
class cart_list(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class items(models.Model):
    prod=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cart_list,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.prod
    def total(self):
        return self.prod.price*self.quantity