from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import views
from django.template.response import TemplateResponse
from exams.views import intro
from examinee.models import Examinee
from .forms import LoginForm


def authuser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            username = first_name+last_name+password
            user = authenticate(username=username, password=password)
            if user is not None:
               login(request, user)
               return redirect('exams/intro')
               #return render(request,'exams/intro.html')
            else:
               form.add_error(None,'name or password invalid')
    else:
        form = LoginForm()
        
    return render(request, 'login2.html', {'form': form,'error':'invalid password'})
   


def welcome(request):
    context = {'title' : 'Welcome'}
    return render(request, 'welcome.html', context)
    
def about(request):
    context = {'title' : 'About'}
    return render(request, 'about.html', context)
    
# def mylogin(request):
#     context = {'title' : 'Login'}
#     return render(request, 'registration/login.html', context)
    
# def loginpost(request):
#     fname = request.POST['fname']
#     lname = request.POST['lname']
#     pword = request.POST['pword']
    
#     if (fname == 'admin' and lname =='admin' and pword == 'admin'):
#         return redirect('/admin/')
        
#     else:
#         examinee = authenticate(fname,lname,pword)
#         if not examinee:
#             return HttpResponse("responses %s,%s,%s,%s" % (fname,lname,pword,examinee))
#         else:
#             return HttpResponse("we have a winner <b>%s</b>:" % examinee)

        
# def authenticateuser(fname,lname,pword):
#     #examinee = get_object_or_404(Examinee,fname=fname )
#     try:
#         examinee = Examinee.objects.get(first_name=fname,last_name=lname,regnum=pword)
#         return examinee
#     except ObjectDoesNotExist:
#         examinee = False
#         context = False
#         return render('/login/',context)
    
    
# def mylogin(request):
#     template_response = views.login(request)
#     template_response.context={'myvar':'myvar content'}
#     return template_response
#     #return render(request, 'registration/login.html',context)
    
def mail(to,cc,subject,message):
    mailfrom = "markndennis@hotmail.com"
    send_mail(subject, message, mailfrom, [to], fail_silently=False)
    return

