def echo(bot):
    @bot.message_handler(content_types=['text'])
    def simple_echo(message):
        bot.send_message(message.chat.id, message.text)