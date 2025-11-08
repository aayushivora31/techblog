from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('tutorials/<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
    path('articles/', views.articles, name='articles'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('snippets/', views.snippets, name='snippets'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add-tutorial/', views.add_tutorial, name='add_tutorial'),
    path('dashboard/edit-tutorial/<int:tutorial_id>/', views.edit_tutorial, name='edit_tutorial'),
    path('dashboard/delete-tutorial/<int:tutorial_id>/', views.delete_tutorial, name='delete_tutorial'),
    path('dashboard/add-article/', views.add_article, name='add_article'),
    path('dashboard/edit-article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('dashboard/delete-article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('contact/', views.contact, name='contact'),
    path('test-media/', views.test_media, name='test_media'),
]