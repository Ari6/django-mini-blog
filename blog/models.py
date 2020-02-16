from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Author(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Author'
        
    def __str__(self):
        return self.username
        
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Post(models.Model):
    title = models.CharField(max_length=200)
    posted_date = models.DateTimeField()
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.id:
            self.posted_date = timezone.now()
        return super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    comment_date = models.DateTimeField()
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.__str__() +  " Date: " + str(self.comment_date)

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.id:
            self.comment_date = timezone.now()
        return super(Comment, self).save(*args, **kwargs)