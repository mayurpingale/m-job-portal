from typing import Optional
from django.db import models

# Create your models here.
class JobRegister(models.Model):
    JobRegisterId =models.AutoField(primary_key=True)
    Company_Name=models.CharField(max_length=100)
    Job_Description=models.TextField()
    CompanyLogo = models.ImageField(upload_to='pics')
    Company_EmailId=models.EmailField(max_length=100)
    
class Registration(models.Model):
    Candidate_Firstname=models.CharField(max_length=100)
    Candidates_lastname=models.CharField(max_length=100)
    Candidates_EmailId=models.EmailField(max_length=254)
    


