from .models import Category, Tag, News, Comment


def add_news_tag_catygory_comment(count):
    for i in range(count):
        category = Category.objects.create(name=f'Category {i}')
        tag = Tag.objects.create(name=f'Tag {i}')
        news = News.objects.create(
            title=f'News {i}',
            content=f'Content {i}',
            category=category
        )
        news.tags.add(tag)
        Comment.objects.create(
            news=news,
            content=f'Comment {i}',
            author=f'Author {i}'
        )

