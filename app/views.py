from django.shortcuts import render
from .models import Post
from .forms import PostForm

def home(request):

    q = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=q)

    context = {
        'posts': posts,
        'q': q
    }

    return render(request, 'app/home.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post
    }

    return render(request, 'app/post_detail.html', context)


def post_create(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    context = {
        'form': form
    }

    return render(request, 'app/post_create.html', context)

def post_update(request):
    return render(request, 'app/post_update.html')

def post_delete(request, pk):

    post = Post.objects.get(id=pk)
    return render(request, 'app/post_delete.html', {'post': post})

def login_page(request):
    return render(request, 'app/login.html')

def sign_up(request):
    return render(request, 'app/sign_up.html')