from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(models.Model):
    name =models.CharField(_('name'),max_length=120)
    price = models.FloatField(_('price'))
    quantity = models.IntegerField(_('quantity'))
    description = models.TextField(_('description'),max_length=30000)
    subtitle = models.TextField(_('subtitle'), max_length=500)
    sku = models.IntegerField(_('sky'))
    brand =models.ForeignKey('Brand',verbose_name=_('brand'),related_name='product_brand', on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    image = models.ImageField(_('image'),upload_to='products')
  
    def __str__(self):
        return self.name


class ProductImages(models.Model):
     product = models.ForeignKey(Product,verbose_name=('product'),related_name='product_image',on_delete=models.CASCADE)
     image = models.ImageField(_('image'),upload_to='productimages')
    
     def __str__(self):
        return str(self.product)
       


class Brand(models.Model):
    name =models.CharField(_('name'),max_length=120)
    image =models.ImageField(_('image'),upload_to='brands')


    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=('user'),related_name='review_author',on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,verbose_name=('product'),related_name='product_review',on_delete=models.CASCADE)
    review =models.TextField(_('review'),max_length=500)
    rate =models.BigIntegerField(_('rate'))
    create_date =models.DateTimeField(_('creat_date'),default=timezone.now)

    def __str__(self):
        return str(self.Product)