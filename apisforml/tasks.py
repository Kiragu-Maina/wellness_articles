# tasks.py (Celery task)
from celery import shared_task
from datetime import timedelta
import random
from .models import Article
from channels.layers import get_channel_layer

@shared_task
def send_random_prompt(user_id):
    channel_layer = get_channel_layer()
    prompts = ["How are you feeling today?", "Tell us about your mood.", "How's your wellness journey going?"]
    random_prompt = random.choice(prompts)
    
    channel_name = f"user_{user_id}"
    async_to_sync(channel_layer.send)(channel_name, {"type": "prompt.user", "prompt": random_prompt})

@shared_task
def send_suitable_article(user_id, feeling):
    channel_layer = get_channel_layer()
    suitable_articles = Article.objects.filter(category__icontains=feeling).order_by('?')[:1]
    
    if suitable_articles:
        article = suitable_articles[0]
        article_data = {
            "title": article.title,
            "url": article.url,
            # Include other relevant article data
        }
        
        channel_name = f"user_{user_id}"
        async_to_sync(channel_layer.send)(channel_name, {"type": "send.article", "article_data": article_data})
