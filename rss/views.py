from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import PostSerializers
from .models import Url, PostFromUrl
from .forms import FormUrl
import feedparser


class PostViewSet(viewsets.ModelViewSet):
    queryset = PostFromUrl.objects.all()
    serializer_class = PostSerializers


def index(request):
    if request.method == "POST":
        form = FormUrl(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("./news", pk=post.pk)
    else:
        form = FormUrl()
    return render(request, 'index.html', {'form': form})


def news(request):
    url = Url.objects.all().order_by("-pk")[0]

    feed = feedparser.parse(url.url)
    news_from = feed["channel"]["title"]
    for item in feed["items"]:
        title = item['title']
        date = item['published']
        link = item['link']
        if 'media_content' in item:
            img = item.media_content[0]["url"]
        else:
            img = None
        temp = PostFromUrl.objects.get_or_create(title=title, date=date, link=link, img=img)

    news = PostFromUrl.objects.all().distinct()[:url.limit]
    return render(request, 'news.html', {'title': news_from, 'news': news})
