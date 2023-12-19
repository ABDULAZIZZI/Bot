from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton)
import requests

url = requests.get("https://nbu.uz/en/exchange-rates/json/")
data = url.json()
currency_data = ""

for i in data:
    currency_data += i['code'] + ' '
currency_list = currency_data.split(' ')

markup = ReplyKeyboardMarkup()
for il in currency_list:
    markup.insert(il)


def get_nbu_keyboards():
    url = requests.get('https://nbu.uz/en/exchange-rates/json/')
    data = url.json()
    nbu_buttons = ReplyKeyboardMarkup()
    for i in data:
        button = ReplyKeyboardMarkup(text=i['code'], callback_data=f"key__{i['code']}")
        nbu_buttons.insert(button)
    return nbu_buttons


markup = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("AED"),
            KeyboardButton("AUD")
        ],
        [
            KeyboardButton("CAD"),
            KeyboardButton("CHF")
        ],
        [
            KeyboardButton("CNY"),
            KeyboardButton("DKK")
        ],
        [
            KeyboardButton("EGP"),
            KeyboardButton("EUR")
        ],
        [
            KeyboardButton("GBP"),
            KeyboardButton("ISK")
        ],
        [
            KeyboardButton("AJPY"),
            KeyboardButton("KRW")
        ],
        [
            KeyboardButton("KWD"),
            KeyboardButton("KZT")
        ],
        [
            KeyboardButton("LBP"),
            KeyboardButton("MYR")
        ],
        [
            KeyboardButton("NOK"),
            KeyboardButton("PLN")
        ],
        [
            KeyboardButton("RUB"),
            KeyboardButton("SEK")
        ],
        [
            KeyboardButton("SGD"),
            KeyboardButton("TRY")
        ],
        [
            KeyboardButton("UAH"),
            KeyboardButton("USD")
        ],
    ],
    resize_keyboard=True
)
