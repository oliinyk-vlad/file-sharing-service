from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from app.models import File
from app.tasks import delete_file

import os


@receiver(post_save, sender=File)
def set_deleting_timer(sender, instance, created, **kwargs):
    if created:
        delete_file.apply_async([instance.id], eta=instance.expires_at)


@receiver(post_delete, sender=File)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.source:
        if os.path.isfile(instance.source.path):
            os.remove(instance.source.path)
