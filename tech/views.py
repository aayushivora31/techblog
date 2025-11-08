from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from .models import Tutorial, Article, Snippet
from django.db.models import Q
import os
from typing import Optional

# Import forms for tutorial management
from django import forms

class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'description', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    """Landing page view with hero section and navigation"""
    return render(request, 'tech/home.html')

def tutorials(request: HttpRequest) -> HttpResponse:
    """Display coding tutorials with filtering options"""
    tutorials_list = Tutorial.objects.all().order_by('-created_at')
    
    # Filter by search query if provided
    query: str = request.GET.get('q', '')
    if query:
        tutorials_list = tutorials_list.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    
    # Pagination
    from django.core.paginator import Paginator
    paginator = Paginator(tutorials_list, 6)  # Show 6 tutorials per page
    page_number = request.GET.get('page')
    tutorials = paginator.get_page(page_number)
    
    context = {
        'tutorials': tutorials,
        'query': query,
    }
    return render(request, 'tech/tutorials.html', context)

def tutorial_detail(request: HttpRequest, tutorial_id: int) -> HttpResponse:
    """Display a single tutorial"""
    try:
        tutorial: Tutorial = get_object_or_404(Tutorial, id=tutorial_id)
        
        context = {
            'tutorial': tutorial,
        }
        return render(request, 'tech/tutorial_detail.html', context)
    except Exception as e:
        print(f"Error in tutorial_detail view: {e}")
        raise

def articles(request: HttpRequest) -> HttpResponse:
    """Display blog articles with search functionality"""
    articles_list = Article.objects.all().order_by('-created_at')
    
    # Filter by search query if provided
    query: str = request.GET.get('q', '')
    if query:
        articles_list = articles_list.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(tags__icontains=query)
        )
    
    # Pagination
    from django.core.paginator import Paginator
    paginator = Paginator(articles_list, 5)  # Show 5 articles per page
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    
    context = {
        'articles': articles,
        'query': query,
    }
    return render(request, 'tech/articles.html', context)

def article_detail(request: HttpRequest, article_id: int) -> HttpResponse:
    """Display a single article"""
    try:
        article: Article = get_object_or_404(Article, id=article_id)
        
        context = {
            'article': article,
        }
        return render(request, 'tech/article_detail.html', context)
    except Exception as e:
        print(f"Error in article_detail view: {e}")
        raise

def snippets(request: HttpRequest) -> HttpResponse:
    """Display code snippets with language filtering"""
    snippets_list = Snippet.objects.all().order_by('-created_at')
    
    # Filter by language if provided
    language: str = request.GET.get('language', '')
    if language:
        snippets_list = snippets_list.filter(language=language)
    
    # Pagination
    from django.core.paginator import Paginator
    paginator = Paginator(snippets_list, 10)  # Show 10 snippets per page
    page_number = request.GET.get('page')
    snippets = paginator.get_page(page_number)
    
    context = {
        'snippets': snippets,
        'language': language,
    }
    return render(request, 'tech/snippets.html', context)

def login_view(request: HttpRequest) -> HttpResponse:
    """Handle user login"""
    if request.method == 'POST':
        username: str = request.POST['username']
        password: str = request.POST['password']
        from django.contrib.auth.base_user import AbstractBaseUser
        from typing import Optional, cast
        user: Optional[AbstractBaseUser] = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'tech/login.html')

def signup_view(request: HttpRequest) -> HttpResponse:
    """Handle user registration"""
    from typing import Any
    form: UserCreationForm[Any]
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username: Optional[str] = form.cleaned_data.get('username')
            if username:
                messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'tech/signup.html', context)

