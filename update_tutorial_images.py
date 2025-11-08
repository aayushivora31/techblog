import os
import django
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from typing import TYPE_CHECKING, Optional, Any

# Add type checking imports
if TYPE_CHECKING:
    from tech.models import Tutorial

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
        if response.status_code == 200:  # type: ignore
            image_io = BytesIO(response.content)
            image_io.seek(0)
            return InMemoryUploadedFile(
                image_io,
                None,
                f"tutorial_image_{int(timezone.now().timestamp())}.jpg",
                'image/jpeg',
                len(response.content),  # type: ignore
                None
            )
    except Exception as e:
        print(f"Error downloading image: {e}")
    return None

def update_tutorial_images() -> None:
    # Image URLs for tutorials
    image_urls = [
        'https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=600&h=400',
        'https://images.unsplash.com/photo-1633356122102-3fe601e05bd2?auto=format&fit=crop&w=600&h=400',
        'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&h=400',
        'https://images.unsplash.com/photo-1635069989174-83099c9e36d7?auto=format&fit=crop&w=600&h=400',
        'https://images.unsplash.com/photo-1633356122544-f1575931d73e?auto=format&fit=crop&w=600&h=400',
        'https://images.unsplash.com/photo-1555066932-4365d14bab8c?auto=format&fit=crop&w=600&h=400',
        'https://images.unsplash.com/photo-1633356122545-f1575931d73e?auto=format&fit=crop&w=600&h=400',
        'https://images.unsplash.com/photo-1551288050-bebda4e38f71?auto=format&fit=crop&w=600&h=400'
    ]
    
    # Get all tutorials
    # Type ignore for unknown queryset type
    tutorials = Tutorial.objects.all()  # type: ignore
    updated_count = 0
    
    # Type the tutorial variable for better type checking
    tutorial: Tutorial
    # Type ignore for unknown enumerate type
    for i, tutorial in enumerate(tutorials):  # type: ignore
        # Only update tutorials that don't have images
        if not tutorial.image:
            image_url = image_urls[i % len(image_urls)]
            image = download_image(image_url)
            if image:
                # Assign the image directly to the field and save
                tutorial.image = image
                # Type ignore for unknown save method
                tutorial.save()  # type: ignore
                
                # Type ignore for unknown title attribute
                print(f"Updated image for tutorial: {tutorial.title}")  # type: ignore
                updated_count += 1
            else:
                # Type ignore for unknown title attribute
                print(f"Failed to download image for tutorial: {tutorial.title}")  # type: ignore
    
    print(f"\nUpdated images for {updated_count} tutorials!")

if __name__ == '__main__':
    update_tutorial_images()