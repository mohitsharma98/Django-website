from django.shortcuts import render
from django.views.generic import TemplateView
from gallery.models import Gallery
# Create your views here.
def GalleryView(request):
    gallery = Gallery.objects.all()
    context = {'gallery':gallery}
    return render(request, 'gallery/gallery.html', context)


