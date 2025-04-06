import config
import telebot
from telebot import types


bot = telebot.TeleBot(config.token)

chat_id = 809091866

markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)
bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	photo = open('C:/Users/willy/OneDrive/Изображения/Saved Pictures/plane.jpg', 'rb')
	bot.send_photo(chat_id, photo)
	# ReplyKeyboardRemove: hides a previously sent ReplyKeyboardMarkup
	# Takes an optional selective argument (True/False, default False)
	markup = types.ReplyKeyboardRemove(selective=False)
	bot.send_message(chat_id, message, reply_markup=markup)

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	pass

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	pass

# Which could also be defined as:
def test_message(message):
	return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
	pass

# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == '😀')
def send_something(message):
    pass

bot.infinity_polling()