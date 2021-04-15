from django.contrib import admin
from .models import Blog, PostImage, Comment


class PostImageAdmin(admin.StackedInline):
    model = PostImage

class PostCommentAdmin(admin.StackedInline):
    model = Comment

# admin.site.register(Blog)
@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Blog

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class PostCommentAdmin(admin.ModelAdmin):
    pass