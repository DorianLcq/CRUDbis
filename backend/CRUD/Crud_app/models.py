from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, help_text='Title of your inspiration.')
    message = models.TextField(help_text="Be imaginative...")
    date = models.DateField(help_text= 'Publication date', default=datetime.date.today)
 
    def __str__(self):
        return self.title,self.date