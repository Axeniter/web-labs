from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Имя',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
        }),
        error_messages={'required': 'Поле "Имя" обязательно для заполнения'}
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
        }),
        error_messages={
            'required': 'Поле "Email" обязательно для заполнения',
            'invalid': 'Введите корректный email адрес'
        }
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'rows': 5,
            'style': 'resize: vertical;'
        }),
        error_messages={'required': 'Поле "Сообщение" обязательно для заполнения'}
    )

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'text', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите содержимое статьи'}),
            'category': forms.Select(attrs={'class': 'form-control'})}
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите ваш комментарий'}),
        }

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})