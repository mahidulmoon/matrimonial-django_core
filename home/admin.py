from django.contrib import admin
from .models import SuccessStory,NewEvent
# Register your models here.

class ShowSuccessStory(admin.ModelAdmin):
    list_display = ('story_name','date')


class ShowNewEvent(admin.ModelAdmin):
    list_display = ('eventname','date')


admin.site.register(SuccessStory,ShowSuccessStory)
admin.site.register(NewEvent,ShowNewEvent)