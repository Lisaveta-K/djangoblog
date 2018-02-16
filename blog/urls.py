from django.conf.urls import url
from . import views
from blog import views as blog_views
from django.conf.urls import handler404, handler500

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

handler404 = blog_views.error_404
handler500 = blog_views.error_500