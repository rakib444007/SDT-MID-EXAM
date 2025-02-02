from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=244)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
