from django import forms
from django.forms import Textarea
from contact.models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'content',
        ]
        widgets = {
            'content' : Textarea(attrs={'cols':50, 'rows':4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'name':'name', 'type':'text', 'autocomplete':'off'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'name': 'email', 'type':'email', 'autocomplete':'off'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'name':'message', 'id':'exampleMessage1'})