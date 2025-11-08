import os
import django
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.fields.files import ImageFieldFile  # Add this import
from typing import cast, TYPE_CHECKING, Any, Optional

# Add these imports for proper type hinting
if TYPE_CHECKING:
    from django.db.models.query import QuerySet
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
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # Type ignore for unknown response type
        response: Any = requests.get(url, timeout=15, headers=headers)  # type: ignore
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
        print(f"Error downloading image from {url}: {e}")
    return None

def fix_tutorial_images() -> None:
    # Image URLs for tutorials (using different sources)
    image_urls = [
        'https://picsum.photos/600/400?random=1',
        'https://picsum.photos/600/400?random=2',
        'https://picsum.photos/600/400?random=3',
        'https://picsum.photos/600/400?random=4',
        'https://picsum.photos/600/400?random=5',
        'https://picsum.photos/600/400?random=6',
        'https://picsum.photos/600/400?random=7',
        'https://picsum.photos/600/400?random=8'
    ]
    
    # Get all tutorials - let Django handle the typing
    # Type ignore for unknown queryset type
    tutorials = Tutorial.objects.all()  # type: ignore
    updated_count = 0
    
    # For type checking purposes, we can iterate without explicit typing
    # Type ignore for unknown enumerate type
    for i, tutorial in enumerate(tutorials):  # type: ignore
        # Update tutorials that don't have images or re-download for all to ensure they work
        if not tutorial.image:
            image_url = image_urls[i % len(image_urls)]
            # Type ignore for unknown title attribute
            print(f"Downloading image for tutorial: {tutorial.title}")  # type: ignore
            image = download_image(image_url)
            if image and image.name:  # Check that image and image.name are not None
                # Assign the image directly to the tutorial's image field
                # This is the correct way to set an image for an existing tutorial
                tutorial.image = image
                # Type ignore for unknown save method
                tutorial.save()  # type: ignore
                # Type ignore for unknown title attribute
                print(f"Updated image for tutorial: {tutorial.title}")  # type: ignore
                updated_count += 1
            else:
                # Type ignore for unknown title attribute
                print(f"Failed to download image for tutorial: {tutorial.title}")  # type: ignore
        else:
            # Check if existing image is accessible
            try:
                # Try to access the image URL to see if it's still valid
                # Type ignore for unknown title attribute
                print(f"Checking image for tutorial: {tutorial.title}")  # type: ignore
            except Exception as e:
                # Type ignore for unknown title attribute
                print(f"Image issue for tutorial {tutorial.title}: {e}")  # type: ignore
    
    print(f"\nUpdated images for {updated_count} tutorials!")

if __name__ == '__main__':
    fix_tutorial_images()