from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Category: {self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Tag: {self.name}'


class News(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='news',
        null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='news')
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'News: {self.title}'

    def category_str(self):
        if self.category:
            return self.category.name
        return None


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Comment: {self.content}'
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
