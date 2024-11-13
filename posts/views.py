from django.shortcuts import render
from .models import Post


dummy = [
    {
        "author": "ferogerg",
        "title": "jijirjirgjri",
        "content": "dhfgifjorfjof0",
        "date_posted": "11/4/2068"
    },
    {
        "author": "wgthtrhtg",
        "title": "gtrhrhtyjy",
        "content": "ghtjtyuj",
        "date_posted": "15/8/2069"
    }]


def index(request):
    context = {
        "posts": Post.objects.all(),  # reverse
    }
    # return render(request, "posts/index.html")
    return render(request, "posts/index_test.html", context)


def about(request):
   # return render(request, "posts/about.html")
    return render(request, "posts/about_test.html", {"title": "About"})
