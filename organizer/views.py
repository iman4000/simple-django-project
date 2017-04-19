#from django.http.response import HttpResponse
from .models import Tag, Startup
#from django.template import loader, RequestContext
from django.shortcuts import (get_object_or_404, render, redirect)
from .forms import TagForm, StartupForm, NewsLinkForm
from django.views.generic import View
from .utils import ObjectCreateMixin

# def Tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             new_tag = form.save()
#             return redirect(new_tag)
#     else:
#         form = tag_form()
#         return render(request, 'organizer/tag_form.html', {'form':form})

class TagCreate (ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

class StartupCreate (ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'

class NewsLinkCreate (ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'

################################################################################################
def startup_list(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_list.html', {'startup_list':startup})

def tag_list (request):
    return render(request,'organizer/tag_list.html', {'tag_list':Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag':tag})
