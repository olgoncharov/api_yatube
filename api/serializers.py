from rest_framework.serializers import ModelSerializer, SerializerMethodField
from posts.models import Post, Comment


class PostSerializer(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['pub_date']

    def get_author(self, obj):
        return obj.author.get_full_name()
