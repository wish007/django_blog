from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import Article
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def archives(request):
    post_list = Article.objects.values('id', 'title', 'category', 'publish_time')
    return render(request, 'archives.html', {'post_list' : post_list})

def categories(request):
    post_list = Article.objects.values('category')
    return render(request, 'categories.html', {'post_list' : post_list})
