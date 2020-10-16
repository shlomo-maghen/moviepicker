from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:room_id>/', views.room, name="room"),
    path('create/', views.new_room, name="create")
]