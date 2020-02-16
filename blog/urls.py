from django.urls import path, include
from .views import IndexView, PostListView, \
AuthorDetailView, PostDetailView, \
CommentDetailView, AuthorListView, PostCreateView, \
CommentCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blogs/', PostListView.as_view(), name='all-blog'),
    path('blogger/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('bloggers/', AuthorListView.as_view(), name='all-author'),
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/create', CommentCreateView.as_view(), name='comment-create'),
]