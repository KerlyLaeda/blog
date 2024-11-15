<<<<<<< HEAD
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"successfully registered user {username}")
            #return redirect("posts-index")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register_test.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile_test.html")
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> a3d12e0c42f094e74ef03cbfbc1150cb0385b89a
