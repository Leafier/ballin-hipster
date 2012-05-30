# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from artifact.models import *

def front(request):
    cat_list = Category.objects.all()[:5]
    return render_to_response('index.html', {'cat_list': cat_list})

def cat(request, catid):
    cat_list = Category.objects.all()[:5]
    cat = get_object_or_404(Category, pk=catid)
    a_list = Artifact.objects.get(category=catid)
    return render_to_response('cat.html', {'cat_list': cat_list, 'cat': cat, 'a_list': a_list})
