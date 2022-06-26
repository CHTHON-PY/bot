M = "\033[1;96m"
import telebot
import requests
from telebot import types
tok_kabos = ("5496267284:AAEreO2kP5KWA3zFRjO4SZ9AdXT9Y0lEOo0")
bot = telebot.TeleBot(tok_kabos)

sff = types.InlineKeyboardButton(text="• المطور",url="t.me/mq_5p")
kees = types.InlineKeyboardButton(text="• المطور",callback_data="tg")

@bot.message_handler(commands = ["start"])
def kabos(message):
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 2
    Keyy.add(sff,kees)
    kafirst = message.chat.first_name
    aan = types.InlineKeyboardMarkup()
    aan.add(sff,kees)
    bot.send_message(message.chat.id,text = f"للتواصل",reply_markup=Keyy)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="tg":
        KABOS(call.message)
    elif call.data == "tg":
    	KABS(call.message)
    	
def answer(message):
        ka_A = message.text
        txtkabos = f"• 1"
        bot.send_message(message.chat.id,callback_data=txtkabos)


        
bot.polling(True)