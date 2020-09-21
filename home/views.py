from django.shortcuts import render
from .models import NewEvent,SuccessStory
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    eventlist = NewEvent.objects.all()
    storylist = SuccessStory.objects.all()
    
    events = Paginator(eventlist,3)
    stories = Paginator(storylist,2)
    page_number1 = request.GET.get('page1')
    event_obj = events.get_page(page_number1)
    page_number2 = request.GET.get('page2')
    story_obj = stories.get_page(page_number2)

    context = {
        "events": event_obj,
        "stories": story_obj,
        "eventpage": range(events.num_pages+1)
    }

    return render(request,'index.html',context)