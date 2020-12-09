from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import filters
from misc import dp, bot


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.reply('Привет')


# Response to any message
@dp.message_handler()
async def show_portfolios(message: types.Message):
    await message.reply(message.text)
