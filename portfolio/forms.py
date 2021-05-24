from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields =[
        'first_name',
        'last_name',
        'email_adress',
        'message',
        ]
        # fields ="__all__"
