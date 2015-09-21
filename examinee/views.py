from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from examinee.models import Examinee, ExamInstance, ExamResults
from exams.models import ExamType, Questions
from invigilator.models import Invigilator
from django.core.mail import send_mail
#from caa.views import mail
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from random import shuffle
from django.conf import settings
from django.template.response import TemplateResponse
import datetime

# Create your views here.

def home(request):
    context = {'title' : 'Examinee Home'}
    return render(request, 'examinee/home.html', context)
    
# def apply(request):
#     exam_types = ExamType.objects.all()
#     invig_list = Invigilator.objects.order_by('institution','last_name')
#     intend_date = (datetime.datetime.now()+datetime.timedelta(30))
#     intend_date = intend_date.strftime('%Y-%m-%d')
#     context = {
#         'title' : 'Exam Application',
#         'exam_types' : exam_types,
#         'invig_list' : invig_list,
#         'intend_date' : intend_date,
#         }
#     return render(request, 'examinee/apply.html', context)
    
# def application(request):
#     postdata={
#     'fname' : request.POST['fname'],
#     'lname' : request.POST['lname'],
#     'regnum' : request.POST['regnum'],
#     'email' : request.POST['email'],
#     'exam' : ExamType.objects.get(pk=request.POST['exam']),
#     'invigilator' : Invigilator.objects.get(pk=request.POST['invigid']),
#     'intended' : request.POST['examdate'],
#     'dob' : request.POST['dob'],
#     }
    
#     ne = Examinee()
#     ne.first_name = postdata['fname']
#     ne.last_name = postdata['lname']
#     ne.regnum = postdata['regnum']
#     ne.email = postdata['email']
#     ne.exam_type = postdata['exam']
#     ne.invigilator = postdata['invigilator']
#     ne.dob = postdata['dob']
#     ne.intended = postdata['intended']
#     ne.save()
    
#     #mail("markndennis@hotmail.com","markndennis@hotmail.com","test mail","%s this is your test mail" %answer1)
#     #return HttpResponse("Hello, %s %s <br/> you selected invigilator %s and exam %s" %(answer1, answer2, answer3, answer4))
    
#     return render(request, 'examinee/applicationConfirmation.html', postdata)
    

# @login_required
# def examineelist(request):
#     object_list = Examinee.objects.order_by('last_name')
#     logout = '<a href="/logout?next=/" >(logout)</a>'
#     user_greeting = "Welcome "+request.user.first_name + "! " + logout
#     context = {'object_list':object_list,'title':'Examinee List', 'user_greeting':user_greeting}
#     return render(request, 'examinee/examinee_list.html', context)
    


# checks to see if an examinstance exists and if not creates one by calling createexaminstance
def checkexaminstance(username):
    print "checkexaminstance called"
    try:
        instance = ExamInstance.objects.get(examinee=username)
        print "exam instance exists"
    except:
        createexaminstance(username)
    return

# creates an examinstance
def createexaminstance(username):
    instance = ExamInstance()
    instance.examinee = username
    #now = datetime.datetime.now()
    #instance.start_time = now
    qlist = makeexamineequeslist()
    for q in qlist:
        result = ExamResults(examinee=username,ques_number=q)
        result.save()
    qstr = ','.join(str(e) for e in qlist)
    instance.ques_sequence = qstr
    instance.save()
    return
    
    



# the number of questions required for each examtype
quesprofile={
    "IC" : 9,
    "RM" : 15,
    "AC" : 16
    }
    

# creates a random list of questions meeting the specifications of quesprofile
def makeexamineequeslist():
    dlist = []
    
    #iterate through the question profile dictionary    
    for subtest in quesprofile.keys():
        st = subtest
        num = quesprofile[st]
        # get a query set for each exam type
        qlist = getquestions(st,num)
        # convert the queryset into a list
        mylist = list(qlist)
        # randomize the list
        shuffle(mylist)
        # iterate the list pulling out the number required by question profile
        for e in mylist[:num]:
          dlist.append(e.qnum) 
    
    # return the list to the display
    return dlist
    
def getquestions(st,num):
    qlist = Questions.objects.all().filter(examtype = st)
    return qlist




# class ExamineeListView(ListView):
#     model = Examinee
    
#     @login_required
#     def get_context_data(self, **kwargs):
#         context = super(ExamineeListView, self).get_context_data(**kwargs)
#         context['title'] = "Examinee List Generic View"
#         return context