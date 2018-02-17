from django.db import models

# Create your models here.
class Topping(models.Model):
    topping_name = models.CharField(max_length=200)
    topping_category = models.CharField(max_length=200)
    topping_price = models.DecimalField(max_digits=8,decimal_places=2)
    topping_upvotes = models.IntegerField(default=0)
    topping_downvotes = models.IntegerField(default=0)
    def __str__(self):
        return self.topping_name
        # this is more "informative"
        # return str(self.__dict__)

