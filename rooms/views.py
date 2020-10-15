from django.http import HttpResponse

def index(request):
    return HttpResponse("Hiiii")

def room(request, room_id):
    return HttpResponse("You are in room %s" % room_id)