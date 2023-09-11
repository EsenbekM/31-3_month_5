from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'News: {self.title}'


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
