from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'category', 'author', 'image_url', 'short_description', 'content', 'created_at')
