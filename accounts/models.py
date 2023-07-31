from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profil')
    image = models.ImageField(upload_to='accounts')

    def __str__(self):
        return str(self.user)
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)    
       

    

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