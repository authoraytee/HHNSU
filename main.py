from config import bot
import telebot

TOKEN = '2036020508:AAFP8dlyx70n_oW7M-MZ8w9uOa6dZl8KpuQ'


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def simple_echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
