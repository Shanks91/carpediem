from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writen_by")
    title = models.CharField(max_length=400)
    content = models.TextField()
    pic = models.ImageField(upload_to='/blog/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def publish_article(self):
        self.publish = True
        self.save()

    def get_article_id(self):
        return self.id


class BlogComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_on = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)



