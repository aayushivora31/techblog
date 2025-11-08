import os
import django
from typing import TYPE_CHECKING, Any

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

from django.contrib.auth.models import User
from tech.models import Tutorial, Article, Snippet
from django.utils import timezone

if TYPE_CHECKING:
    from django.db.models.manager import Manager
    from tech.models import Tutorial as TutorialModel, Article as ArticleModel, Snippet as SnippetModel

def create_sample_data() -> None:
    # Create a user if one doesn't exist
    if not User.objects.filter(username='admin').exists():
        # Type ignore for unused call result
        _ = User.objects.create_user(  # type: ignore
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        # Type ignore for unknown return type
        user: User = User.objects.get(username='admin')  # type: ignore
        print("Created user: admin")
    else:
        # Type ignore for unknown return type
        user: User = User.objects.get(username='admin')  # type: ignore
    
    # Create sample tutorials
    tutorials_data = [
        {
            'title': 'Getting Started with Python',
            'description': 'Learn the basics of Python programming language',
            'content': 'Python is a high-level programming language...',
        },
        {
            'title': 'Django Web Development',
            'description': 'Build web applications with Django framework',
            'content': 'Django is a high-level Python web framework...',
        },
        {
            'title': 'JavaScript Fundamentals',
            'description': 'Master the essentials of JavaScript',
            'content': 'JavaScript is the programming language of the web...',
        }
    ]
    
    for tut_data in tutorials_data:
        if not Tutorial.objects.filter(title=tut_data['title']).exists():
            # Type ignore for unused call result
            _ = Tutorial.objects.create(  # type: ignore
                title=tut_data['title'],
                description=tut_data['description'],
                content=tut_data['content'],
                author=user,
                created_at=timezone.now()
            )
            print(f"Created tutorial: {tut_data['title']}")
    
    # Create sample articles
    articles_data = [
        {
            'title': 'The Future of Web Development',
            'content': 'Web development is constantly evolving...',
        },
        {
            'title': 'Best Practices for Code Quality',
            'content': 'Writing clean, maintainable code is essential...',
        },
        {
            'title': 'Understanding RESTful APIs',
            'content': 'REST APIs are the backbone of modern web services...',
        }
    ]
    
    for article_data in articles_data:
        if not Article.objects.filter(title=article_data['title']).exists():
            # Type ignore for unused call result
            _ = Article.objects.create(  # type: ignore
                title=article_data['title'],
                content=article_data['content'],
                author=user,
                created_at=timezone.now()
            )
            print(f"Created article: {article_data['title']}")
    
    # Create sample snippets
    snippets_data = [
        {
            'title': 'Hello World in Python',
            'code': 'print("Hello, World!")',
            'language': 'python',
        },
        {
            'title': 'CSS Flexbox Example',
            'code': '.container { display: flex; justify-content: center; align-items: center; }',
            'language': 'css',
        },
        {
            'title': 'JavaScript Array Map',
            'code': 'const doubled = numbers.map(num => num * 2);',
            'language': 'js',
        }
    ]
    
    for snippet_data in snippets_data:
        if not Snippet.objects.filter(title=snippet_data['title']).exists():
            # Type ignore for unused call result
            _ = Snippet.objects.create(  # type: ignore
                title=snippet_data['title'],
                code=snippet_data['code'],
                language=snippet_data['language'],
                author=user,
                created_at=timezone.now()
            )
            print(f"Created snippet: {snippet_data['title']}")
    
    print("\nSample data population complete!")
    print(f"Total tutorials: {Tutorial.objects.count()}")
    print(f"Total articles: {Article.objects.count()}")
    print(f"Total snippets: {Snippet.objects.count()}")

if __name__ == '__main__':
    create_sample_data()