from aiogram.enums import ButtonStyle
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)



def start_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Каталог", style="primary",  callback_data="catalog")],
            [InlineKeyboardButton(text="Тг канал", url="https://t.me/mobilegemss"),InlineKeyboardButton(text="Сайт", url="https://redlineshop.shop")],
            [InlineKeyboardButton(text="Реферальная система", callback_data="referal")],
            [InlineKeyboardButton(text="Отзывы ТГ", url="https://t.me/redlineshopchat"),InlineKeyboardButton(text="Отзывы ВК", url="https://vk.com/topic-147969897_48891442")]
        ]
    )
    return keyboard

def catalog_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🏆 Brawl Stars 🏆", callback_data="brawl")],
            [InlineKeyboardButton(text="Clash Royale", callback_data="clash_royal"),InlineKeyboardButton(text="Sim City Buildit", callback_data="sim_city")],
            [InlineKeyboardButton(text="☢ S.T.A.L.K.E.R. 2 ☢", callback_data="stalker2")],
            [InlineKeyboardButton(text="TikTok Валюта", callback_data="tiktok"), InlineKeyboardButton(text="Telegram Плюшки", callback_data="telegram")], 
            [InlineKeyboardButton(text="🤖 ChatGPT 🤖", callback_data="gpt")],
            [InlineKeyboardButton(text="🌐 VPN 🌐", callback_data="vpn")],
            [InlineKeyboardButton(text="Назад в меню", style=ButtonStyle.PRIMARY ,callback_data="menu")]
        ]
    )
    return keyboard

def backward_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Написать Артуру для покупки", style=ButtonStyle.PRIMARY,
                                  url="https://t.me/Mobile_Game_YT1")],
            [InlineKeyboardButton(text="Назад", style="danger", callback_data="catalog")]
        ]
    )
    return keyboard

def brawl_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ОСОБАЯ АКЦИЯ 67 ГЕМОВ", style=ButtonStyle.SUCCESS, callback_data="67brawl")],
            [InlineKeyboardButton(text="Бусты", style=ButtonStyle.SUCCESS, callback_data="brawl_boost")],
            [InlineKeyboardButton(text="☠️Читы☠️", style=ButtonStyle.SUCCESS, callback_data="brawl_cheats")],
            [InlineKeyboardButton(text="Написать Артуру для покупки", style=ButtonStyle.PRIMARY,
                                  url="https://t.me/Mobile_Game_YT1")],
            [InlineKeyboardButton(text="Назад", style=ButtonStyle.DANGER, callback_data="catalog")],
        ]
    )
    return keyboard

def back_to_brawl_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Написать Артуру для покупки", style=ButtonStyle.PRIMARY, url="https://t.me/Mobile_Game_YT1")],
            [InlineKeyboardButton(text="Назад", style="danger", callback_data="brawl")],
        ]
    )
    return keyboard
