import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from bot.commands import register_user_commands
from bot.commands.utils import bot_commands
from bot.config import TOKEN
from bot.fsm_handler import register_fsm
from bot.handlers import register_main_menu
from database.models import Base
from database.task_crud import engine
from parser.main_parser import parse_codeforces


def register_routers(dp):
    register_user_commands(dp)
    register_main_menu(dp)
    register_fsm(dp)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    bot = Bot(TOKEN)

    commands = [types.BotCommand(
        command=item.command,
        description=item.short_desc)
        for item in bot_commands
    ]

    register_routers(dp)
    Base.metadata.create_all(bind=engine)
    parse_codeforces(2)
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
