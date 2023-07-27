from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profil')
    image = models.ImageField(upload_to='accounts')

    def __str__(self):
        return str(self.user)
       

    

PHONE_TYPES = (
    ('Primary','Primary'),
    ('Secondary','Secondary')
)
class Phones(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_phone')
    type = models.CharField(max_length=20,choices=PHONE_TYPES)
    number = models.CharField(max_length=20)


      
ADDRESS_TYPES = (
    ('Home','Home'),
    ('Office','Office'),
    ('Academy','Academy'),
    ('Bussiness','Bussiness'),
    ('Others','Others'),
)
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_address')
    type = models.CharField(max_length=20,choices=ADDRESS_TYPES)
    address = models.TextField(max_length=200)      