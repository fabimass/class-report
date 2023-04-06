from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from datetime import datetime
import requests

from .models import User, Sync, Repo


def index(request):

    repoOwner = "fabimass"
    repoName = "class-report"

    query_url = f"https://api.github.com/repos/{repoOwner}/{repoName}/branches"
    params = {
        "per_page": 100
    }
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    branches = requests.get(query_url, headers=headers, params=params).json()

    if Sync.objects.filter(id=1).exists():
        sync_date = Sync.objects.get(id=1).last_sync
    else:
        sync_date = "No data"

    if request.user.is_authenticated:
        return render(request, "submissions/index.html", {
            "students": branches,
            "sync_date": sync_date
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "submissions/login.html", {
                "message": "Invalid credentials"
            })
    else:
        return render(request, "submissions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "submissions/register.html", {
                "message": "Passwords must match"
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "submissions/register.html", {
                "message": "Username already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "submissions/register.html")


def sync_db(request):
    #sync_record = Sync(last_sync=datetime.now())
    #sync_record.save()

    return HttpResponseRedirect(reverse("index"))
