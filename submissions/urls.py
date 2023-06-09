from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:repo_owner>/<str:repo_name>", views.submissions, name="submissions"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("sync", views.sync_db, name="sync")
]