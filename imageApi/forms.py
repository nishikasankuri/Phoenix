# forms.py

from django import forms
from imageApi.models import UploadedImage


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']