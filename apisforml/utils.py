from newsapi import NewsApiClient
from .models import Article

def articletodb():
    try:
        newsapi = NewsApiClient(api_key='3643ab3265664d62b65c32577344769f')
        articles_response = newsapi.get_everything(
            q='health, wellness, fitness, mental-health',
            language='en',
            sort_by='relevancy',
            page_size=50  # Specify the page you want to fetch
        )

        articles = articles_response.get('articles', [])  # Get the 'articles' list from the response
        
        for article in articles:
            title = article.get('title')
            if title and title != 'None':  # Check if title is not empty or 'None'
                Article.objects.create(
                    title=title,
                    category='wellness',  # You can set the category as you like
                    author=article.get('author', ''),
                    short_description=article.get('description', ''),
                    content=article.get('content', ''),
                    published_at=article.get('publishedAt', ''),  # Use the appropriate field
                    image_url=article.get('urlToImage', ''),
                    readmoreurl=article.get('url', '')  # Use the appropriate field
                )

        return True
    except Exception as e:
        # Print or log the exception for debugging purposes
        print(f"An error occurred: {str(e)}")
        return False
