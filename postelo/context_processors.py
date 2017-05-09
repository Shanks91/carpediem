from .models import Message


def mail_processor(request):
    if request.user.is_authenticated():
        mail_drafts = Message.objects.filter(sender=request.user).filter(draft=True).count()
        mail_sent = Message.objects.filter(sender=request.user).filter(draft=False).count()
        mail_inbox = Message.objects.filter(recipient=request.user).filter(draft=False).count()
        mail_inbox_unread = Message.objects.filter(recipient=request.user).filter(draft=False).filter(is_read=False).count()
        return {
            'mail_drafts': mail_drafts,
            'mail_sent': mail_sent,
            'mail_inbox': mail_inbox,
            'mail_inbox_unread': mail_inbox_unread,
        }
    else:
        return {
            'mail_drafts': None,
            'mail_sent': None,
            'mail_inbox': None,
            'mail_inbox_unread': None,
        }
