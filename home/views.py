from django.views.generic import UpdateView, ListView
from django.shortcuts import render
from form.models import Formstudent
from django.shortcuts import render
from form.forms import FormstudentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.


# def home(request):

#     reportstudent = Formstudent.objects.all()

#     return render(request,'home.html',{'reportstudent':reportstudent})

# class ReportstudentListView(ListView):
#     model = Formstudent
#     context_object_name = 'reportstudent'
#     template_name = 'home.html'

def home(request):
    
    return render(request, "home/home.html")