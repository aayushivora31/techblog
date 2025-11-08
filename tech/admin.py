from django.contrib import admin
from .models import Tutorial, Article, Snippet
from typing import final

# Register your models here.

@admin.register(Tutorial)
@final
class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Article)
@final
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'tags')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Snippet)
@final
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'author', 'created_at')
    list_filter = ('language', 'created_at', 'author')
    search_fields = ('title', 'code')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)