from django.shortcuts import render, redirect, get_object_or_404
from .models import Article


# Create your views here.

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    # 아니라면 POST 일경우 사용자 데이터 받아서 article 생성
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article()
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)
    #만약 GET 요청으로 들어오면 HTML 페이지 rendering
    else:
        return render(request, 'articles/create.html')
        


def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}

    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk) 


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:index')
    else:
        return render(request, 'articles/update.html', {'article': article})
