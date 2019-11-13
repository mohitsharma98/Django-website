from django.shortcuts import render, get_object_or_404
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

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        context = {'post': post}
        return render(request, 'blog/blog_detail.html', context)