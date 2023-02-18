from django import forms
from .models import Vehicle, Comment
from django.db import models


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        # exclude = []


# class SearchForm(forms.ModelForm):
#     class Meta:
#         name = models.CharField(max_length=100)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

