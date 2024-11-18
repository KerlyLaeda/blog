from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (CreateView,
                                  DeleteView,
                                  DetailView,
                                  ListView,
                                  UpdateView)
from .models import Post


def index(request):
    context = {
        "posts": Post.objects.all(),  # reverse
    }
    # return render(request, "posts/index.html")  # open source frontend
    return render(request, "posts/index_test.html", context)  # my basic temporary template with no styles


class PostListView(ListView):
    model = Post

    # posts/post_list.html
    # <app>/<model>_<viewtype>.html
    template_name = "posts/index_test.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5


class UserPostListView(ListView):
    """Displays posts written by a particular user"""
    model = Post
    template_name = "posts/user_posts.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post
    # or without post_detail.html
    # template_name = "posts/index_test.html"
    # def get_context_data(self, **kwargs):
    #     context = {"posts": [self.get_object()]}
    #     return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # set attr success_url = homepage to redirect to hp after creating post
    # c delete


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # 403 if false


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # 403 if false


def about(request):
   # return render(request, "posts/about.html")
    return render(request, "posts/about_test.html", {"title": "About"})
