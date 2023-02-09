import telebot
import random
from telebot import types
# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
# Загружаем список kek
k = open('data/kek.txt', 'r', encoding='UTF-8')
kek  = k.read().split('\n')
k.close()
# Загружаем список kek
v = open('data/vova.txt', 'r', encoding='UTF-8')
vova  = v.read().split('\n')
v.close()
e = open('data/egor.txt', 'r', encoding='UTF-8')
egor  = e.read().split('\n')
e.close()
# Создаем бота
bot = telebot.TeleBot('5539879235:AAE6ywr_9PcECBUiB7LlYV5w01-jY__EESk')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Поговорка")
        item3=types.KeyboardButton("Тыкни")
        item4=types.KeyboardButton("Для Вовы")
        item5=types.KeyboardButton("Для Егора")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты\nТыкни - узнаешь всё',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
   if message.text.strip() == 'Факт' :
      answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
   elif message.text.strip() == 'Поговорка':
      answer = random.choice(thinks)
   elif message.text.strip() == 'Тыкни':
      answer = random.choice(kek)
   elif message.text.strip() == 'Для Вовы':
      answer = random.choice(vova)
   elif message.text.strip() == 'Для Егора':
      answer = random.choice(egor)
    # Отсылаем юзеру сообщение в его чат
   bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)