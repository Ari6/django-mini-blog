from django.urls import path, include
from .views import IndexView, PostListView, \
AuthorDetailView, PostDetailView, \
CommentDetailView, AuthorListView, PostCreateView, \
CommentCreateView, AuthorCreateView, AuthorEditView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blogs/', PostListView.as_view(), name='all-blog'),
    path('blogger/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('blogger/create', AuthorCreateView.as_view(), name='author-create'),
    path('bloggers/', AuthorListView.as_view(), name='all-author'),
    path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/create', CommentCreateView.as_view(), name='comment-create'),
    path('blogger/<int:pk>/edit', AuthorEditView.as_view(), name='author-edit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)