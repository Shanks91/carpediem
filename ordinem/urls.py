from django.conf.urls import url
from ordinem import views


urlpatterns = [
    url(r'^ngo/$', views.ngolist, name='ngo_list'),
    url(r'^ngo/signup/$', views.createngo, name='ngo_signup'),
    url(r'^ngo/detail/(?P<pk>\d+)/$', views.ngoprofile, name='ngo_profile'),
    url(r'^ngo/detail/(?P<pk>\d+)/gallery/$', views.gallery_view, name='gallery'),
    url(r'^ngo/detail/(?P<pk>\d+)/like/$', views.ngo_like, name='ngo_like'),
    url(r'^ngo/detail/(?P<pk>\d+)/create/event/$', views.post_happening, name='post_happening'),
    url(r'^ngo/detail/(?P<npk>\d+)/follow/(?P<upk>\d+)/$', views.follow_ngo, name='follow_ngo'),
    url(r'^ngo/detail/(?P<pk>\d+)/create/gallery/$', views.post_gallery, name='post_gallery'),
    url(r'^ngo/detail/(?P<pk>\d+)/comment/$', views.post_comment, name='post_comment'),
]
