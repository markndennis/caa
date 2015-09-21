from django.contrib import admin
from exams.models import ExamType, Questions, Exam

#Register your models here.

class ExamTypeAdmin(admin.ModelAdmin):
    #fields = [ 'last_name','first_name', 'email']
    list_display = ('exam_type','pk')  
    
class QuestionsAdmin(admin.ModelAdmin):
    #fields = ['qnum','qtext']
    list_display = ('qnum','examtype','qtext','r1','r2','r3','r4','qtext_c','pk')
    
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_type','sub_test','exam_ques')
    
    
admin.site.register(ExamType,ExamTypeAdmin)
admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Exam,ExamAdmin)