from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Blog, PostImage, Comment, Tag
from .forms import CommentForm

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    if request.method == 'POST':
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            blog = get_object_or_404(Blog, pk=blog_id)
            content = request.POST.get('content')
            comment = Comment.objects.create(post = blog, user = request.user, content = content)
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        cf = CommentForm()
        blog = get_object_or_404(Blog, pk=blog_id)
        photos = PostImage.objects.filter(post=blog_id)
        comment = Comment.objects.filter(post=blog_id)
        tag = Tag.objects.filter(post=blog_id)
        return render(request, 'updated/detail_blog.html',{'blog':blog, 'photos':photos, 'comments':comment ,'comment_form':cf, 'tag': tag})
