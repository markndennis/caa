from django.test import TestCase
from invigilator.models import Invigilator, Institution
from django.http import HttpResponse
from django.shortcuts import redirect
import os, random

# dictionary for institution names
instdict={"Camosun College":"Victoria","College of the Rockies":"Cranbrook", "Douglas College":"New Westminster","British Columbia Institute of Technology":"Burnaby","Justice Institute of British Columbia":"New Westminster","Langara College":"Vancouver","Nicola Valley Institute of Technology":"Merritt","Okanagan College":"Kelowna","UBC":"Vancouver","SFU":"Burnaby","UNBC":"Prince George","UVIC":"Victoria","Capilano University":"North Van","Emily Carr University of Art and Design":"Vancouver","Kwantlen Polytechnic University":"Surrey","Royal Roads University":"Victoria","Thompson Rivers University":"Kamloops","University of the Fraser Valley":"Chilliwack","Vancouver Island University":"Nanaimo"}

# populates database with instituion names from dictionary
def createinstitutions(request):
    Institution.objects.all().delete()
    
    insts=[]
    for inst in instdict.keys():
        ni = Institution()
        ni.name = inst
        insts.append(ni.name)
        ni.save()
   
    return redirect("admin/invigilator/institution/")
        
    
# create test invigilator names from CSV files and populate database
def createtestinvigs(request,num):
    Invigilator.objects.all().delete()
    fresults = getfileinput("static/files/fnames.csv")
    lresults = getfileinput("static/files/lnames.csv")
    institutions = Institution.objects.all()
    
    fnames = []
    lnames = []
    inames = []
    
   
    for x in range(0,int(num)):
        fname = random.choice(fresults)
        fnames.append(fname)
        lname = random.choice(lresults)
        lnames.append(lname)
        iname = random.choice(institutions)
        inames.append(iname)
        ni = Invigilator()
        ni.first_name = fname
        ni.last_name = lname
        ni.institution = iname
        ni.email = fname+"@"+lname+".com"
        cname = instdict.get(iname.name)
        ni.city = cname
        ni.province="British Columbia"
        ni.country="Canada"
        ni.save()
    
    return redirect("/admin/invigilator/invigilator/")
    

# reads CSV file used by above functions
def getfileinput(filename):
    fo = open(filename,"r")
    line = fo.readlines()
    fo.close()
    results=[]
    for eachline in line:
        foo = eachline.strip('\n')
        results.append(foo)
    return results
    
        
        
    