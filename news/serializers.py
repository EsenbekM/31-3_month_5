from rest_framework import serializers
from news.models import News, Comment


# class NewsSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     title = serializers.CharField()
#     content = serializers.CharField()
#     is_active = serializers.BooleanField()
#     view_count = serializers.IntegerField()
#     # created_at = serializers.DateTimeField()
#     # updated_at = serializers.DateTimeField()


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'view_count',)


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"