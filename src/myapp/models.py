from django.db import models
from django.utils import timezone
from django.forms import TextInput, Textarea
from django.db import models



# Create your models here.
class URL(models.Model):
 myurl = models.URLField()
 price = models.IntegerField(null=True,blank=True)
 revenue = models.IntegerField(null=True,blank=True)
 d_a = models.IntegerField(null=True,blank=True)
 p_a = models.IntegerField(null=True,blank=True)
 timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
 updated = models.DateTimeField(auto_now_add=False, auto_now=True)

 def __str__(self):
  return self.myurl


class API(models.Model):
 apiurl = models.URLField()
 nofollow = models.NullBooleanField()
 mainurl = models.URLField(default ='')
 da = models.IntegerField(null=True,blank=True)
 pa = models.IntegerField(null=True,blank=True)

 timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
 updated = models.DateTimeField(auto_now_add=False, auto_now=True)


 def __str__(self):
  return self.apiurl