from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Article
from .utils import articletodb
from .serializers import ArticleSerializer  # Import your ArticleSerializer here

class ArticlesView(APIView):
    def get(self, request):
        # Fetch new articles from the API and store them in the database
        response = articletodb()
        if response:
            # Retrieve 10 article objects from the database (make sure to specify the order_by condition)
            articles = Article.objects.order_by('?')[:10]
            
            # Serialize the articles using your serializer
            serialized_articles = ArticleSerializer(articles, many=True).data

            return Response(serialized_articles)
        else:
            return JsonResponse({'error': 'Failed to fetch articles'}, status=400)
