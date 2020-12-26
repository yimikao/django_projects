from django.shortcuts import render
from .models import Post

# Create your views here.

def blog_list(request):

    posts = Post.objects.all()

    context = {
        'post_list': posts
    }

    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, id):

    one_post = Post.objects.get(id = id)

    context = {
        'one_post': one_post
    }

    return render(request, 'blog/blog_detail.html', context)
