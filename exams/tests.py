from django.test import TestCase
from exams.models import ExamType, Questions, Exam
from django.shortcuts import redirect
from django.http import HttpResponse
import os, random

# Create your tests here.
examtypes=["Acupuncturist","Herbalist","Reciprocity","Doctor of TCM"]

def createexamtype(request):
    ExamType.objects.all().delete()
    
    for mytype in examtypes:
        nt = ExamType()
        nt.exam_type = mytype
        nt.save()
        
    return redirect("/admin/exams/examtype/")
    
    
def createques(request):
    Questions.objects.all().delete()
    questions = getfileinput("static/files/questions.csv") 
    for lines in questions:
        fields = lines.split("|")
        nq = Questions()
        nq.qnum = int(fields[0])
        nq.examtype = fields[1]
        nq.qtext = fields[3]
        nq.r1 = fields[4]
        nq.r2 = fields[5]
        nq.r3 = fields[6]
        nq.r4 = fields[7]
        nq.qtext_c = fields[8]
        nq.r1_c = fields[9]
        nq.r2_c = fields[10]
        nq.r3_c = fields[11]
        nq.r4_c = fields[12]
        nq.difficulty = fields[13]
        nq.active = fields[14]
        nq.create_date = fields[15]
        nq.solution = fields[16]
        nq.save()
        
    #return HttpResponse("hello,<br/>%s" % z)
    return redirect("/admin/exams/questions/")

def createexams(request):
    Exam.objects.all().delete()
    exams=ExamType.objects.all()
    subtests = ["A","B","C","D"]
   
    for et in exams:
        for st in subtests:
            qnums = ""
            for x in range(0,10):
                qnum = random.randint(1,160)
                qnums = qnums + str(qnum) + ","
            
            qnums = qnums[:-1]
            ne = Exam()
            ne.exam_type = et
            ne.sub_test = st
            ne.exam_ques = qnums
            ne.save()
             
    return redirect("/admin/exams/exam/")

    
def getfileinput(filename):
    fo = open(filename, 'r')
    line = fo.readlines()
    fo.close()
    results=[]
    for eachline in line:
        foo = eachline.strip('\n')
        results.append(foo)
    return results