from django.contrib import admin
from invigilator.models import Invigilator, Institution

# Register your models here.

class InvigilatorAdmin(admin.ModelAdmin):
    fields = [ 'first_name','last_name', 'email', 'institution','city','province','country','details']
    list_display = ('last_name', 'first_name','institution','city','province','country')
    
class InstitutionAdmin(admin.ModelAdmin):
    fields = [ 'name']
    list_display = ('name',)
    
admin.site.register(Invigilator, InvigilatorAdmin)
admin.site.register(Institution, InstitutionAdmin)


