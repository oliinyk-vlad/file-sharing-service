from __future__ import absolute_import, unicode_literals
from celery import task

from app.models import File


@task()
def delete_file(pk):
    File.objects.get(id=pk).delete()
