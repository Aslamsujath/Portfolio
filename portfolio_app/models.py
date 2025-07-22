from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(max_length=50,null=True,blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
    remarks=models.TextField(null=True,blank=True)
    services = models.CharField(max_length=50,null=True, blank=True)
    created_at = models.DateField(null=True, blank=True)