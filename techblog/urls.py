"""
URL configuration for techblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from django.urls import URLPattern, URLResolver

# Type cast settings to explicit strings to satisfy type checker
DEBUG: bool = cast(bool, settings.DEBUG)
MEDIA_URL: str = cast(str, settings.MEDIA_URL)
MEDIA_ROOT: str = cast(str, settings.MEDIA_ROOT)

# Type annotations for URL patterns
urlpatterns: list[URLPattern | URLResolver] = [
    path('admin/', admin.site.urls),
    path('', include('tech.urls')),
]

# Serve media files during development
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)