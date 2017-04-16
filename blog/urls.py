from django.conf.urls import url
from django.core.urlresolvers import reverse

from .views import PostList, post_detail
urlpatterns = [
	url(r'^$', PostList.as_view(template_name='blog/post_list.html'), name='blog_post_list'),
	url(r'^(?P<year>\d{4})/'r'(?P<month>\d{1,2})/'r'(?P<slug>[\w\-]+)/$', post_detail, name='blog_post_detail'),
	]
