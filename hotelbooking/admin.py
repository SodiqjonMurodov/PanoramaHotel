from django.contrib import admin
from . import models
from django.db.models import QuerySet


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'country', 'email', 'check_in', 'check_out']
    list_display_links = ['firstname', 'lastname', 'country', 'email']
    ordering = ['firstname', 'lastname']
    list_per_page = 25


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['room_name', 'price', 'max_persona', 'beds', 'room_size', 'smoking', 'mini_bar']
    ordering = ['room_name']
    list_per_page = 25


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'room_type_id', 'user_id', 'bron']
    list_display_links = ['room_number', 'room_type_id']
    ordering = ['room_number']
    list_per_page = 25
    actions = ['set_empty_room']

    @admin.action(description='Освободить комнату')
    def set_empty_room(self, request, qs: QuerySet):
        qs.update(user_id=None, bron=False)


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'room_id', 'count']
    list_display_links = ['user_id', 'room_id']
    ordering = ['user_id', 'room_id']
    list_per_page = 25


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'cardname', 'cardnumber', 'expiration', 'cvv_code', 'total']
    list_display_links = ['user_id', 'cardname']
    ordering = ['user_id', 'cardname']
    list_per_page = 25


@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'phone', 'message']
    ordering = ['fullname']
    list_per_page = 25
