from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    title=models.CharField(_('title'),max_length=20)
    text=models.TextField(_('description'),blank=True)
    avatar=models.ImageField(blank=True,upload_to='categories/')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    
    



class Product(models.Model):
    title=models.CharField(_('title'),max_length=20)
    text=models.TextField(_('description'),blank=True)
    avatar=models.ImageField(blank=True,upload_to='products/')
    categories=models.ManyToManyField('Category',blank=True)
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)


class Productfile(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    title=models.CharField(_('title'),max_length=20)
    avatar=models.ImageField(blank=True,upload_to='categories/')
    file=models.FileField(upload_to='files/%Y/%m/%d/')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

