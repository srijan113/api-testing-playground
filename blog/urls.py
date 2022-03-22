import imp
from pkgutil import ImpImporter
from django.urls import path
from .views import BlogApiView, CreateBlogApiView, ListBlogApiView


urlpatterns = [
    path('', ListBlogApiView.as_view()),
    path('create/', CreateBlogApiView.as_view()),
    path('<int:pk>/', BlogApiView.as_view()),



]


