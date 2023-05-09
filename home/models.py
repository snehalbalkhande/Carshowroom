from django.db import models

# Create your models here.

class Car(models.Model):
        car_id=models.AutoField
        car_name=models.CharField(max_length=50)
        car_type=models.CharField(max_length=20)
        engine=models.CharField(max_length=20)
        mileage=models.CharField(max_length=20)
        fuel_type=models.CharField(max_length=20)
        price=models.FloatField(max_length=50)
        image=models.ImageField(upload_to='home/images', default="")

        
        def __str__(self):
          return self.car_name
        
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name        