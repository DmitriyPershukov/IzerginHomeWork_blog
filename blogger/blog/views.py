from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        attribute_values = list(User.objects.values_list('username', flat=True))
        context['names'] = attribute_values
        return context