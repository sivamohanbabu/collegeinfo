from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'joining_date']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'})
        }