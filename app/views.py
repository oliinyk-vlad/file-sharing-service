from django.views.generic import CreateView, DetailView
from django.urls import reverse

from app.models import File
from app.mixins import AjaxableResponseMixin


class FileUpload(AjaxableResponseMixin, CreateView):
    template_name = 'index.html'
    model = File
    fields = "__all__"

    def get_success_url(self):
        return reverse('file-detail', args=[str(self.object.id)])


class FileDetailView(DetailView):
    template_name = 'file_detail.html'
    model = File
