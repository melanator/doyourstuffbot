from aiogram import Bot, executor
import config
import handlers
from misc import dp, bot


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
