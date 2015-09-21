from django.test import TestCase
from examinee.models import Examinee
from exams.models import ExamType
from invigilator.models import Invigilator, Institution
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
import os, random


# create test examinee names
def createtestexaminees(request,num):
    Examinee.objects.all().delete()
    fresults = getfileinput("static/files/fnames.csv")
    lresults = getfileinput("static/files/lnames.csv")
    invigs = Invigilator.objects.all()
    examtypes = ExamType.objects.all()
   
    fnames = []
    lnames = []
    inames = []
    
   
    for x in range(0,int(num)):
        fname = random.choice(fresults)
        fnames.append(fname)
        lname = random.choice(lresults)
        lnames.append(lname)
        iname = random.choice(invigs)
        inames.append(iname)
        # etype = random.choice(examtypes)
        etype = examtypes.get(exam_type="Acupuncturist")
        ne = Examinee()
        ne.first_name = fname
        ne.last_name = lname
        #zfill adds leading zeros where necessary
        ne.regnum = str(x+1).zfill(4)
        ne.invigilator = iname
        ne.exam_type = etype
        ne.email = fname+"@"+lname+".com"
        ne.dob = getrandomdob()
        ne.intended = getrandomintended()
        ne.save()
    
    return redirect("/admin/examinee/examinee/")
    
def createtestusers(request,num):
    #Examinee.objects.all().delete()
    User.objects.filter(is_staff__exact=0).delete()
    fresults = getfileinput("static/files/fnames.csv")
    lresults = getfileinput("static/files/lnames.csv")
    invigs = Invigilator.objects.all()
    examtypes = ExamType.objects.all()
   
    fnames = []
    lnames = []
    inames = []
    
   
    for x in range(0,int(num)):
        fname = random.choice(fresults)
        fnames.append(fname)
        lname = random.choice(lresults)
        lnames.append(lname)
        iname = random.choice(invigs)
       # inames.append(iname)
        # etype = random.choice(examtypes)
        #etype = examtypes.get(exam_type="Acupuncturist")
         # zfill adds leading zeros
        password = str(x+1).zfill(4)
        username = fname+lname+password
        email = fname+"@"+lname+".com"
        # create_user requires username, email and password be passed to create a valid user
        # user does not automatically get staff rights and therefore can't see any admin tables
        nu = User.objects.create_user(username,email,password)
        nu.first_name = fname
        nu.last_name = lname
        nu.save()
        
    return redirect("/admin/auth/user/")
    
    
    
def getfileinput(filename):
    fo = open(filename,"r")
    line = fo.readlines()
    fo.close()
    results=[]
    for eachline in line:
        foo = eachline.strip('\n')
        results.append(foo)
    return results
    
def getrandomdob():
    age = random.randint(21,65)
    bday = random.randint(0,364)
    delta = age*365+bday
    now =  datetime.now()
    date = now - timedelta(days=delta)
    return date
    

def getrandomintended():
    # random integer between 45 and 182
    intenddays = random.randint(45,182)
    now = datetime.now()
    # add random integer reprsenting days to todays integer value
    date = now + timedelta(intenddays)
    return date
