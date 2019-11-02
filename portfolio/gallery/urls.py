from django.urls import path
from gallery.views import GalleryView

app_name = 'gallery'

urlpatterns = [
    path('', GalleryView, name='gallery')
]