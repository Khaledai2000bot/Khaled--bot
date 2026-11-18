import telebot

TOKEN = "حط_التوكن_هنا"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا بيك يا خالد! البوت شغال ✅")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"انت قولت: {message.text}")

print("البوت شغال...")
bot.polling()
