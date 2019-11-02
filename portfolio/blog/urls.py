from django.urls import path
from blog.views import BlogListView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView, name='blog')
]