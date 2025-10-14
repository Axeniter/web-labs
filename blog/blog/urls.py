from django.urls import path
from news_blog import views

urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
    path("feedback/", views.feedback),

    path("create-article/", views.create_article),
    path("edit-article/", views.edit_article),
    path("delete-article/", views.delete_article),

    path("articles/", views.all_articles),
    path("articles/<str:category>/", views.articles_by_category),
    path("articles/<int:id>/", views.article_detail),

    path('register/', views.register),
    path('login/', views.custom_login),
    path('logout/', views.custom_logout),

    path("news/<int:id>", views.article)
]
