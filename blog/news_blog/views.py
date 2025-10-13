from django.shortcuts import render
from .forms import FeedbackForm

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
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
        form = FeedbackForm()
        return render(request, "feedback.html", {"form": form})
    
def article(request, id):
    return render(request, "article.html", {"id": id})