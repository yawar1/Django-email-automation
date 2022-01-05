from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipient
from django.core.mail import send_mail
from django.db.models.signals import post_save
import requests,json

def read_db(*y,**x):
    users = Recipient.objects.all()
    most_recent_user_added = users[len(users)-1]
    temp = get_temp(most_recent_user_added.city)
    emoji = get_emoji(temp)
    send_mail(
        subject=f"Hi {most_recent_user_added.name}, interested in our services",
        message=f"Dear sir/maam, The temperature in {most_recent_user_added.city} is {temp} (in standard units) {emoji}",
        from_email="yawarmushtaq52@gmail.com",
        recipient_list=[most_recent_user_added.mail],
        fail_silently=True
        )
    return HttpResponse(200)

def get_temp(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4f57ec75313cf9d5181b6fc7daf3db13'
    r = requests.get(url,allow_redirects=True)

    open('weather.json', 'wb').write(r.content)
    with open('weather.json') as json_file:
        data = json.load(json_file)

    return data['main']['temp']

def get_emoji(temp):
    if temp < 283.15:
        return '\U0001F976'
    if temp >= 283.15 and temp < 293.15:
        return '\U0001F60E'
    if temp >= 293.15 and temp < 303.15:
        return '\U0001F975'
    if temp >= 303.15:
        return '\U0001F92F'

post_save.connect(read_db,sender=Recipient)