from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'JonF',
        'title': 'blog post 1',
        'content': 'Fist Instagram post',
        'date_posted': 'March 4, 2019'
    },
    {
        'author': 'ChaiG',
        'title': 'blog post 2',
        'content': 'Fist Instagram post',
        'date_posted': 'March 3, 2019'


    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'instagram/home.html', context)


def about(request):
    return render(request, 'instagram/about.html', {'title': 'About'})

