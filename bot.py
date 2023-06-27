import telebot
from telebot import types
bot = telebot.TeleBot('6075249140:AAFRR6Ry1Nih5kXH-1CmloYtsu9AmrO4Wcs')
@bot.message_handler(content_types=['text'])
@bot.callback_query_handler(func=lambda call: True)
def get_text_messages(message):
    if message.text == 'привет'or message.text == 'Привет' or message.text == 'hi' or message.text == 'Hi' or message.text == 'Hello' or message.text == 'hello' :
        bot.send_message(message.from_user.id, "Приветствую тебя мой дорогой друг")
        bot.send_message(message.from_user.id,'вот что я могу:сказать имя,ответить на привет ,попрощаться,сыграть в вопросы')
        bot.send_message(message.from_user.id, "Чем могу тебе помочь?")
    elif message.text== '\help':
        bot.send_message(message.from_user.id, "Поприветствуй меня")
    elif message.text == 'скажи имя' or message.text == 'Как тебя зовут'  or message.text == 'как тебя зовут'or message.text == 'Как тебя зовут?'  or message.text == 'как тебя зовут?':
        bot.send_message(message.from_user.id, "я @smith228_bot")
    elif message.text == 'пока' or message.text == 'Пока' or message.text == 'до встречи'or message.text == 'До встречи':
        bot.send_message(message.from_user.id, "пока рад был поговорить")
    elif message.text== 'давай сыграем' or message.text== 'Давай сыграем' or  message.text== 'Давай сыграем в вопросы'  or message.text== 'давай сыграем в вопросы':
        def get_qua(message):
            keyboard = types.InlineKeyboardMarkup()
            key_yes = types.InlineKeyboardButton(text='2007', callback_data='yes')
            keyboard.add(key_yes)
            key_no= types.InlineKeyboardButton(text='2008', callback_data='no')
            keyboard.add(key_no)
            question = 'Когда вышел 1 айфон?'
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
        def callback_worker(call):
            if call.data == 'yes': 
                bot.send_message(call.message.chat.id, 'абсолютно верно')
            elif call.data == 'no':
                bot.send_message(call.message.chat.id,'неверно в 2007')
    else:
        bot.send_message(message.from_user.id, "824#djq394q")
        bot.send_message(message.from_user.id, "ага не понятно тебе")
        bot.send_message(message.from_user.id,'вот и я тебя не понимаю')
bot.polling(none_stop=True,interval=0)