from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from pymysql import NULL

# Create your models here.
class Explore(models.Model):
    image_ex = models.ImageField()
    country = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.country

class City(models.Model):
    image_pl = models.ImageField()
    country = models.CharField(max_length=20, default="india")
    city = models.CharField(max_length=20)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),   
        ]
    )
    def __str__(self):
        return self.city
    