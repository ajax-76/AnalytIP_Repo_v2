from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class TechCategories(models.Model):
    Info=models.CharField(max_length=100)
    TimeStamp=models.DateTimeField()

class StartUpInfo(models.Model):
    Name=models.CharField(max_length=100)
    TeamMemebersNumber=models.CharField(max_length=100)
    About=models.TextField()
    HeadQuarters=models.CharField(max_length=100)
    ProductVideo=models.CharField(max_length=100)
    WebsiteLink=models.CharField(max_length=100)
    Founders=models.CharField(max_length=100)
    FundingInfo=models.TextField()
    Team=models.CharField(max_length=50)
    ProductFeature=models.CharField(max_length=100)
    DateTime=models.DateTimeField()
    TechSpecId=models.ForeignKey(TechCategories,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
    
class Activites(models.Model):
    StartUpId=models.ForeignKey(StartUpInfo,on_delete=models.CASCADE)
    Info=models.TextField()
    TimeStamp=models.DateTimeField()