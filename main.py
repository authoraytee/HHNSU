from bot import echo
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

if __name__ == '__main__':
    echo(bot)
    bot.polling(none_stop=True)
