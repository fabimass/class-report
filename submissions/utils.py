from .models import Sync

def get_sync_date():
    sync_data = Sync.objects.all()
    if sync_data.count() > 0:
        return sync_data[0].last_sync
    else:
        return "No data"
