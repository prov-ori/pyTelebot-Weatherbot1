import telebot
import requests
import json

bot = telebot.TeleBot('6648714139:AAHZ_N7dKOhtrSXOeNZ_gfp1SSWWwFNfEQA')
API = '58ec4645144da65562725f981065d0fc'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Я - бот, созданный Михаилом. Для получения информации по поводу погоды, напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Температура в "{city}": {temp} градусов цельсия.')

        image1 = 'sunny.jpg' if temp < 20.0 else 'sun.jpg'
        file = open('./' + image1, 'rb')
        if temp <= 10.0:
            file = open('./' + 'cloudy.jpg', 'rb')
        elif temp <= 0.0:
            file = open('./' + 'ice.png', 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан не верно')


bot.polling(none_stop=True)
