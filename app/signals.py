from django.db.models.signals import post_save
from django.dispatch import receiver
from app.models import File
from app.tasks import delete_file


@receiver(post_save, sender=File)
def set_deleting_timer(sender, instance, created, **kwargs):
    if created:
        delete_file.apply_async([instance.id], eta=instance.expires_at)
