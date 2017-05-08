from django.db import models
from django.contrib.auth.models import User


class Ngo(models.Model):
    name = models.CharField(max_length=300)
    moderator = models.OneToOneField(User)
    address = models.CharField(max_length=500, default='Vadodara')
    contact_no = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default='Children')
    web_url = models.URLField(default='web link')
    email = models.EmailField(default='name@emample.com')
    logo = models.ImageField(upload_to='logos/', null=True)
    creation_date = models.DateTimeField(auto_now=True, blank=True)
    rating = models.IntegerField(default=0)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name

    def rate(self):
        self.rating += 1
        self.save()

    def get_live_id(self):
        return self.pk


class Happening(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True, blank=True)


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/')
    owner = models.ForeignKey(Ngo, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now=True, blank=True)


class HapComments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_on = models.ForeignKey(Happening, on_delete=models.CASCADE, related_name='comment_of')
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now=True, blank=True)
