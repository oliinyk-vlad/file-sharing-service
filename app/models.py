from django.db import models

from django.utils import timezone

from datetime import timedelta


class File(models.Model):
    source = models.FileField()
    expires_at = models.DateTimeField(help_text="Format: 2020-07-25 00:00")

    @property
    def time_left(self):
        duration = self.expires_at - timezone.now()
        return duration - timedelta(microseconds=duration.microseconds)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('file-detail', args=[str(self.id)])
