from django import forms
from .models import PhotoPost

class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPost
        fields = [ 'category', 'title', 'comment', 'image1', 'image2']
