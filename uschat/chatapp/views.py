from django.shortcuts import render
from .models import Room, Message

# Create your views here.
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def room(request,slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    return render(request, 'room.html', {'room': room, 'messages': messages, 'slug':slug})