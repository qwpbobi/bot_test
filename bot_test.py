import telebot

TOKEN = '6182882883:AAFALLjMdxv6bm8Z-ui5-1prxshsoGwj7bI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message,f'ID: {message.from_usser.id}')
         
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')

bot.polling(none_stop=True)