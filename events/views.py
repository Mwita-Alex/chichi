from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event

# Create your views here.

def event(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request,'events/events.html',context)


def singleevent(request,event_id):
    event = get_object_or_404(Event,pk=event_id)
    context = {'event':event}
    return render(request,'events/singleevent.html',context)