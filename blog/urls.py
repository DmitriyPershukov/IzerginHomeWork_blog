from django.urls import path

from .views import PostView

urlpatterns = [
    path('posts/<int:id>/', PostView.as_view(), name='post'),
]