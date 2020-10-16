from django.contrib import admin

from .models import User, Movie, Room, Suggestion

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Suggestion)
