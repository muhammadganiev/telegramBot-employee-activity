import telebot

TOKEN = '5328372677:AAEdTWisnVtVOoleO-pojxmEBXCZdRe_CTw'

bot = telebot.TeleBot(TOKEN)
def echo_messages(*messages):
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            bot.send_message(chatid, text)
bot.set_update_listener(echo_messages)
bot.polling()

while True: # Don't let the main Thread end.
    pass