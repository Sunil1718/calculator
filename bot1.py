import telebot
token="7466444170:AAFminT9F3hT1t7stBoVKGDSWU_elnj-wdI"
bot=telebot.TeleBot(token)
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome To Our Math Calculator Bot. Here U Can Calculate All Mathematical Operations....")

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"""Here U Can See All Commands That Are Help For calculations
/start -> Greeting
/help -> All Commands Lists
""")

@bot.message_handler()
def calculate(message):
    try:
        a=eval(message.text.strip())
    except Exception as e:
        a="This Can't Be Calculate"
    bot.reply_to(message,a)
bot.polling()
