from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post


def index(request):
    #posts = Post.objects.filter(date__lte=datetime.now())
    #posts = Post.objects.filter(content__icontains='zweiter')
    posts = Post.objects.filter(deleted=False)
    #posts = Post.objects.all()

    return render(request, 'blog/index.html', context={'posts': posts, 'now': datetime.now()})
