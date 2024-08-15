from django.db import models


class Client(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    adults = models.IntegerField()
    children = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class RoomType(models.Model):
    room_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    max_persona = models.IntegerField()
    room_size = models.IntegerField()
    beds = models.CharField(max_length=255)
    comforts = models.TextField()
    services = models.TextField()
    smoking = models.BooleanField()
    mini_bar = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return f'{self.room_name}'


class Room(models.Model):
    user_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING, null=True, blank=True)
    room_number = models.IntegerField()
    room_type_id = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    bron = models.BooleanField(default=False)

    def __str__(self):
        return f'Номер #{self.room_number}'


class Booking(models.Model):
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    room_id = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.user_id} - {self.room_id} room'


class Payment(models.Model):
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    cardname = models.CharField(max_length=255)
    cardnumber = models.CharField(max_length=19)
    expiration = models.CharField(max_length=10)
    cvv_code = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return f'{self.user_id} user - {self.cardname}'


class Feedback(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return f'{self.fullname}'
