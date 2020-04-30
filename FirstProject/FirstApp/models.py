from django.db import models

from django.db import models

# Create your models here.


class Candidate(models.Model):
    CandidateID = models.CharField(max_length=30)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email_Id = models.CharField(max_length=30)

class Student(models.Model):
    StudentID = models.CharField(max_length=30)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Contact = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)

