



from django.db import models

# Our Imports
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import random

class EventPost(models.Model):
    title          = models.CharField(max_length=50,null=False,blank=False)
    description    = models.TextField(max_length=7000,null=True,blank=True)
    slug           = models.SlugField(unique=True,auto_created=True)
    start_time     = models.DateTimeField()
    end_time       = models.DateTimeField()
    attendees      = models.IntegerField(default=10)
    private        = models.BooleanField(default=False)
    organizer 	   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    invited_user   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = "invited_user")
    attending_users= models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = "attending_user")


    def __str__(self):
        return self.title


def pre_save_event_post_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        rand = random.randint(1,1000000000)
        instance.slug = slugify(instance.title + "-" + str(rand))

pre_save.connect(pre_save_event_post_receiever, sender=EventPost)