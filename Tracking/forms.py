# forms.py
from django import forms
from .models import Achivement

class AchivementForm(forms.ModelForm):
    class Meta:
        model = Achivement
        fields = ['studentId', 'advisorId', 'sportClubsCode', 'session', 'date', 'achivement', 'merit']
        widgets = {
            'studentId': forms.Select(attrs={'class': 'form-control'}),
            'advisorId': forms.Select(attrs={'class': 'form-control'}),
            'sportClubsCode': forms.Select(attrs={'class': 'form-control'}),      
        }

from .models import MeritRequest

class MeritRequestForm(forms.ModelForm):
    class Meta:
        model = MeritRequest
        fields = ['description', 'image']