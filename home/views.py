from django.shortcuts import render
from .models import NewEvent,SuccessStory
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def home(request):
    eventlist = NewEvent.objects.all()
    storylist = SuccessStory.objects.all()
    
    events = Paginator(eventlist,2)
    stories = Paginator(storylist,3)
    page_number1 = request.GET.get('page1')
    try:
        event_obj = events.page(page_number1)
    except PageNotAnInteger:
        event_obj = events.page(1)
    except EmptyPage:
        event_obj = events.page(events.num_pages)


    page_number2 = request.GET.get('page2')
    try:
        story_obj = stories.page(page_number2)
    except PageNotAnInteger:
        story_obj = stories.page(1)
    except EmptyPage:
        story_obj = stories.page(stories.num_pages)
    

    context = {
        "events": event_obj,
        "stories": story_obj
        
    }

    return render(request,'index.html',context)