import telebot
from telebot import types
from schedule import Schedule

tBot = telebot.TeleBot('7519900327:AAEW2RA718-L_gsDCLtGXo6rzgsZEcE_6Eo')
s = Schedule()


@tBot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сегодня")
    btn2 = types.KeyboardButton("Завтра")
    markup.add(btn1, btn2)
    tBot.send_message(message.chat.id, text="aaaaa", reply_markup=markup)


@tBot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Сегодня':
        tBot.send_message(message.chat.id, s.form_schedule_today())
        print('aboba')
    elif message.text == 'Завтра':
        tBot.send_message(message.chat.id, s.form_schedule_tomorrow())
        print('2aboba2')


tBot.infinity_polling()

# dict = {
#     "hi": lambda: print("Hi"),
#     "bye": lambda: print("bye")
# }
# str = input()
# dict[str]()