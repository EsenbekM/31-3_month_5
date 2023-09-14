from rest_framework import serializers
from news.models import News, Comment, Category, Tag


# class NewsSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     title = serializers.CharField()
#     content = serializers.CharField()
#     is_active = serializers.BooleanField()
#     view_count = serializers.IntegerField()
#     # created_at = serializers.DateTimeField()
#     # updated_at = serializers.DateTimeField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class NewsListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    comments = CommentListSerializer(many=True)
    # category_name = serializers.CharField(source='category.name')
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'comments', 'view_count', 
                  'category', 'tags', 'created_at', 'updated_at',
                  'category_name', 'category_str')

    def get_category_name(self, news):
        if news.category:
            return news.category.name
        return None
    

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

