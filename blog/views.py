from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, PostImage, Comment
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
            return redirect('home')
    else:
        cf = CommentForm()
        blog = get_object_or_404(Blog, pk=blog_id)
        photos = PostImage.objects.filter(post=blog_id)
        comment = Comment.objects.filter(post=blog_id)
        return render(request, 'blog/detail.html',{'blog':blog, 'photos':photos, 'comments':comment ,'comment_form':cf})
