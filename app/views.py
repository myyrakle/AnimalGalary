from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ImageFileName

def get_random_image_filename():
    return ImageFileName.objects.order_by('?').first().filename

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    
    context = {
        'image_path': '/static/image/'+get_random_image_filename()
    }

    return HttpResponse(template.render(context, request))

def get_random_image_filepath(request):
    return HttpResponse('/static/image/'+get_random_image_filename())