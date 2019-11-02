from django.shortcuts import render
from contact.forms import ContactForm
from contact.models import Contact

# Create your views here.

def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
    
    context = {
        'form' : form,
    }

    return render(request, "contact/contact.html", context)