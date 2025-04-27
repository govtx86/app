from django import forms
from .models import Tracker

class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = (
            "desc",
            "amount",
            "date",
            "category",
        )
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }