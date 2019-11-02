from django.shortcuts import render
from blog.models import Post

# Create your views here.
def BlogListView(request):
    object_list = Post.objects.all()

    context = {
        'object_list':object_list
    }
    return render(request, 'blog/blog_list.html', context)