from django import forms

class QuesDisplayForm(forms.Form):
    qtext = forms.CharField(label='qtext',max_length=40)
    rq = forms.CharField(label='Last Name', max_length=40)
    password = forms.CharField(label='Password', max_length=40)
    
    
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
    