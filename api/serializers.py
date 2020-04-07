from rest_framework.serializers import ModelSerializer
from posts.models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'pub_date']