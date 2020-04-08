from rest_framework.serializers import ModelSerializer, ReadOnlyField

from posts.models import Comment, Post


class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['pub_date']


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['post']
