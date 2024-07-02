from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()

    return render(request, 'app/home.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    return render(request, 'app/post_detail.html', {'post': post})


def post_create(request):
    return render(request, 'app/post_create.html')

def post_update(request):
    return render(request, 'app/post_update.html')

def post_delete(request):
    return render(request, 'app/post_delete.html')

def login_page(request):
    return render(request, 'app/login.html')

def sign_up(request):
    return render(request, 'app/sign_up.html')