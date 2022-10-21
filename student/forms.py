from dataclasses import fields
from django import forms
from django import forms
from .models import StudentModel,S_name




class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        exclude = ('__all__')



class s_nameForm(forms.ModelForm):
    class Meta:
        model = S_name
        fields = ('name',)