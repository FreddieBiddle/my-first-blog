from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    """Creating model named Post; model.Model insures it's a Django model"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # models.ForeignKey is a link to another model 
    title = models.CharField(max_length=200) # models.CharField defines text with limited num of characters
    text = models.TextField() # models.TextField is for long text without a limit (this is for a blog!)
    created_date = models.DateTimeField(default=timezone.now) # models.DateTimeField is a date and time
    published_date = models.DateTimeField(blank=True, null=True) 

    # These functions are indented within the above class; they serve as methods for the class.
    def publish(self):
        """Defining a pulish function for the blog"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """We will get a text (string) with a Post title"""
        return self.title
