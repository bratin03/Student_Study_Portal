from django import forms 
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']

class DateInput(forms.DateInput):
    input_type='date'

class (HomeworkForm9forms.ModelForm):
    class Meta:
        model=Homework
        widgets={'due':DateInput()}
        fields=['subjects','title','description','due','is_finished']

class DashboardForm(form.Form):
    text= forms.CharField(max_length=100,label="Enter Youtube Search : ")

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']

class ConversionForm(forms.Form):
    CHOICES=[('length','Length'),('mass','Mass')]
    measurement=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

class ConversionMassForm(form.Form):
    CHOICES=[('pound','Pound'),('kilogram','Kilogram')]
    input=forms.Charfield(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number'}
    ))
    measure1=forms.Charfield(
        label='',widget=forms.Select(choices=CHOICES)
    )
    measure2=forms.Charfield(
        label='',widget=forms.Select(choices=CHOICES)
    )