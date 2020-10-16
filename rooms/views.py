from django.shortcuts import get_object_or_404, render

from .models import Room, Suggestion


def home(request):
    return render(request, 'rooms/home.html')


def new_room(request):
    # create a new room and redirect to it
    return render(request, 'rooms/home.html')


def room(request, room_id):
    get_object_or_404(Room, pk=room_id)
    context = {
        'suggestions': Suggestion.objects.filter(room_id=room_id),
        'room_id': room_id,
    }
    return render(request, 'rooms/room.html', context)
