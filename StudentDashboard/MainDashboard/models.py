from django.db import models
from django.contrib.auth.models import User
from UserPreferences.models import UserPreference


class Curriculum(models.Model):
    
    user_preference = models.ForeignKey(UserPreference, on_delete=models.CASCADE)
    subject_one=models.CharField(max_length=255)
    subject_two=models.CharField(max_length=255)
    subject_three=models.CharField(max_length=255)
    subject_four=models.CharField(max_length=255)
    subject_five=models.CharField(max_length=255)
    subject_six=models.CharField(max_length=255)
   
    class Meta:
        verbose_name_plural="Curriculums"
        unique_together = (
                'user_preference',
                'subject_one',
                'subject_two',
                'subject_three',
                'subject_four',
                'subject_five',
                'subject_six'
            )
           
    def __str__(self) -> str:
        return f'{self.user_branch_sem}'
    
class UserMarks(models.Model):
   
    user_branch_sem = models.ForeignKey(UserPreference, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=255)
    quiz1 = models.IntegerField()
    quiz2 = models.IntegerField()
    mid_semester = models.IntegerField()
    end_semester = models.IntegerField()
    
    class Meta:
        verbose_name_plural="UserMarks"
        unique_together = (
                'user_branch_sem',
                'subject_name'
            )
        
    def __str__(self) -> str:
        return f'{self.user_branch_sem}'
    
  

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
  

    
