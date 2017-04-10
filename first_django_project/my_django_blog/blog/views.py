#coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Article
from .forms import EditArcicle, SearchArticle

def index(request):
    if request.method == 'POST':
        form = SearchArticle(request.POST)
        title = form.data['title']
        articles = Article.objects.filter(title=title)
        return render(request, 'blog/index.html', {'articles': articles, 'form': form})

    pagenum = 2
    articles_list = Article.objects.all().order_by('-publish_time')
    paginator = Paginator(articles_list, pagenum)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    form = SearchArticle()
    return render(request, 'blog/index.html', {'articles': articles, 'form': form})

def each_blog(request, blog_id):
    article = get_object_or_404(Article, id=blog_id)
    return render(request, 'blog/blog.html', {'article': article})

def edit(request, blog_id):
    if request.method == 'POST':
        articles = Article.objects.all().order_by('-publish_time')
        form = EditArcicle(request.POST)

        title = form.data['title']
        content = form.data['content']

        if str(blog_id) == '0':
            Article.objects.create(title=title, content=content)
        else:
            arti = Article.objects.filter(id=blog_id)[0]
            arti.title = title
            arti.content = content
            arti.save()
        return HttpResponseRedirect('/')

    else:
        form = EditArcicle()
        return render(request, 'blog/edit_blog.html', {'form': form, 'blog_id': blog_id})

def delete(request, blog_id):
    blog = get_object_or_404(Article, pk=int(blog_id))
    blog.delete()
    return HttpResponseRedirect('/')
