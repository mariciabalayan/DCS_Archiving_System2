from django import forms

class ScanForm(forms.Form):
    title= forms.CharField(max_length= 100)
    pages= forms.IntegerField
    record= forms.CharField(max_length= 100)
    faculty= forms.ModelChoiceField(Faculty)