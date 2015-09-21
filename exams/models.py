from django.db import models


# Create your models here.

class ExamType(models.Model):
    exam_type= models.CharField(max_length=20)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.exam_type


class Exam(models.Model):
    exam_type = models.ForeignKey(ExamType)
    sub_test = models.CharField(max_length=2)
    exam_ques = models.CharField(max_length=200)
    

class Questions(models.Model):
    qnum = models.IntegerField()
    examtype = models.CharField(max_length=2)
    qtext = models.CharField(max_length=1024)
    r1 = models.CharField(max_length=256)
    r2 = models.CharField(max_length=256)
    r3 = models.CharField(max_length=256)
    r4 = models.CharField(max_length=256)
    qtext_c = models.CharField(max_length=1024)
    r1_c = models.CharField(max_length=256)
    r2_c = models.CharField(max_length=256)
    r3_c = models.CharField(max_length=256)
    r4_c = models.CharField(max_length=256)
    difficulty = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    solution =  models.CharField(max_length=2)
    
