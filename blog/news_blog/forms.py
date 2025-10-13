from django import forms

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