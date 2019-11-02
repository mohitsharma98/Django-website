from django import forms
from django.forms import Textarea
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'content',
        ]
        widgets = {
            'content' : Textarea(attrs={'cols':80, 'rows':2})
        }