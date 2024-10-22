from django.db import models
from brand.models import Brand
from car.models import Car
from django.contrib.auth.models import User
class OrderCarUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    BuyDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Name: {self.user.first_name} ,Car: {self.car.name}'