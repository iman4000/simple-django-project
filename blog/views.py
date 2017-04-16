from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Post

from django.views.decorators.http import require_http_methods


def post_list(request):
	return render(request, 'blog/post_list.html', {'post_list': post.objects.all()}) 
@require_http_methods(['HEAD', 'GET'])
def post_detail(request, year, month, slug):
	post =get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
	return render(request, 'blog/post_detail.html', {'post':post})
# Create your views here.
class PostList (View):
	
	template_name = 'blog/post_list.html'
	
	def get (self, request):
		return render(request, self.template_name, {'post_list': Post.objects.all()})