from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton as kb

main_menu_kb = ReplyKeyboardBuilder()

main_menu_kb.row(
    kb(text='Главная'),
    kb(text='По категориям'),
    kb(text='По сложности'),
)

