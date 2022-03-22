from rest_framework import generics

from .models import Blog
from .serializers import BlogSerializer, CreateBlogSerializer




class ListBlogApiView(generics.ListAPIView):
    serializer_class = CreateBlogSerializer
    queryset = Blog.objects.all()



class CreateBlogApiView(generics.CreateAPIView):
    serializer_class = CreateBlogSerializer
    queryset = Blog.objects.all()



class BlogApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()



