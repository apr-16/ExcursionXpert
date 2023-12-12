from django.db import models
from django.contrib.auth.models import User

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)

class user_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    
class district(models.Model):
    dis = models.CharField(max_length=50, null=True)
    
class packages(models.Model):
    dis = models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    packages_name = models.CharField(max_length=50, null=True)
    destination = models.CharField(max_length=50, null=True)
    date = models.DateField()
    cost = models.CharField(max_length=50, null=True)
    inclusions = models.CharField(max_length=50, null=True)
    attraction = models.CharField(max_length=50, null=True)
    climate = models.CharField(max_length=50, null=True)
    more_info = models.CharField(max_length=50, null=True)
    images1 = models.FileField(max_length=50, null=True)
    images2 = models.FileField(max_length=50, null=True)
    images3 = models.FileField(max_length=50, null=True)

class confirm(models.Model):
    pack = models.ForeignKey(packages, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE, null=True)
    persons = models.IntegerField(null=True)
    date = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    total = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=50, null=True)
    
class payment(models.Model):
    pack = models.ForeignKey(packages, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE, null=True)
    cardname=models.CharField(max_length=150)
    cardno=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    cardyear=models.CharField(max_length=150)
    status = models.CharField(max_length=50, null=True)

class guidedetails(models.Model):
    dis = models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    guide = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=50, null=True)
