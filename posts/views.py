from django.shortcuts import render
from .models import Post


dummy = [
    {
        "author": "ferogerg",
        "title": "jijirjirgjri",
        "body": "dhfgifjorfjof0",
        "date_posted": "11/4/2068"
    },
    {
        "author": "wgthtrhtg",
        "title": "gtrhrhtyjy",
        "body": "ghtjtyuj",
        "date_posted": "15/8/2069"
    }
]


def index(request):
    context = {
        # "posts": Post.objects.all()
        "posts": dummy
    }
    return render(request, "posts/index.html", context)
