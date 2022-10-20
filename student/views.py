import genericpath
from operator import ge
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from .forms import StudentForm
from .models import StudentModel

# Create your views here.


def home(request):
    return render(request,'student/home.html')



class Add_studentView(generic.CreateView):
    
    form_class= StudentForm
    template_name = 'student/add_student.html'
    
    
class AllDetailView(generic.ListView):
    model = StudentModel
    form_class= StudentForm
    context_object_name= 'objects'
    template_name = 'student/detail.html'    
    


# class AboutStudent(generic.ListView):
#     model = StudentModel
#     form_class= StudentForm
#     context_object_name= 'details'
#     template_name= 'student/detail_id.html'  

def aboutstudent(request, pk):
    details = StudentModel.objects.get(id= pk)
    
    return render(request,'student/detail_id.html',{'details':details})