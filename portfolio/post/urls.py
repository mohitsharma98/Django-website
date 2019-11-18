from django.urls import path
from post import views
from post.views import index

app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
]