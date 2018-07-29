from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    # Using 'auth.User' means that any user can author a post.
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    # The timezone used is specified by `TIME_ZONE` in settings.py.
    create_date = models.DateTimeField(default=timezone.now())
    # `blank=True` to allow saving posts without publishing.
    # `null=True` to allow saving posts with no publication date.
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200) # Choose a name - no need to login
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        # TODO: After approving a post, no redirection should occur.
        return reverse('post_list')

    def __str__(self):
        return self.text
