from django import forms
from .models import Person

class MemberForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['firstname','lastname','password','phone','email','date']