from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils.text import Truncator
import textwrap
from django.http import Http404
from django.db import models

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html', {'posts': posts})

def read_blog(request, id):
    try:
        post = get_object_or_404(Post, pk=id)
        words = post.body.split()
        chunk_size = 300
        pages = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
        return render(request, 'blog.html', {'post': post, 'pages': pages})
    except Http404:
        # You can log this or render a custom 404 page
        return render(request, 'error_page.html', {'error': 'Blog not found'})
    except Exception as e:
        # Optional: Log the actual error for debugging
        print(f"Unexpected error: {e}")
        return render(request, 'error_page.html', {'error': 'Something went wrong'})
    
def view_blogs(request):
    posts = Post.objects.all()
    return render(request, 'view_blogs.html', {'posts': posts})

def post_blog(request):
    return render(request, 'post_blog.html')

def createNewBlog(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')

        Post.objects.create(title=title, body=content)
    
        return redirect('../view-blogs')

    else:
        return render(request, 'post_blog.html')

