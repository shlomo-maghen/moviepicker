from django.shortcuts import get_list_or_404, render

from .models import Suggestion


def home(request):
    return render(request, 'rooms/home.html')


def new_room(request):
    # create a new room and redirect to it
    return render(request, 'rooms/home.html')


def room(request, room_id):
    context = {
        'suggestions': get_list_or_404(Suggestion.objects.filter(room_id=room_id)),
        'room_id': room_id,
    }
    return render(request, 'rooms/room.html', context)
