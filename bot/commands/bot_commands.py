from aiogram import types
from aiogram.filters import CommandObject

from bot.commands.utils import bot_commands
from bot.keyboards.replies.main_menu import main_menu_kb


async def start_command(message: types.Message) -> None:
    await message.answer('Тут можешь найти задачки с codeforces', reply_markup=main_menu_kb.as_markup())


async def help_command_all(
        message: types.Message,
        command: CommandObject) -> types.Message:
    if command.args:
        for cmd in bot_commands:
            if cmd.command == command.args:
                return await message.answer(cmd.long_desc)
        else:
            return await message.answer('Команда не найдена')
    return await message.answer('HELP_TEXT')
