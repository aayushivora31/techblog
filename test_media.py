import os
import django
from django.conf import settings
from typing import Any, Optional

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

def test_media_config() -> None:
    # Type ignore for "Any" types from Django settings
    print("BASE_DIR:", settings.BASE_DIR)  # type: ignore
    print("MEDIA_URL:", settings.MEDIA_URL)  # type: ignore
    print("MEDIA_ROOT:", settings.MEDIA_ROOT)  # type: ignore
    print("DEBUG:", settings.DEBUG)  # type: ignore
    
    # Test if MEDIA_ROOT directory exists
    # Type ignore for "Any" types from Django settings
    print("MEDIA_ROOT exists:", os.path.exists(settings.MEDIA_ROOT))  # type: ignore
    
    # Test if we can access a tutorial image
    try:
        from tech.models import Tutorial
        tutorial: Optional[Tutorial] = Tutorial.objects.first()
        if tutorial and tutorial.image:
            print("Tutorial image URL:", tutorial.image.url)
            print("Tutorial image path:", tutorial.image.path)
            print("Image file exists:", os.path.exists(tutorial.image.path))
        else:
            print("No tutorial with image found")
    except Exception as e:
        print("Error accessing tutorial image:", e)

if __name__ == '__main__':
    test_media_config()