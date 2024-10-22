from django.db import models
from brand.models import Brand
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=230)
    description = models.TextField()
    image = models.ImageField(upload_to='car/upload',blank=True,null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE , related_name='cars')

    def __str__(self) -> str:
        return f'Name: {self.name} Brand: {self.brand}'
    

class Comment(models.Model):
    post = models.ForeignKey(Car,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments by {self.name}'