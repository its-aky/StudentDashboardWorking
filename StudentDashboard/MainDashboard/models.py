from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
   class Meta:
        verbose_name_plural="UserDetails"

   student=models.ForeignKey(to=User,on_delete=models.CASCADE)  
   name=models.CharField(max_length=255)
   year=models.IntegerField()
   branch=models.CharField(max_length=255)
   type=models.CharField(max_length=255)
   mode=models.CharField(max_length=255)
   category=models.CharField(max_length=255)
   
   def __str__(self) -> str:
      return self.student.username
  
class Category(models.Model):
    class Meta:
        verbose_name_plural="Categories"
        
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
      return self.name
  
class Type(models.Model):
    class Meta:
        verbose_name_plural="Types"
        
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
      return self.name
  
class Mode(models.Model):
    class Meta:
        verbose_name_plural="Modes"
        
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
      return self.name
  

class UpcomingCompanyDetails(models.Model):
    class Meta:
        verbose_name_plural="UpcomingCompanyDetails"
  
    name_of_company=models.CharField(max_length=255)
    year_of_passing=models.IntegerField()
    preferred_branch=models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    mode=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name_of_company
  

    
