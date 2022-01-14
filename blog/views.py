from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    # The 3rd argument will be passed into the urls
    
# blog -> templates -> blog -> template.html
