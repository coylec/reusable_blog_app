from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^blog/$', views.post_list),
    # url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    # url(r'^blog/top', views.top_posts),
    # url(r'^post/new/$', views.new_post, name='new_post'),
    # url(r'^blog/(?P<id>\d+)/edit$', views.edit_post),
    url(r'^$', views.post_list, name="post_list"),
    url(r'^/$', views.post_list, name="post_list"),
    url(r'^/stuff/$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^post/$', views.new_post, name='new_post'),
]