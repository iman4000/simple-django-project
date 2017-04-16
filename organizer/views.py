#from django.http.response import HttpResponse
from .models import Tag, Startup
#from django.template import loader, RequestContext
from django.shortcuts import (get_object_or_404, render)

def startup_list(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_list.html', {'startup_list':startup})

def tag_list (request):
    return render(request,'organizer/tag_list.html', {'tag_list':Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag':tag})
