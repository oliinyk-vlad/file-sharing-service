from django import forms

from app.models import File


class FileForm(forms.ModelForm):
    expires_at = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = File
        fields = "__all__"
