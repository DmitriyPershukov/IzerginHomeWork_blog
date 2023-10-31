from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User

from .models import Post, Commentary


class PostView(ListView):
    model = Post
    template_name = 'post.html'