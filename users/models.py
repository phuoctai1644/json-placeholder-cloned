from django.db import models

class Geo(models.Model):
  lat = models.DecimalField(max_digits=9, decimal_places=6)
  lng = models.DecimalField(max_digits=9, decimal_places=6)

class Address(models.Model):
  street = models.CharField(max_length=255)
  suite = models.CharField(max_length=20)
  city = models.CharField(max_length=255)
  zipcode = models.CharField(max_length=20)
  geo = models.OneToOneField(Geo, on_delete=models.CASCADE)

class Company(models.Model):
  name = models.CharField(max_length=255)
  catchPhrase = models.CharField(max_length=255)
  bs = models.CharField(max_length=255)

class User(models.Model):
  name = models.CharField(max_length=255)
  username = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  address = models.OneToOneField(Address, on_delete=models.CASCADE)
  phone = models.CharField(max_length=255)
  website = models.CharField(max_length=255)
  company = models.OneToOneField(Company, on_delete=models.CASCADE)
