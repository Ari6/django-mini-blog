import datetime

from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, \
PermissionRequiredMixin
from .models import Author, Post, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PostCreateForm, AuthorCreateForm

from extra_views import CreateWithInlinesView, InlineFormSet
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post-list.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['posts'] = self.model.objects.all()
        return context

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'authors'

class AuthorDetailView(generic.DetailView):
    model = Author
    
    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        self.author = get_object_or_404(Author, id=self.kwargs['pk'])
        post = Post
        context['posts'] = post.objects.filter(author=self.author)
        return context

class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        self.post = get_object_or_404(Post, id=self.kwargs['pk'])
        comment = Comment
        context['comments'] = comment.objects.filter(post=self.post)
        return context
    class Meta:
        model = Post
        fields = '__all__'

class CommentDetailView(generic.DetailView):
    model = Comment

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['title', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['pk'])
        return super().form_valid(form)

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    #fields = ['username', 'password1', 'password2', 'bio']
    template_name = 'blog/author_create.html'
