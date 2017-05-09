from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^inbox/$', views.message_index, name='message_inbox'),
    url(r'^drafts/$', views.message_drafts, name='message_drafts'),
    url(r'^sent/$', views.message_sent, name='message_sent'),
    url(r'^compose/$', views.message_create, name='message_compose'),
    url(r'^inbox/message/(?P<pk>\d+)/$', views.message_detail, name='message_detail'),
    url(r'^inbox/message/(?P<pk>\d+)/delete/$', views.message_delete, name='message_delete'),
]
