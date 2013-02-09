from django import forms
from models import Faculty
class ScanForm(forms.Form):
    title= forms.CharField(max_length= 100)
    faculty= forms.CharField(max_length= 100)
    pages= forms.IntegerField
