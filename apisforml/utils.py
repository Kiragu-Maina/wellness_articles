from newsapi import NewsApiClient
from .models import Article

# Define the maximum lengths for your database columns
MAX_TITLE_LENGTH = 255
MAX_SHORT_DESCRIPTION_LENGTH = 512
MAX_CONTENT_LENGTH = 2048

def save_article_to_db(article):
    try:
        title = article.get('title')
        short_description = article.get('description', '')
        content = article.get('content', '')

        # Check if the text lengths are within the allowed limits
        if len(title) <= MAX_TITLE_LENGTH and len(short_description) <= MAX_SHORT_DESCRIPTION_LENGTH and len(content) <= MAX_CONTENT_LENGTH:
            Article.objects.create(
                title=title,
                category='wellness',  # You can set the category as you like
                author=article.get('author', ''),
                short_description=short_description,
                content=content,
                published_at=article.get('publishedAt', ''),  # Use the appropriate field
                image_url=article.get('urlToImage', ''),
                readmoreurl=article.get('url', '')  # Use the appropriate field
            )
            return True
        else:
            print(f"Entry exceeds the maximum allowed length for one or more fields. Skipping this article.")
            return False
    except Exception as e:
        # Print or log the exception for debugging purposes
        print(f"An error occurred: {str(e)}")
        return False

def articletodb():
    try:
        newsapi = NewsApiClient(api_key='3643ab3265664d62b65c32577344769f')
        articles_response = newsapi.get_everything(
            q='health, wellness, fitness, mental-health',
            language='en',
            sort_by='relevancy',
            page_size=50  # Specify the number of articles you want to fetch
        )

        articles = articles_response.get('articles', [])  # Get the 'articles' list from the response

        for article in articles:
            if not save_article_to_db(article):
                continue  # Skip this article and move to the next

        return True
    except Exception as e:
        # Print or log the exception for debugging purposes
        print(f"An error occurred: {str(e)}")
        return False
