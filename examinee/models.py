from django.db import models

class Examinee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length =40)
    regnum = models.CharField(max_length=20)
    email = models.EmailField()
    exam_type = models.ForeignKey('exams.ExamType')
    invigilator = models.ForeignKey('invigilator.Invigilator')
    dob = models.DateField(blank=True)
    intended = models.DateField(blank=True)
    approved = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):              # __unicode__ on Python 2
         self.name = self.last_name + ", " + self.first_name + " - " + str(self.exam_type)
         return self.name


class ExamInstance(models.Model):
    examinee = models.CharField(max_length=10)
    start_time=models.DateTimeField(blank=True,null=True)
    elapsed_time=models.DateTimeField(blank=True,null=True)
    end_time=models.DateTimeField(blank=True,null=True)
    ques_sequence=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.examinee
        
    
class ExamResults(models.Model):
    examinee =  models.CharField(max_length=10)
    ques_number = models.IntegerField()
    ques_response = models.CharField(max_length=2,null=True)
    
    def __unicode__(self):
        return self.examinee
    
    
    