from django.urls import path, re_path
from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView, name='blog'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail')
]