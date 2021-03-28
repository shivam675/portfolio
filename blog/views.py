from django.shortcuts import render, get_object_or_404
from .models import Blog, PostImage

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    photos = PostImage.objects.filter(post=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog, 'photos':photos})
