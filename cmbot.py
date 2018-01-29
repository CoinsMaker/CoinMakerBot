import telebot
import config
import requests

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришла команда /help")

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришла команда /start")

@bot.message_handler(commands=['settings'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришла команда /settings")

@bot.message_handler(commands=['action'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришла команда /action")



@bot.message_handler(content_types=["text"] + message.from_user.id)
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришло простое сообщение")

@bot.message_handler(content_types=["document"])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришел документ")

@bot.message_handler(content_types=["audio"])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришла аудиозапись")

@bot.message_handler(content_types=["photo"])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришло изображение")

@bot.message_handler(content_types=["sticker"])
def handle_text(message):
    bot.send_message(message.from_user.id, "Пришел стикер")




bot.polling()
