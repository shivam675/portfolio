from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/',  blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'portfolio/images/')
 
    def __str__(self):
        return self.post.title