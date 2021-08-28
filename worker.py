import requests
import datetime
import random
import time
import json

def get_time():
    now = datetime.datetime.now()
    return datetime.datetime.now().strftime("%H:%M:%S   %Y-%m-%d")

def get_token():
    return open('token.txt', 'r', encoding='UTF-8').read()

def change_status_text(token, text):
    url = 'https://discord.com/api/v9/users/@me/settings'

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": token
    }
    payload = {"custom_status": {"text": text}}

    r = requests.patch(url, headers=headers, data=json.dumps(payload))

token = get_token()

while True:
    change_status_text(token, str(get_time()))
    time.sleep(0.5)

