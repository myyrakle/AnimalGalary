from django.db import models

# Create your models here.
class ImageFileName(models.Model):
    filename = models.TextField(max_length=255)

    def print(self):
        print('id:'+str(self.id)+', filename:'+self.filename)