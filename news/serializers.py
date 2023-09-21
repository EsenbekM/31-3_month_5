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



class NewsValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(required=False)
    is_active = serializers.BooleanField(required=False)
    category_id = serializers.IntegerField()
    tags = serializers.ListField(
        child=serializers.IntegerField()
    )

    def validate_category_id(self, value):
        try:
            Category.objects.get(id=value)
        except Category.DoesNotExist as e:
            raise serializers.ValidationError(str(e))
        
        return value
    
    def validate_tags(self, value: list):
        for tag_id in value:
            try:
                Tag.objects.get(id=tag_id)
            except Tag.DoesNotExist as e:
                raise serializers.ValidationError(str(e))
        
        return value

    def create(self, validated_data):
        title = validated_data.get('title')
        content = validated_data.get('content')
        is_active = validated_data.get('is_active')
        category_id = validated_data.get('category_id')
        tags = validated_data.get('tags')
        
        news = News.objects.create(
            title=title, 
            content=content,
            category_id=category_id,
            is_active=is_active
            )
        
        news.tags.set(tags)

        return news
    

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.tags.set(validated_data.get('tags', instance.tags.all()))
        instance.save()

        return instance