from django.contrib import admin
from .models import User, Repo, Commit, Branch

class BranchAdmin(admin.ModelAdmin):
    filter_horizontal = ("commits",)

admin.site.register(User)
admin.site.register(Repo)
admin.site.register(Commit)
admin.site.register(Branch, BranchAdmin)
