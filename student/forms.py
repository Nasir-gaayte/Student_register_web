from django import forms
from django import forms
from .models import StudentModel




class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        exclude = ('__all__')



