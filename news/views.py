from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import News, Comment
from news.serializers import NewsListSerializer, NewsDetailSerializer, CommentListSerializer


@api_view(['GET'])
def hello_world(request):
    dct = {
        'message': 'Hello, world!',
        'int': 123,
        'float': 123.456,
        'list': [1, 2, 3],
        'dict': {
            'a': 1,
            'b': 2,
            'c': 3,
        },
        'bool': True
    }

    return Response(dct)


@api_view(['GET', 'POST'])
def news_list(request):
    if request.method == "GET":
        search = request.GET.get('search', '')
        # get all news
        news = News.objects.select_related('category').prefetch_related(
            'tags', 'comments').filter(title__icontains=search)
        # SELECT * FROM news_news;
        # serialize news
        data = NewsListSerializer(instance=news, many=True).data
        return Response(data, status=200)

    elif request.method == "POST":
        title = request.data.get('title')
        content = request.data.get('content')
        category_id = request.data.get('category_id')
        tags = request.data.get('tags', [])
        
        news = News.objects.create(
            title=title, 
            content=content,
            category_id=category_id,
            )
        
        # 1 способ
        news.tags.set(tags)
        
        # 2 способ
        # for tag_id in tags:
        #     news.tags.add(tag_id)
        
        # 3 способ
        # news.tags.add(*tags)
        
        data = NewsListSerializer(instance=news, many=False).data
        return Response(data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def news_detail(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist:
        return Response(
            {'ERROR': f"Новости с id {news_id} не существует"},
            status=404
            )

    if request.method == "GET":
        serializer = NewsDetailSerializer(instance=news, many=False)
        return Response(serializer.data, status=200)

    elif request.method == "PUT":
        news.title = request.data.get('title', news.title)
        news.content = request.data.get('content', news.content)
        news.category_id = request.data.get('category_id', news.category_id)
        news.tags.set(request.data.get('tags', news.tags.all()))
        news.save()

        data = NewsListSerializer(instance=news, many=False).data

        return Response(data, status=200)
    
    elif request.method == "DELETE":
        news.delete()
        return Response(status=204)
    

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    data = CommentListSerializer(instance=comments, many=True).data

    return Response(data)
