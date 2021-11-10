from config import bot

from modules.echo import echo

if __name__ == '__main__':
    echo(bot)
    bot.polling(none_stop=True
