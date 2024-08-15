from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Полное имя'})
    )
    email = forms.EmailField(max_length=255,
                            widget=forms.EmailInput(attrs={'placeholder': 'Email'})
                            )
    phone = forms.CharField(min_length=10, max_length=13,
                            widget=forms.TextInput(attrs={'placeholder': 'Телефон'})
                            )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Напишите свое сообщение ...'})
    )


class ClientForm(forms.Form):
    firstname = forms.CharField(label="Имя:", widget=forms.TextInput(attrs={
        'placeholder': 'Введите ваше имя',
        'class': 'form-control'})
                                )
    lastname = forms.CharField(label="Фамилия:", widget=forms.TextInput(attrs={
        'placeholder': 'Введите свою фамилию',
        'class': 'form-control'})
                               )
    email = forms.EmailField(label="Электронная почта:", widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес электронной почты',
        'class': 'form-control'})
                            )
    country = forms.CharField(label="Страна:", widget=forms.TextInput(attrs={
        'placeholder': 'Введите свою страну',
        'class': 'form-control'})
                              )
    phone = forms.CharField(label="Номер телефона:", max_length=13, min_length=10, widget=forms.TextInput(
        attrs={'placeholder': 'Введите свою страну', 'class': 'form-control'})
                            )
    adults = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'value': '0'
    }))
    children = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'value': '0'
    }))
    check_in = forms.DateField(label="Заселение:", widget=forms.DateInput(attrs={
        'class': 'date-input',
        'type': 'date'
    }))
    check_out = forms.DateField(label="Выселение:", widget=forms.DateInput(attrs={
        'class': 'date-input',
        'type': 'date'
    }))


class PaymentForm(forms.Form):
    cardname = forms.CharField(label='Имя карты',
                               widget=forms.TextInput(attrs={'placeholder': 'John Smith'}),
                               )
    cardnumber = forms.CharField(label='Номер карты', min_length=19, max_length=19,
                                 widget=forms.TextInput(attrs={'placeholder': '0000-0000-0000-0000', 'id': 'cr_no'})
                                 )
    cvv_code = forms.CharField(label='CVV', min_length=3, max_length=3,
                               widget=forms.TextInput(
                                   attrs={'placeholder': '***', 'class': 'placeicon', 'type': 'password'})
                               )
    expiration = forms.CharField(label='Дата окончания срока', min_length=5, max_length=5,
                                 widget=forms.TextInput(attrs={'placeholder': 'MM/YY', 'id': 'exp'})
                                 )
