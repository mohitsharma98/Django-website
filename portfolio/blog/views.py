from django.shortcuts import render
from blog.models import Post
from django.views.generic import DetailView

# Create your views here.
def BlogListView(request):
    object_list = Post.objects.all()

    context = {
        'object_list':object_list
    }
    return render(request, 'blog/blog_list.html', context)


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/blog_detail.html"
