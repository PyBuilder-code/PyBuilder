import telebot
from datetime import time
from telebot import TeleBot

bot = telebot.TeleBot("7793340834:AAHv5exlOamBxbdhSxIRo3ndJIB15zsavfU")

@bot.message_handler(commands=['start'])
def start_messaging(message):
    bot.send_message(message.chat.id, "Привет, ты мне написал /start")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)