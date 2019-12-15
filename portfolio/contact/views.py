from django.shortcuts import render
from contact.forms import ContactForm
from contact.models import Contact, Information

# Create your views here.

def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
    
    info = Information.objects.all()

    context = {
        'form' : form,
        'info' : info,
    }

    return render(request, "contact/contact.html", context)