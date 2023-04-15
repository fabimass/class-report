from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from datetime import datetime
import requests

from .models import User, Sync, Repo, Commit, Branch
from .utils import get_sync_date, process_branches


def index(request):

    if request.user.is_authenticated:

        if request.user.is_superuser:
            repos = Repo.objects.all()
        else:
            repo_list = Branch.objects.filter(name=request.user.username).values_list('repo', flat=True)
            repos = Repo.objects.filter(id__in=repo_list)

        return render(request, "submissions/index.html", {
            "repos": repos,
            "sync_date": get_sync_date()
        })
    else:
        return HttpResponseRedirect(reverse("login"))
    

def submissions(request, repo_owner, repo_name):

    if request.user.is_authenticated:

        repo = Repo.objects.get(owner=repo_owner, name=repo_name)
        commits = repo.commits.all()

        if request.user.is_superuser:
            branches = repo.branches.all()
        else:
            branches = repo.branches.filter(name=request.user.username)

        branches = process_branches(branches, commits)

        return render(request, "submissions/submissions.html", {
            "commits": repo.commits.all(),
            "branches": branches,
            "repo": repo,
            "sync_date": get_sync_date()
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
    
    if request.method == "POST":
        
        # Update branches table
        Branch.objects.all().delete()
        
        for repo in Repo.objects.all():
            repoOwner = repo.owner
            repoName = repo.name
            params = {
                "per_page": 100
            }
            if repo.private:
                headers = {
                    "Accept": "application/vnd.github.v3+json",
                    "Authorization": f"Bearer {repo.token}"
                }
            else:
                headers = {
                    "Accept": "application/vnd.github.v3+json"
                }

            # Pull all the branches for the given repo
            branches_url = f"https://api.github.com/repos/{repoOwner}/{repoName}/branches"
            branches = requests.get(branches_url, headers=headers, params=params).json()

            for branch in branches:
                # Avoid main branch
                if branch["name"] != "main":
                    Branch(name=branch["name"], repo=repo).save()

                    # Pull all the commits
                    commits_url = f"https://api.github.com/repos/{repoOwner}/{repoName}/commits?sha={branch['name']}"
                    commits = requests.get(commits_url, headers=headers, params=params).json()
                    
                    # Compare the existing commits with the ones registered in the commits table
                    for commit in commits:
                        if Commit.objects.filter(name=commit["commit"]["message"], repo=repo).exists():
                            Branch.objects.get(name=branch["name"], repo=repo).commits.add(Commit.objects.get(name=commit["commit"]["message"], repo=repo)) 

        # Update last sync record
        Sync.objects.all().delete()
        sync_record = Sync(last_sync=datetime.now())
        sync_record.save()

    if request.method == "GET":
        sync_record = Sync.objects.all()[0]

    return(JsonResponse({
        "last_sync": sync_record.last_sync
        }, 
        status=200))
