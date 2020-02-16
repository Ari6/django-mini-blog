from django import forms 
from .models import Author, Post, Comment

class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=200,  required=True)
    content = forms.CharField(widget=forms.Textarea)

class CommentCreateForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    comment = forms.CharField(widget=forms.Textarea)