from rest_framework import serializers
from myblog.models import Post, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'title', 'text', 'author', 'created_date', 'modified_date', 'published_date')

    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=128)
    text = serializers.CharField(style={'base_template': 'textarea.html'})
    author = serializers.CharField(required=True)
    created_date = serializers.DateTimeField(required=True)
    modified_date = serializers.DateTimeField(required=True)
    published_date = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.author = validated_data.get('author', instance.author)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.modified_date = validated_data.get('modified_date', instance.modified_date)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'description')

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=True, max_length=128)
    description = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance