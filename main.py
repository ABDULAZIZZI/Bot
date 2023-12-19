import logging
import requests

from aiogram import Bot, Dispatcher, executor, types
from keyboards import *

API_TOKEN = '6428980378:AAHMDwKWajyHrsy54lSX59pHowTQXjO9GFw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    await message.reply(f"Hello, {first_name} {last_name}", reply_markup=markup)


@dp.message_handler(commands='currency')
async def get_course(message: types.Message):
    url = requests.get("https://nbu.uz/en/exchange-rates/json/")
    data = url.json()
    print(data)
    currency_data = ""
    for i in data:
        currency_data += f"{i['title']} - {i['code']} - {i['cb_price']}1 UZS-so'mga\n"

    await message.answer(currency_data, reply_markup=get_nbu_keyboards())


@dp.message_handler()
async def get_currency_by_code(message: types.Message):
    text = message.text.split()
    if len(text) > 1:
        code = text[0].upper()
        amount = text[1]
        url = requests.get("https://nbu.uz/en/exchange-rates/json/")
        data = url.json()
        for i in data:
            if i['code'] == code:
                print(i['cb_price'])
                result = float(amount) * float(i['cb_price'])
                await message.answer(text=f"{amount} {code} --> {result} UZS SO'Mga")
    else:
        code = message.text.upper()
        url = requests.get("https://nbu.uz/en/exchange-rates/json/")
        data = url.json()
        for i in data:
            if i['code'] == code:
                await message.answer(text=f"{i['title']} - {code} - {i['cb_price']}UZS SO'Mga")

    url = requests.get('https://hp-api.onrender.com/api/characters')
    date = url.json()
    name = message.text
    for i in date:
        if i['name'] == name:
            await message.answer(f"Name: {i['name']}\nHouse: {i['house']}\nDate of birth: {i['dateOfBirth']}")
            await message.answer_photo(photo=i['image'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