def logout_view(request: HttpRequest) -> HttpResponse:
    """Handle user logout"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    """User dashboard with profile and activity"""
    # Get user's content
    user_tutorials = Tutorial.objects.filter(author=request.user).order_by('-created_at')
    user_articles = Article.objects.filter(author=request.user).order_by('-created_at')
    user_snippets = Snippet.objects.filter(author=request.user).order_by('-created_at')
    
    # Get counts for statistics
    tutorial_count = user_tutorials.count()
    article_count = user_articles.count()
    snippet_count = user_snippets.count()
    
    # Get recent items (last 5)
    recent_tutorials = user_tutorials[:5]
    recent_articles = user_articles[:5]
    recent_snippets = user_snippets[:5]
    
    context = {
        'user_tutorials': user_tutorials,
        'user_articles': user_articles,
        'user_snippets': user_snippets,
        'tutorial_count': tutorial_count,
        'article_count': article_count,
        'snippet_count': snippet_count,
        'recent_tutorials': recent_tutorials,
        'recent_articles': recent_articles,
        'recent_snippets': recent_snippets,
    }
    return render(request, 'tech/dashboard.html', context)

@login_required
def add_tutorial(request: HttpRequest) -> HttpResponse:
    """Add a new tutorial"""
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.author = request.user
            tutorial.save()
            messages.success(request, 'Tutorial created successfully!')
            return redirect('dashboard')
    else:
        form = TutorialForm()
    
    context = {
        'form': form,
    }
    return render(request, 'tech/add_tutorial.html', context)

@login_required
def edit_tutorial(request: HttpRequest, tutorial_id: int) -> HttpResponse:
    """Edit an existing tutorial"""
    tutorial = get_object_or_404(Tutorial, id=tutorial_id, author=request.user)
    
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES, instance=tutorial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tutorial updated successfully!')
            return redirect('dashboard')
    else:
        form = TutorialForm(instance=tutorial)
    
    context = {
        'form': form,
        'tutorial': tutorial,
    }
    return render(request, 'tech/edit_tutorial.html', context)

@login_required
def delete_tutorial(request: HttpRequest, tutorial_id: int) -> HttpResponse:
    """Delete a tutorial"""
    tutorial = get_object_or_404(Tutorial, id=tutorial_id, author=request.user)
    
    if request.method == 'POST':
        tutorial.delete()
        messages.success(request, 'Tutorial deleted successfully!')
        return redirect('dashboard')
    
    return redirect('dashboard')

@login_required
def add_article(request: HttpRequest) -> HttpResponse:
    """Add a new article"""
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Article created successfully!')
            return redirect('dashboard')
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'tech/add_article.html', context)

@login_required
def edit_article(request: HttpRequest, article_id: int) -> HttpResponse:
    """Edit an existing article"""
    article = get_object_or_404(Article, id=article_id, author=request.user)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article updated successfully!')
            return redirect('dashboard')
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'tech/edit_article.html', context)

@login_required
def delete_article(request: HttpRequest, article_id: int) -> HttpResponse:
    """Delete an article"""
    article = get_object_or_404(Article, id=article_id, author=request.user)
    
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article deleted successfully!')
        return redirect('dashboard')
    
    return redirect('dashboard')

def contact(request: HttpRequest) -> HttpResponse:
    """Handle contact form submission"""
    if request.method == 'POST':
        # We're not using these variables, just acknowledging the form submission
        _name: str = request.POST['name']
        _email: str = request.POST['email']
        _message: str = request.POST['message']
        
        # In a real application, you would save this to a database
        # or send an email to the site administrator
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'tech/contact.html')

def test_media(request: HttpRequest) -> HttpResponse:
    """Test view to check if media files are being served correctly"""
    from django.conf import settings
    
    # Get a tutorial with an image
    tutorial: Optional[Tutorial] = Tutorial.objects.first()
    
    context = {
        'debug': bool(getattr(settings, 'DEBUG', False)),
        'media_url': str(getattr(settings, 'MEDIA_URL', '')),
        'media_root': str(getattr(settings, 'MEDIA_ROOT', '')),
        'tutorial': tutorial,
        'file_exists': os.path.exists(tutorial.image.path) if tutorial and tutorial.image else False,
    }
    return render(request, 'tech/test_media.html', context)