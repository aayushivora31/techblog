from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.db.models.fields import CharField, TextField, DateTimeField
    from django.db.models.fields.files import ImageFieldFile, ImageField
    from django.db.models.fields.related import ForeignKey
    from django.db.models.fields.files import ImageField as ImageFieldType

class Tutorial(models.Model):
    title: 'CharField[str, str]' = models.CharField(max_length=200)
    description: 'TextField[str, str]' = models.TextField()
    content: 'TextField[str, str]' = models.TextField()
    image: 'ImageField | None' = models.ImageField(upload_to='tutorials/', blank=True, null=True)
    created_at: 'DateTimeField[datetime, datetime]' = models.DateTimeField(default=timezone.now)
    updated_at: 'DateTimeField[datetime, datetime]' = models.DateTimeField(auto_now=True)
    author: 'ForeignKey[User, User]' = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tutorial'
        verbose_name_plural = 'Tutorials'

class Article(models.Model):
    title: 'CharField[str, str]' = models.CharField(max_length=200)
    content: 'TextField[str, str]' = models.TextField()
    author: 'ForeignKey[User, User]' = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at: 'DateTimeField[datetime, datetime]' = models.DateTimeField(default=timezone.now)
    updated_at: 'DateTimeField[datetime, datetime]' = models.DateTimeField(auto_now=True)
    tags: 'CharField[str, str]' = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Snippet(models.Model):
    LANGUAGE_CHOICES = [
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('js', 'JavaScript'),
        ('python', 'Python'),
        ('django', 'Django'),
    ]
    
    title: 'CharField[str, str]' = models.CharField(max_length=200)
    code: 'TextField[str, str]' = models.TextField()
    language: 'CharField[str, str]' = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    created_at: 'DateTimeField[datetime, datetime]' = models.DateTimeField(default=timezone.now)
    author: 'ForeignKey[User, User]' = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Snippet'
        verbose_name_plural = 'Snippets'