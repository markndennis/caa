from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from invigilator.models import Invigilator
from django.views import generic


# Create your views here.

def home(request):
    curr_user = request.user
    greeting = "Welcome " + curr_user.first_name
    context = {'title' : 'Invigilator Home' , 'user_greeting' : greeting }
    return render(request, 'invigilator/home.html', context)
    
def invigilator_detail(request, invig_id):
    thisinvigilator = get_object_or_404(Invigilator, pk=invig_id)
    title = 'Invigilator ' + thisinvigilator.first_name + " " + thisinvigilator.last_name+ ' Details'
    context = {'invigilator':thisinvigilator, 'title':title}
    return render(request, 'invigilator/detail.html', context)    

    
# class invigilator_list(generic.ListView):
#     model = Invigilator
#     template_name = 'invigilator/invigilatorList.html'
     
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(invigilator_list, self).get_context_data(**kwargs)
#         curr_user = user
#         greeting = "Welcome " + curr_user.first_name
#         context['user_greeting'] = "Welcome "
#         context['title'] = "List of Approved Invigilators"
#         return context 

def invigilator_list(request, so):
    #sord='last_name'
    invig_list = Invigilator.objects.order_by(so)
    context = {'invigilatorList':invig_list,'title':'Invigilator List'}
    return render(request, 'invigilator/invigilatorList.html', context)
    

        

     