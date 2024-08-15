from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('rooms', views.rooms_page, name='rooms_page'),
    path('gallery', views.gallery_page, name='gallery_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('booking', views.booking_page, name='booking_page'),
    path('booking/select-room', views.booking_room_page, name='select_room'),
    path('booking/select-room/payment', views.payment_page, name='payment'),
]