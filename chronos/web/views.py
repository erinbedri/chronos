from django.shortcuts import render
from chronos.posts.models import Post


def show_homepage(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'web/homepage.html', context)












