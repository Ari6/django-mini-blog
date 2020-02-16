from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Post, Comment
# Register your models here.

admin.site.register(Author, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
