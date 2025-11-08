import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techblog.settings')
django.setup()

from django.contrib.auth.models import User

def create_test_user():
    """Create a test user if one doesn't exist"""
    username = 'admin'
    password = 'admin123'
    
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists")
        return
    
    # Create the user
    user = User.objects.create_user(
        username=username,
        password=password,
        email='admin@example.com'
    )
    print(f"Created user '{username}' with password '{password}'")
    print("You can now log in to the dashboard with these credentials")

if __name__ == '__main__':
    create_test_user()