from django.db import models

# Create your models here.
class Offer(models.Model):
    title = models.CharField(max_length = 50,verbose_name='عنوان العرض')
    text = models.TextField(max_length=400,verbose_name='نص العرض')


class Project(models.Model):
    name = models.CharField(max_length = 50,null=True,verbose_name='اسم الصورة')
    image = models.ImageField(upload_to='images',verbose_name='الصورة')

class About(models.Model):
    text = models.TextField(verbose_name='النص')
    phone = models.CharField(max_length=10,verbose_name='رقم الجوال' )
    logo = models.ImageField(upload_to='images',verbose_name='الشعار')
    address = models.CharField(max_length=200,verbose_name='العنوان')
    url = models.CharField(max_length = 100,verbose_name='رابط الموقع')
    



