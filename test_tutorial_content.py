import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

from tech.models import Tutorial

def test_tutorial_content():
    """Test to check what content is actually stored in tutorials"""
    tutorials = Tutorial.objects.all()
    print(f"Found {tutorials.count()} tutorials")
    
    for tutorial in tutorials:
        print(f"\n--- Tutorial: {tutorial.title} ---")
        print(f"ID: {tutorial.id}")
        print(f"Description: {tutorial.description}")
        print(f"Content length: {len(tutorial.content) if tutorial.content else 0}")
        print(f"Content preview: {tutorial.content[:200] if tutorial.content else 'None'}")
        print(f"Has image: {bool(tutorial.image)}")
        print(f"Author: {tutorial.author.username}")
        print("-" * 40)

if __name__ == '__main__':
    test_tutorial_content()