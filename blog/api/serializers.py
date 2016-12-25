from rest_framework.serializers import ModelSerializer
from blog.models import Blog


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'created_at',
        ]
