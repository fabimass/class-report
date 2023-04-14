from .models import Sync

def get_sync_date():
    sync_data = Sync.objects.all()
    if sync_data.count() > 0:
        return sync_data[0].last_sync
    else:
        return "No data"
    

def process_branches(branches, commits):
    processedBranches = []
    for branch in branches:
        processedCommits = []
        
        for commit in commits:
            processedCommits.append({
                "name": commit.name,
                "submitted": commit.is_submitted(branch)
            })

        processedBranches.append({
            "name": branch.name,
            "commits": processedCommits,
            "percentage": branch.commits.all().count
        })
    return processedBranches
