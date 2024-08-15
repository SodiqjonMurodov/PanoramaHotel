from django.shortcuts import render
from .models import RoomType, Feedback, Client, Payment, Room, Booking
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm, ClientForm, PaymentForm
from django.http import HttpResponseRedirect, Http404


def main_page(request):
    return render(request, 'hotelbooking/main.html')


def rooms_page(request):
    room_typies_list = RoomType.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(room_typies_list, 6)
    try:
        room_typies = paginator.page(page)
    except PageNotAnInteger:
        room_typies = paginator.page(1)
    except EmptyPage:
        room_typies = paginator.page(paginator.num_pages)

    return render(request, 'hotelbooking/rooms.html', {
        'room_typies': room_typies
    })


def gallery_page(request):
    return render(request, 'hotelbooking/gallery.html')


def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Feedback(
                fullname=form.cleaned_data['fullname'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],
            )
            contact.save()
            return HttpResponseRedirect("/contact")
    else:
        form = ContactForm()

    return render(request, 'hotelbooking/contact.html', context={'form': form})


def booking_page(request):
    if request.method == "POST":
        clientform = ClientForm(request.POST)
        if clientform.is_valid():
            client_data = Client(
                firstname=clientform.cleaned_data['firstname'],
                lastname=clientform.cleaned_data['lastname'],
                email=clientform.cleaned_data['email'],
                country=clientform.cleaned_data['country'],
                phone=clientform.cleaned_data['phone'],
                adults=clientform.cleaned_data['adults'],
                children=clientform.cleaned_data['children'],
                check_in=clientform.cleaned_data['check_in'],
                check_out=clientform.cleaned_data['check_out'],
            )
            if client_data.check_out <= client_data.check_in:
                error_message = "Дата выезда не должна быть меньше чем даты заезда!"
            elif client_data.adults == 0:
                error_message = "Должен быть хотя бы 1 человек!"
            else:
                client_data.save()
                request.session['client_id'] = client_data.id
                return HttpResponseRedirect("/booking/select-room")
    else:
        clientform = ClientForm()
        error_message = False
    return render(request, 'hotelbooking/booking.html',
                  context={'clientform': clientform, 'error_message': error_message})


def booking_room_page(request):
    if request.session.get('client_id'):
        client_id = request.session.get('client_id')
        client_info = Client.objects.get(id=client_id)
        # Nights
        settle_nights = client_info.check_out - client_info.check_in
        settle_nights = settle_nights.days
        if settle_nights % 10 == 1:
            rus_settle_nights = f"{settle_nights} ночь"
        elif settle_nights % 10 == [2, 3, 4]:
            rus_settle_nights = f"{settle_nights} ночи"
        else:
            rus_settle_nights = f"{settle_nights} ночей"
        # Available Rooms
        room_typies = RoomType.objects.all()
        rooms = Room.objects.filter(bron=False)
        empty_rooms = {}
        count_id = 1
        for room in rooms:
            room = room.room_type_id
            if not room in empty_rooms.keys():
                room_count = Room.objects.filter(room_type_id=room, bron=False).count()
                room_price = RoomType.objects.get(room_name=room.room_name)
                empty_rooms.update({room.room_name: [room_count, room_price.price, count_id]})
                count_id += 1
        # GET method
        if request.GET:
            client = Client.objects.get(id=client_id)
            get_rooms = dict(request.GET)['room-names']
            get_count = dict(request.GET)['room-count']
            for room, count in zip(get_rooms, get_count):
                count = int(count)
                rm_type = RoomType.objects.get(room_name=room)
                rm = Room.objects.filter(bron=False, room_type_id=rm_type.id)
                id_list = []
                for i in rm:
                    id_list.append(i.id)
                if count > 0:
                    # Bookings Table
                    booking_data = Booking(
                        user_id=client,
                        room_id=rm_type,
                        count=count)
                    booking_data.save()
                    # Rooms Table
                    for x in range(count):
                        room_id = Room.objects.get(id=id_list[x])
                        room_id.user_id = client
                        room_id.bron = True
                        room_id.save(update_fields=["user_id", "bron"])
            # Total sum
            total_sum_session = dict(request.GET)['total'][0]
            request.session['total_sum'] = int(total_sum_session)
            return HttpResponseRedirect("/booking/select-room/payment")
        return render(request, 'hotelbooking/booking-room.html', {
            'room_typies': room_typies,
            'empty_rooms': empty_rooms,
            'client_info': client_info,
            'settle_nights': settle_nights,
            'rus_settle_nights': rus_settle_nights})
    else:
        return HttpResponseRedirect('/booking')


def payment_page(request):
    if request.session.get('client_id'):
        client_id = request.session.get('client_id')
        total_sum = request.session.get('total_sum')
        client_info = Client.objects.get(id=client_id)

        if request.method == "POST":
            paymentform = PaymentForm(request.POST)
            if paymentform.is_valid():
                payment_data = Payment(
                    user_id=client_info,
                    cardname=paymentform.cleaned_data['cardname'],
                    cardnumber=paymentform.cleaned_data['cardnumber'],
                    cvv_code=paymentform.cleaned_data['cvv_code'],
                    expiration=paymentform.cleaned_data['expiration'],
                    total=total_sum
                )
                payment_data.save()
                return HttpResponseRedirect("/rooms")
        else:
            paymentform = PaymentForm()
        return render(request, 'hotelbooking/payment.html', context={'paymentform': paymentform})
    else:
        return HttpResponseRedirect('/booking')
