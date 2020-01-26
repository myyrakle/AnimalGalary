from app.models import ImageFileName
import os

def init():
    for e in os.listdir('static/image'):
        ImageFileName(filename=e).save()