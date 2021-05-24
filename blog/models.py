from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    thought = models.CharField(default='Notice me senpai' ,max_length=200)
    two_line_des = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/',  blank=True)
    date = models.DateField()
    type = [
    ('automation','automation'),
    ('ROS', 'ROS'),
    ('microcontroller','microcontroller'),
    ]
    tags = models.CharField(max_length=20, choices=type, default='automation')
    # user_name = models.ForeignKey(User, default=None, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'portfolio/images/')

    def __str__(self):
        return self.post.title

class Tag(models.Model):
    post = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    t = models.CharField(max_length=20, default='robot operating system')

class Comment(models.Model):
    post = models.ForeignKey(Blog, default=None, on_delete = models.CASCADE, related_name ='comments')
    user_name = models.CharField(max_length=20, default='anon')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
