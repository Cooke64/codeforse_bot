import typing


class BotCommand(typing.NamedTuple):
    command: str
    short_desc: str
    long_desc: str


bot_commands = (
    BotCommand('start', 'START_DESCR', 'long_star'),
    BotCommand('help', 'HELP_DESCR', 'long_help'),
)
