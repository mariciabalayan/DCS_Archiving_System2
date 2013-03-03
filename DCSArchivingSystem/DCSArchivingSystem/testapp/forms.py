from django import forms
from models import Faculty
from models import Transaction
class ScanForm(forms.Form):
    #title= forms.CharField(max_length= 100)
    transactions= forms.ChoiceField(choices=Transaction.objects.all())
    faculty= forms.CharField(max_length= 100)
    pages= forms.IntegerField
