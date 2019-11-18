from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

URL = 'https://api.telegram.org/bot919974881:AAHwfCsrATbNx9fxjhbSxzacw5Ip-G-aTKE/'
#URL = URL + 'getMe'


def write_json(data, filename='./answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def index(request):
    # bot.polling(none_stop=True)

    r = requests.get(URL + 'getMe')
    #r = requests.get(URL)

    write_json(r.json())

    return HttpResponse("<h1>--Скрипт бота 'Test1--' </h1>" + str(r.json()))
