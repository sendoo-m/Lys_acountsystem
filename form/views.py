from django.views.generic import UpdateView, ListView
from form.models import Formstudent
from django.shortcuts import get_object_or_404, render
from form.forms import FormstudentForm, Update_StudentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
# Create your views here.

# def studentform_form(request):
#     return render(request, 'form/student_form.html')


def studentform_form(request):
    if request.method == "POST":

        form = FormstudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تسجيل الطالب بنجاح !")
            return HttpResponseRedirect('/form')
    else:
        form    = FormstudentForm()
        context = {
                "form":form
            }
        return render(request, "form/student_form.html", context)

def allstudents(request):
    data        = Formstudent.objects.all()
    context     = {
        'data':data
    }
    return render(request, 'form/all_student.html', context)

# ---------------------------------
# Edit student to DB From HTML File and this file come from forms
# ---------------------------------

def edit(request, id): #def edit student in urls
    edit = get_object_or_404(Formstudent, id=id)
    if request.method == 'POST': #POST in form edit student in edit student html
        formtohtml = Update_StudentForm(request.POST, instance=edit) # edit student come from forms.py
        if formtohtml.is_valid():
            formtohtml.save() # to save data in forms
            messages.success(request, 'تم تسجيل دفع القسط بنجاح')
            return HttpResponseRedirect('/form/')
    else:
        formtohtml= Update_StudentForm(instance=edit)
        return render(request,'form/edit.html', {'updatehtml':formtohtml}) # edit student From forms.py 
# ---------------------------------
#  END Add Student to DB Code
# ---------------------------------

def search(request):
    return render(request, 'form/search.html')


# ---------------------------------
# Search From HTML File To Get Results in another files
# ---------------------------------
def result(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multple_q = Q(Q(name__icontains=q) | Q(id_number__iexact=q)) # def multple_q and Q to allow search 2 fields
        data = Formstudent.objects.filter(multple_q)
        context={
            'data':data
        }
    return render(request,'form/search_result.html',context)
# ---------------------------------
#  END Search Results Code
# ---------------------------------


def sumfees(request):
    val1 = int(request.GET['school_fees'])
    val2 = int(request.GET['activity'])
    val3 = int(request.GET['discount'])
    val4 = int(request.GET['f_installment'])
    val5 = int(request.GET['s_installment'])
    val6 = int(request.GET['th_installment'])

    res = val1 + val2 - val3
    finl = val4 + val5 + val6

    context = {
        'res_net_expenses':res,
        'res_remaining_amount':finl,
    }
    return render(request, 'form/all_student.html', context)
