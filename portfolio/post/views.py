from django.shortcuts import render
from django.views.generic.base import TemplateView
from post.models import IndexModel
# Create your views here. 
# class index(TemplateView):
#     object_list = IndexModel.objects.all()
#     context = {
#         'object_list': object_list
#     }
#     template_name = "post/index.html"

def index(request):
    object_list = IndexModel.objects.all()
    context = {'object_list':object_list}
    return render(request, 'post/index.html', context)