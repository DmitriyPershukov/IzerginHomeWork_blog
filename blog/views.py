from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User

from .models import Post, Commentary


class PostView(TemplateView):
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(id = kwargs['id'])
        context['post'] = post
        return context