from django.urls import path
from django.contrib.auth import views as auth_views
from news_blog import views

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("feedback/", views.feedback, name='feedback'),

    path('create-article/', views.create_article, name='create_article'),
    path('edit-article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete-article/<int:article_id>/', views.delete_article, name='delete_article'),

    path('articles/', views.articles_list, name='articles_list'),
    path('articles/<str:category>/', views.articles_list, name='articles_by_category'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
