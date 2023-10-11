from django.db import models

# Create your models here.
class QUESTION(models.Model):
    name=models.CharField(blank=False,max_length=50)
    q1=models.CharField(blank=False,max_length=900)
    q2=models.CharField(blank=False,max_length=900)
    q3=models.CharField(blank=False,max_length=900)
    q4=models.CharField(blank=False,max_length=900)
    
    q6=models.CharField(blank=False,max_length=900)
    q7=models.CharField(blank=False,max_length=900)
    q8=models.CharField(blank=False,max_length=900)
    q9=models.CharField(blank=False,max_length=900)
    content=models.IntegerField(blank=False,default=9)
    tech=models.IntegerField(blank=False,default=9)
    design=models.IntegerField(blank=False,default=9)
    cultural=models.IntegerField(blank=False,default=9)
    creativity=models.IntegerField(blank=False,default=9)
    hospitality=models.IntegerField(blank=False,default=9)
    logistics=models.IntegerField(blank=False,default=9)


   