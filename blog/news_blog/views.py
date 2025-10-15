from django.shortcuts import render, redirect
from . import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from .models import Article
from .forms import ArticleForm, CommentForm, CustomUserRegistrationForm
from django.contrib.auth import logout

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def feedback(request):
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            return render(request, 'feedback_success.html', {
                'name': name,
                'email': email,
                'message': message
            })
        return render(request, "feedback.html", {"form": form})
    else:
        form = forms.FeedbackForm()
        return render(request, "feedback.html", {"form": form})
    
def articles_list(request, category=None):
    articles = Article.objects.all()
    
    if category:
        valid_categories = [choice[0] for choice in Article.CATEGORY_CHOICES]
        if category not in valid_categories:
            return render(request, 'articles_invalid_category.html', {'category': category})
        articles = articles.filter(category=category)
    
    search_query = request.GET.get('search', '')
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) | 
            Q(text__icontains=search_query)
        )
    
    context = {
        'articles': articles,
        'category': category,
        'search_query': search_query,
        'category_choices': Article.CATEGORY_CHOICES,
    }
    return render(request, 'articles_list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()
    
    context = {
        'article': article,
        'comments': comments,
        'form': form,
    }
    return render(request, 'article_detail.html', context)

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles_list')
    else:
        form = ArticleForm()
    
    context = {'form': form}
    return render(request, 'article_create.html', context)

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if article.author != request.user:
        return redirect('articles_list')
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    
    context = {'form': form, 'article': article}
    return render(request, 'article_create.html', context)

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if article.author != request.user:
        return redirect('articles_list')
    
    if request.method == 'POST':
        article.delete()
        return redirect('articles_list')
    
    context = {'article': article}
    return render(request, 'article_delete.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    return redirect('home')