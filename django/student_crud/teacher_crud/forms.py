from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        Model = Teacher
        fields = '__all__'