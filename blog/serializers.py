import imp
from rest_framework import serializers
from .models import Blog



class CreateBlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id','title', 'description', 'image', 'active']




class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id','title', 'description', 'image', 'active', 'updated_at', 'created_at']

