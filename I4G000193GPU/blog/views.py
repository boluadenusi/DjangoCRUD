from pyexpat import model
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = [
        "title",
        "slug",
        "author",
        "body",
        "publish",
        "created",
        "updated",
        "status"
    ]
    success_url  = reverse_lazy("blog:all")
    template_name = 'blog/post_form.html'


class PostDetailView(DetailView):
    model = Post
    

class PostUpdateView(UpdateView):
    model = Post
    fields = [
        "title",
        "slug",
        "author",
        "body",
        "publish",
        "created",
        "updated",
        "status"
    ]
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = [
        "title",
        "slug",
        "author",
        "body",
        "publish",
        "created",
        "updated",
        "status"
    ]
    success_url  = reverse_lazy("blog:all")
    template_name = 'blog/post_form.html'