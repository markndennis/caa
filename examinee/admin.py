from django.contrib import admin
from examinee.models import Examinee, ExamInstance, ExamResults
#from exams.models import ExamType

# Register your models here.

class ExamineeAdmin(admin.ModelAdmin):
    #fields = [ 'last_name','first_name', 'email']
    list_display = ('pk','first_name','last_name','regnum','invigilator','exam_type')
    
# class ExamInstanceAdmin(admin.ModelAdmin):
#     list_display = ('pk','examinee')
    
class ExamResultsAdmin(admin.ModelAdmin):
    #list_filter = ('examinee')
    #fields = ['examinee','ques_number','ques_response']
    search_fields = ['examinee']
    list_display = ('examinee','ques_number','ques_response')
    
    
# class ExamTypeAdmin(admin.ModelAdmin):
#     #fields = [ 'last_name','first_name', 'email']
#     list_display = ('exam_type','pk')    
    
admin.site.register(Examinee,ExamineeAdmin)
admin.site.register(ExamInstance)
admin.site.register(ExamResults, ExamResultsAdmin)



