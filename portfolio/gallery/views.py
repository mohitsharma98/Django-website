from django.shortcuts import render

# Create your views here.
def GalleryView(request):
    return render(request, 'gallery/gallery.html')