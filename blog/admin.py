from django.contrib import admin
from .models import Blog, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage

# admin.site.register(Blog)
@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Blog

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass