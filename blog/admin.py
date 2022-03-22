import imp
from django.contrib import admin
from .models import Blog




class BlogAdmin(admin.ModelAdmin):

    list_display = ['title', 'active']

    class Meta:
        model = Blog



admin.site.register(Blog, BlogAdmin)

