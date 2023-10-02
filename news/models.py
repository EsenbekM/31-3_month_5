from django.db import models
import uuid


class BaseModel(models.Model):
    # id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Category: {self.name}'


class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Tag: {self.name}'


class News(BaseModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='news',
        null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='news')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'News: {self.title}'

    def category_str(self):
        if self.category:
            return self.category.name
        return None


class Comment(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Comment: {self.content}'
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
