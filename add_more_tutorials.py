import os
import django
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from typing import Optional, Any

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

from django.contrib.auth.models import User
from tech.models import Tutorial
from django.utils import timezone

def download_image(url: str) -> Optional[InMemoryUploadedFile]:
    """Download image from URL and return as InMemoryUploadedFile"""
    try:
        # Type ignore for unknown response type
        response: Any = requests.get(url, timeout=10)  # type: ignore
        if response.status_code == 200:
            image_io = BytesIO(response.content)
            image_io.seek(0)
            return InMemoryUploadedFile(
                image_io,
                None,
                f"tutorial_image_{int(timezone.now().timestamp())}.jpg",
                'image/jpeg',
                len(response.content),
                None
            )
    except Exception as e:
        print(f"Error downloading image: {e}")
    return None

def create_additional_tutorials() -> None:
    # Get or create admin user
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
    
    # Additional tutorials with images
    tutorials_data = [
        {
            'title': 'Advanced Python Techniques',
            'description': 'Master advanced Python concepts and techniques',
            'content': 'Learn about decorators, generators, context managers, and more...',
            'image_url': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=600&h=400'
        },
        {
            'title': 'React.js Fundamentals',
            'description': 'Build modern user interfaces with React',
            'content': 'Learn components, props, state, and the React ecosystem...',
            'image_url': 'https://images.unsplash.com/photo-1633356122102-3fe601e05bd2?auto=format&fit=crop&w=600&h=400'
        },
        {
            'title': 'Machine Learning with Python',
            'description': 'Introduction to ML concepts and scikit-learn',
            'content': 'Learn supervised and unsupervised learning techniques...',
            'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&h=400'
        },
        {
            'title': 'CSS Grid Layout',
            'description': 'Master modern CSS layout techniques',
            'content': 'Learn CSS Grid, Flexbox, and responsive design patterns...',
            'image_url': 'https://images.unsplash.com/photo-1633356122544-f1575931d73e?auto=format&fit=crop&w=600&h=400'
        },
        {
            'title': 'Node.js Backend Development',
            'description': 'Build scalable backend services with Node.js',
            'content': 'Learn Express, middleware, databases, and REST APIs...',
            'image_url': 'https://images.unsplash.com/photo-1635069989174-83099c9e36d7?auto=format&fit=crop&w=600&h=400'
        }
    ]
    
    added_count = 0
    for tut_data in tutorials_data:
        # Check if tutorial already exists
        # Type ignore for unknown filter return type
        if not Tutorial.objects.filter(title=tut_data['title']).exists():  # type: ignore
            # Create tutorial
            tutorial = Tutorial(
                title=tut_data['title'],
                description=tut_data['description'],
                content=tut_data['content'],
                author=user,
                created_at=timezone.now()
            )
            
            # Save tutorial first to create the instance
            # Type ignore for unknown save method
            tutorial.save()  # type: ignore
            
            # Try to download and save image
            image: Optional[InMemoryUploadedFile] = download_image(tut_data['image_url'])
            # Check if image is not None before trying to assign it
            if image is not None:
                tutorial.image = image
                # Type ignore for unknown save method
                tutorial.save(update_fields=['image'])  # type: ignore
            
            print(f"Created tutorial: {tut_data['title']}")
            added_count += 1
        else:
            print(f"Tutorial already exists: {tut_data['title']}")
    
    print(f"\nAdded {added_count} new tutorials!")
    # Type ignore for unknown count method
    total_tutorials = Tutorial.objects.count()  # type: ignore
    print(f"Total tutorials: {total_tutorials}")

if __name__ == '__main__':
    create_additional_tutorials()