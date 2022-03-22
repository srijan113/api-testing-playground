import imp
from rest_framework import serializers
from .models import Blog



class CreateBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'active']




class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

