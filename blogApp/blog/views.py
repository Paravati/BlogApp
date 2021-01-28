from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # po 3 posty na każdej stronie
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts.paginator.page(1)  # jezeli zmienna page nie jest l.calkowita to pobierana jest pierwsza strona wynikow
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # jezeli zmienna page ma wartosc wieksza niz nr ostatniej strony wynikow to pobierana jest ostatnia strona wynikow
    # posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request,year, month,day, post):
    post = get_object_or_404(Post, slug=post, status='publish', publish__year=year, publish__month=month, publish__day=day)
    return render(request,'blog/post/detail.html', {'post': post})