from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def redirect_root(request):
	url_path = reverse('blog_post_list')
	return HttpResponseRedirect('/blog/')