import telegram_send
import os
import telebot, time
from telebot import types


bot = telebot.TeleBot(os.environ['API_KEY'])
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  keyboard = types.InlineKeyboardMarkup()

  keyboard.row(
    types.InlineKeyboardButton(text='Отправить локацию', callback_data="location"))
  
  if call.data == "otkrit":
    bot.send_message(call.message.chat.id, "Отправьте локацию для подтверждения смены", reply_markup = keyboard)
    telegram_send.send(messages = [f'{call.message.chat.first_name} открыл смену в {tconv(call.message.date)}']);
  if call.data == "location":
    bot.send_message(call.message.chat.id, 'Вы удачно отметились, хорошего рабочего дня')
@bot.message_handler()
def user(message):
  keyboard = types.InlineKeyboardMarkup()

  keyboard.row(
    types.InlineKeyboardButton(text='Открыть смену', callback_data="otkrit"),
    types.InlineKeyboardButton(text='Закрыть смену', callback_data="zakrit"))
  if message.text.lower() == "отметиться":
    bot.send_message(message.chat.id, "Отметьтесь перед началом рабочего дня :)", reply_markup = keyboard)
    
  #@bot.message_handler()
   # def admin(message):
  #   if call.data == "true":
   #     telegram_send.send(messages = [f'{message.from_user.first_name} открыл смену в {tconv(message.date)}']);
bot.polling(none_stop=True)