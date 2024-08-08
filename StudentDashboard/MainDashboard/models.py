from django.db import models
from django.contrib.auth.models import User


class Curriculum(models.Model):
    class Meta:
        verbose_name_plural="Curriculums"
    
    branch=models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    subject_one=models.CharField(max_length=255)
    subject_two=models.CharField(max_length=255)
    subject_three=models.CharField(max_length=255)
    subject_four=models.CharField(max_length=255)
    subject_five=models.CharField(max_length=255)
    subject_six=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.branch} {self.semester}'
    
  

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
  

    
