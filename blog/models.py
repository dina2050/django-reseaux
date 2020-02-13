
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from taggit.managers import TaggableManager
from django.contrib.gis.geos import Point
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profil")
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    interest = TaggableManager()
    follows = models.ManyToManyField('Profil',blank=True, related_name='followed_by')
    address = models.CharField(max_length=50,null=True)
    zipcode = models.CharField(max_length=50,null=True)
    geom = models.PointField(null=True, blank=True)


    def __unicode__(self):
        return self.user.username


