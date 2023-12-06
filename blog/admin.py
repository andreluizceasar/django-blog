from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_field= ('title', 'content')



admin.site.register(Post, PostAdmin)
    