from django import forms 
from .models import Author, Post, Comment
from django.contrib import admin
from django.contrib.auth import forms as auth_forms

class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=200,  required=True)
    content = forms.CharField(widget=forms.Textarea)

class CommentCreateForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    comment = forms.CharField(widget=forms.Textarea)

class AuthorCreateForm(auth_forms.UserCreationForm):
    username = forms.CharField(max_length=10, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Author
        fields = ('username', 'password1', 'password2', 'bio')

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        author = super(AuthorCreateForm, self).save(commit=False)
        author.set_password(self.cleaned_data["password2"])
        if commit:
            author.save()
        return author