from app.models import ImageFileName
import os

for e in os.listdir('static/image'):
    ImageFileName(filename=e).save()