import os
import django
from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from typing import Any, Optional

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

# Explicit type annotations to fix Pyright 'Any' type warnings (after Django setup)
# Type ignore for "Any" types from Django settings
DEBUG: bool = settings.DEBUG  # type: ignore
MEDIA_URL: str = settings.MEDIA_URL  # type: ignore
MEDIA_ROOT: str = settings.MEDIA_ROOT  # type: ignore

def test_media_serving() -> None:
    print("DEBUG:", DEBUG)
    print("MEDIA_URL:", MEDIA_URL)
    print("MEDIA_ROOT:", MEDIA_ROOT)
    
    # Test if the media directory exists
    print("MEDIA_ROOT exists:", os.path.exists(MEDIA_ROOT))
    
    # Test if we can access a tutorial image
    try:
        from tech.models import Tutorial
        tutorial: Optional[Tutorial] = Tutorial.objects.first()
        if tutorial and tutorial.image:
            print("Tutorial image URL:", tutorial.image.url)
            print("Tutorial image path:", tutorial.image.path)
            print("Image file exists:", os.path.exists(tutorial.image.path))
            
            # Test if the URL mapping is correct
            # Type ignore for unknown member types
            if tutorial.image.url.startswith(MEDIA_URL):  # type: ignore
                # Type ignore for unknown member types
                relative_path: str = tutorial.image.url[len(MEDIA_URL):]  # type: ignore
                expected_path: str = os.path.join(MEDIA_ROOT, relative_path)
                print("Expected file path:", expected_path)
                # Type ignore for unknown member types
                print("Paths match:", expected_path == tutorial.image.path)  # type: ignore
        else:
            print("No tutorial with image found")
    except Exception as e:
        print("Error accessing tutorial image:", e)

if __name__ == '__main__':
    test_media_serving()