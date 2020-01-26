from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ImageFileName

def get_random_image_filename():
    return ImageFileName.objects.order_by('?').first().filename

# render random picture
def index(request):
    template = loader.get_template('index.html')
    
    context = {
        'image_path': '/static/image/'+get_random_image_filename()
    }

    return HttpResponse(template.render(context, request))

# ajax random picture
def get_random_image_filepath(request):
    return HttpResponse('/static/image/'+get_random_image_filename())


def order_by_latest(request):
    return HttpResponse('')

def render_login_form(request):
    template = loader.get_template('login_form.html')
    context = {}
    return HttpResponse(template.render(context, request))