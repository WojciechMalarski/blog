from django.shortcuts import render
from .models import Autor,Post
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
class PostView(DetailView):
    model = Post
    template_name = 'post_detail.html'
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
