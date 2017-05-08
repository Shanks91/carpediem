from django.db import models
from django.contrib.auth.models import User


class Massage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_by")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_by")
    content = models.TextField()
    draft = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now=True)