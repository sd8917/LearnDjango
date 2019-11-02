from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogindex.html', {'blogs': blogs})


def blogdetail(request, slug):
    post = get_object_or_404(Blog, Slug = slug)
    return render(request,'blog/blogdetail.html', {'blog':post})