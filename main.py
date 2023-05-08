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
bot = Bot(token='')
# инициализация диспетчера
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# В этой функции мы должны получить список подключаемых устройств, а так же отключаемых, и после выполнения команды
# сохранять структуру данных в отдельном файле: неделя, месяц, год, время, подключался-отключался, внешний IP, IP туннеля

def get_connected():
    command = 'bash ./get_connected.sh'
    pipe = os.popen(command)
    return pipe.read()
    # result = subprocess.call(['bash', 'start_server.sh'])
    # return result
def start_server():
    command = 'bash ./start_server.sh'
    pipe = os.popen(command)
    return pipe.read()
    # result = subprocess.call(['bash', 'start_server.sh'])
    # return result

def restart_server():
    command = 'bash ./restart_server.sh'
    pipe = os.popen(command)
    return pipe.read()

def stop_server():
    command = 'bash ./stop_server.sh'
    pipe = os.popen(command)
    return pipe.read()

def check_status():
    command = 'bash ./check_status.sh'
    pipe = os.popen(command)
    return pipe.read()

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
async def button1_handler(message: Message):
    user_id = message.from_user.id
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text=str(get_connected()), reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(filters.IDFilter(user_id=869031863), text='Остановить сервер')
async def button1_handler(message: Message):
    user_id = message.from_user.id
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text=str(stop_server()), reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(filters.IDFilter(user_id=869031863), text='Запустить сервер')
async def button_checkuot_handler(message: Message):
    user_id = message.from_user.id
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text=str(start_server()), reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)



@dp.message_handler(filters.IDFilter(user_id=869031863), text='Перезагрузить сервер')
async def button_checkuot_handler(message: Message):
    user_id = message.from_user.id
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(chat_id=user_id, text=str(restart_server()), reply_markup=markup,
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
    await bot.send_message(chat_id=user_id, text=str(check_status()), reply_markup=markup,
                           parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)
