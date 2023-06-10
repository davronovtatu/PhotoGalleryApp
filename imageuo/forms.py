from django import forms
from .models import Photo,Category


class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields='__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']