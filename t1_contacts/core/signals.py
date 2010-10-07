from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.models import Log

def delete_callback(sender, instance, signal, *args, **kwargs):
    Log.content="object '%s' is deleted" % instance
    Log.save()
    
def save_callback(sender, instance, signal, *args, **kwargs):
    Log.content="object '%s' is created" % instance
    if ‘created’ not in kwargs:
        if not kwargs['created']:
            Log.content="object '%s' is edited" % instance
    Log.save()
    
post_save(save_callback)
post_delete(delete_callback)
