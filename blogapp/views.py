from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import Article
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 6)
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
    category = Article.objects.values('category')
    empty_list = []
    for c in category:
        for tag in c['category'].split(','):
            empty_list.append(tag)
    tags = set(empty_list)
    return render(request, 'categories.html', {'tags': tags})
