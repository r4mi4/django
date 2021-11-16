from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def all_articles(request):
    all_articles = Article.publish.all()
    return render(request, 'blog/all_articles.html', {'all_articles': all_articles})


def article_detail(request, id, slug):
    # article_detail = Article.objects.get(id=id, slug=slug)
    article_detail = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/article_detail.html', {'article_detail': article_detail})
