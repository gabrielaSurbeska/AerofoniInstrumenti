from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Prodavac(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Email = models.EmailField()
    Transaction_account = models.IntegerField()
    Password = models.CharField(max_length=200)
    Confirm_password = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Name + " " + self.Surname


class Kupuvac(models.Model):
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Mobile_Number = models.IntegerField()
    Card = models.IntegerField()
    CVV = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Name + " " + self.Surname

class Slobodni_Aerofoni(models.Model):
    Brand= models.CharField(max_length=200)
    Model = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Reeds = models.CharField(max_length=200)
    Bass = models.CharField(max_length=200)
    Weight = models.CharField(max_length=200)
    Features = models.CharField(max_length=200)
    Includes = models.CharField(max_length=200)
    Suggested_Upgrades = models.CharField(max_length=200)
    Price = models.IntegerField()
    Video = models.CharField(max_length=2000)
    Photos = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Brand + " " + self.Model

class Duvacki_Instrumenti(models.Model):
    Name = models.CharField(max_length=200)
    Trumpets_Type = models.CharField(max_length=200)
    Trumpets_Bore_Size = models.CharField(max_length=200)
    Trumpets_Bell = models.CharField(max_length=200)
    Trumpets_Valve = models.CharField(max_length=200, null=True, blank=True)
    Trumpets_Leadpipe = models.CharField(max_length=200, null=True, blank=True)
    Trumpets_Finish = models.CharField(max_length=200, null=True, blank=True)
    Trumpets_Options = models.CharField(max_length=200,null=True, blank=True)
    Video = models.CharField(max_length=2000,null=True, blank=True)
    Photos = models.ImageField(null=True, blank=True)
    Price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Name + " " + self.Trumpets_Type


class Register(models.Model):
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=50)
    Email = models.EmailField()
    Transaction_account = models.IntegerField()
    Password = models.CharField(max_length=50)
    Confirm_password = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Name + " " + self.Surname