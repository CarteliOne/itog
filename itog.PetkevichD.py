import telebot
import random
from telebot import types


bot = telebot.TeleBot('5539252161:AAHJ1GPwEMY3KjPewy5Eu4vzT5HCCl_GYOY')

@bot.message_handler(commands=["start"])
def start(message):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button=types.KeyboardButton("Рандомное число")
        markup.add(button)
        bot.send_message(m.chat.id, 'Нажми на кнопку для получения числа от 1 до 1000',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.strip() == 'Рандомное число' :
            chislo = str(random.randint(0, 1000))
    bot.send_message(message.chat.id, chislo)
bot.polling(none_stop=True, interval=0)