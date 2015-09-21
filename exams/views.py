# exams.views

from django.shortcuts import render, get_object_or_404, redirect
from exams.models import Questions
from examinee.models import ExamInstance, ExamResults
from examinee.views import checkexaminstance
import datetime
#from django.template.response import TemplateResponse

from django.http import HttpResponse

def intro(request):
     print request.user
     context = {
     'username' : request.user.first_name + " " + request.user.last_name,
     }
     return render(request, 'exams/intro.html', context)
     
def startexam(request):
    username = request.user.username
    checkexaminstance(username)
    examinstance = ExamInstance.objects.get(examinee=username)  # get exam instance from database
    examinstance.start_time = datetime.datetime.now()
    examinstance.save()
    qlist = examinstance.ques_sequence.split(',')  # convert ques_sequence to a python list
    request.session['username'] = request.user.first_name + " " + request.user.last_name
    request.session['numques'] = len(qlist)
    print "length"
    print len(qlist)
    request.session['qlist']  = qlist  # add python question list to session
    request.session['curr_ques'] = 0
    return displayques(request)
    
    

def displayques(request):
    num = int(request.session['curr_ques'])
    print "from displayques"
    print num
    thisques =request.session['qlist'][num]
    thisques = int(thisques)
    print thisques
    ques = get_object_or_404(Questions,qnum=thisques)
    print ques.qtext
    context = {
        'username' : request.session['username'],
        'num': num + 1,
        'ques' : ques
        }
    return render(request,'exams/examques.html',context)
   
def postanswer(request):
    answer = request.POST.get("response")
    clicked = request.POST.get("submit")
    username = request.user.username
    num = int(request.session['curr_ques'])
    thisques =int(request.session['qlist'][num])
    result = ExamResults.objects.get(examinee=username,ques_number=thisques)
    #myvar = result.ques_number
    result.ques_response = answer
    result.save()
    examinstance = ExamInstance.objects.get(examinee=username)  # get exam instance from database
    print "posted logic goes here you answered question with %s" % {answer}
    num = request.session['curr_ques']
    if clicked == "forward":
        print "forward"
        num = num + 1
        if num > request.session['numques'] - 1:
            num = 0
        request.session['curr_ques'] = num
        qnum = request.session['qlist'][num]
    else:
        print "back"
        num = num - 1
        if num < 0:
            num = request.session['numques'] - 1
        request.session['curr_ques'] = num
        qnum = request.session['qlist'][num]
        
    
    return displayques(request)