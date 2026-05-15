from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)



def start_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Каталог", style="primary",  callback_data="catalog")],
            [InlineKeyboardButton(text="Тг канал", url="https://t.me/mobilegemss")],
            [InlineKeyboardButton(text="Отзывы ТГ", url="https://t.me/redlineshopchat"),InlineKeyboardButton(text="Отзывы ВК", url="https://vk.com/topic-147969897_48891442")]
        ]
    )
    return keyboard

def catalog_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Бравл Старс", callback_data="brawl")],
            [InlineKeyboardButton(text="Игра 1", callback_data="game1"),InlineKeyboardButton(text="Игра 2", callback_data="game2")]
        ]
    )
    return keyboard

def backward_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Написать Артуру для покупки", style="primary",
                                  url="https://t.me/Mobile_Game_YT1")],
            [InlineKeyboardButton(text="Назад", style="primary", callback_data="catalog")]
        ]
    )
    return keyboard

def brawl_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ОСОБАЯ АКЦИЯ 67 ГЕМОВ", style="success", callback_data="67brawl")],
            [InlineKeyboardButton(text="Написать Артуру для покупки", style="primary",
                                  url="https://t.me/Mobile_Game_YT1")],
            [InlineKeyboardButton(text="Назад", style="danger", callback_data="catalog")],
        ]
    )
    return keyboard

def back_to_brawl_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Написать Артуру для покупки", style="primary", url="https://t.me/Mobile_Game_YT1")],
            [InlineKeyboardButton(text="Назад", style="danger", callback_data="brawl")],
        ]
    )
    return keyboard