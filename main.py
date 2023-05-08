import os
import logging
import time
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton
from aiogram.types import ParseMode
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import Message
import logging
from aiogram.dispatcher import filters

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import subprocess

# настройка логирования
logging.basicConfig(level=logging.INFO)

# инициализация бота
bot = Bot(token='6226522935:AAEsccDKhphF9NTKHhQyfdr_eQZEuasAJqA')
# инициализация диспетчера
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# В этой функции мы должны получить список подключаемых устройств, а так же отключаемых, и после выполнения команды
# сохранять структуру данных в отдельном файле: неделя, месяц, год, время, подключался-отключался, внешний IP, IP туннеля



def start_server():
    result = subprocess.call(['bash', 'start_server.sh'])
    return result



# Создаем кнопки основного меню
button1 = KeyboardButton('Получить список подключаемых устройств')
button2 = KeyboardButton('Остановить сервер')
button3 = KeyboardButton('Запустить сервер')
button4 = KeyboardButton('Перезагрузить сервер')
button5 = KeyboardButton('Получить новый конфигурационный файл')
button6 = KeyboardButton('Получить статус сервера')
# Создаем список кнопок
keyboard = [[button1],[button6], [button2], [button3], [button4], [button5]]




# обработчик команды /start
@dp.message_handler(filters.IDFilter(user_id=869031863), commands=['start'])
async def start_command_handler(message: types.Message):
    user_id = message.from_user.id
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text="Здравствуйте, Валентин! Выберите действие:",
                           reply_markup=markup, parse_mode=ParseMode.MARKDOWN)



@dp.message_handler(filters.IDFilter(user_id=869031863), text='Получить список подключаемых устройств')
async def devices_command(message: types.Message):
    # Здесь мы используем subprocess для выполнения команды OpenVPN сервера
    # и получения списка устройств, подключенных к серверу
    command_output = subprocess.check_output(['sudo','netstat', '-tnp'])

    # Обработка вывода команды и формирование сообщения для отправки пользователю
    device_list = [line.split(",")[0] for line in command_output.decode().split("\n")[1:-1]]
    message_text = "Список устройств, подключенных к OpenVPN серверу:\n\n"
    for device in device_list:
        message_text += f"- {device}\n"

    # Отправка сообщения с списком устройств пользователю
    await message.reply(message_text, parse_mode=ParseMode.MARKDOWN)
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text='Получить список подключаемых устройств', reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(filters.IDFilter(user_id=869031863), text='Остановить сервер')
async def button1_handler(message: Message):
    user_id = message.from_user.id
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text='Остановить сервер', reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(filters.IDFilter(user_id=869031863), text='Запустить сервер')
async def button_checkuot_handler(message: Message):
    user_id = message.from_user.id
    start_server()
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text=str(start_server()), reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)



@dp.message_handler(filters.IDFilter(user_id=869031863), text='Перезагрузить сервер')
async def button_checkuot_handler(message: Message):
    user_id = message.from_user.id
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text='Перезагрузить сервер', reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)



@dp.message_handler(filters.IDFilter(user_id=869031863), text='Получить новый конфигурационный файл')
async def button_checkuot_handler(message: Message):
    user_id = message.from_user.id
    gen_sert()
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text='Получить новый конфигурационный файл', reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(filters.IDFilter(user_id=869031863), text='Получить статус сервера')
async def button_checkuot_handler(message: Message):
    user_id = message.from_user.id
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text='Получить статус сервера', reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)
