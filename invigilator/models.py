from django.db import models

# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
  
class Invigilator(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length =40)
    email = models.EmailField()
    institution = models.ForeignKey(Institution)
    city = models.CharField(max_length=40)
    province = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=40)
    details = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.first_name + " " + self.last_name + " - " + str(self.institution)
        
#staff_member = models.ForeignKey(User, limit_choices_to={'is_staff': True})