from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()
    body = models.TextField()
    picture = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.title

class Commentary(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "commentaries"