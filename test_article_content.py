import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

from tech.models import Article

def test_article_content():
    """Test to check what content is actually stored in articles"""
    articles = Article.objects.all()
    print(f"Found {articles.count()} articles")
    
    for article in articles:
        print(f"\n--- Article: {article.title} ---")
        print(f"ID: {article.id}")
        print(f"Content length: {len(article.content) if article.content else 0}")
        print(f"Content preview: {article.content[:200] if article.content else 'None'}")
        print(f"Tags: {article.tags}")
        print(f"Author: {article.author.username}")
        print("-" * 40)

if __name__ == '__main__':
    test_article_content()