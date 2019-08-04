from totoapp.models import Item
from django import forms

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ("title", "description", "status", "expired_at")
        widgets = {
        'expired_at': forms.DateInput(attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
