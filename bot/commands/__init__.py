__all__ = ['start_command', 'help_command_all']

from aiogram import Router
from aiogram.filters import CommandStart, Command

from bot.commands.bot_commands import start_command, help_command_all


def register_user_commands(router: Router):
    router.message.register(start_command, CommandStart())
    router.message.register(help_command_all, Command(commands=['help', 'Помощь']))
