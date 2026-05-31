from aiogram import Router
from aiogram.filters import Command, callback_data
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    FSInputFile,
    InputMediaPhoto
)
from handlers.inline_keyboards import *
import aiosqlite

router = Router()

# --- База данных

DB_NAME = "redlinebot.sql"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
                        CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY,
                                        user_id INTEGER UNIQUE,
                                        full_name TEXT
                        )
                        """)
        await db.commit()

async def add_user(user_id, full_name):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO users (user_id, full_name) VALUES(?, ?)", (user_id,full_name))
        await db.commit()

async def get_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM users")
        result = await cursor.fetchall()
        return result


# --- Конец базы данных



# Тут начинаются callback_query

@router.callback_query(lambda c: c.data == "catalog")
async def on_tg_channel(callback: CallbackQuery):
    # if callback.data == ""
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/redline_shop_1.png"),
                              caption="<b>Выберите игру из каталога товаров:</b>",
                              parse_mode="HTML"),
        reply_markup=catalog_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "game1")
async def on_brawl_stars(callback: CallbackQuery):
    await callback.message.edit_caption(
        caption="game1 цены",
        reply_markup=backward_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "game2")
async def on_brawl_stars(callback: CallbackQuery):
    await callback.message.edit_caption(
        caption="game2 цены",
        reply_markup=backward_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "brawl")
async def on_brawl_stars(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/brawlgems.jpg"),
                              caption='Заходом на аккаунт через почту:\n'
                            'Бравл Пасс - 1799 руб - 70 BYN\n'
                            'Бравл Пасс Плюс - 2599 руб - 100 BYN\n'
                            'Улучшение до Бравл Пасс Плюс - 999 руб - 40 BYN\n'
                            'Про Пасс - 4999 руб - 190 BYN\n'
                            '\n'
                            'Через Supercell Store:\n'
                            'Brawl Pass - 1999 руб - 80 BYN\n'
                            'Brawl Pass Plus - 2899 руб - 112 BYN\n'
                            'Про Пасс - 5499 руб - 210 BYN\n'
                            '\n'
                            'Подарком через Supercell Id:\n'
                            'Brawl Pass Plus - 3999 руб - 151 BYN\n'
                            'Про Пасс - 6999 руб - 265 BYN\n'
                            '30 гемов - 449 руб - 18 BYN\n'
                            '80 гемов - 999 руб - 38 BYN\n'
                            '170 гемов - 1999 руб - 75 BYN\n'
                            '360 гемов - 3937 руб - 147 BYN\n'
                            '950 гемов - 9907 руб - 365 BYN\n'
                            '2000 гемов - 19927 руб - 735 BYN\n'
                            '\n'
                            'Для покупки любой другой акции отправьте фото акции <a href="https://t.me/Mobile_Game_YT1">Артуру</a> при покупке',
                              parse_mode="HTML"
                              ),
        reply_markup=brawl_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "67brawl")
async def on_brawl_stars(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/67meme.jpg"),
                              caption="67 гемов - 967 руб"),
        reply_markup=back_to_brawl_inline_keyboard()
    )
    await callback.answer()



# Отсюда начинаются команды

@router.message(Command("start"))
async def on_start(message: Message):
    await init_db()
    await add_user(message.from_user.id, message.from_user.full_name)

    await message.answer_photo(photo=FSInputFile("Images/redline_shop_1.png"),caption='Добро пожаловать, вас встречает бот магазина [ReDLine Shop 🤑](https://t.me/mobilegemss) \n'
                         '\n'
                         'Для просмотра цен на донаты нажмите на кнопку Каталог под сообщением 😎 \n'
                         '\n'
                         'При проблемах с ботом или для покупки доната писать [Артуру](https://t.me/Mobile_Game_YT1) 🤖'
                         ,reply_markup=start_inline_keyboard()
                         ,parse_mode="MarkdownV2")



@router.message(Command("menu"))
async def on_menu(message: Message):
    await message.answer('Команды:\n/start - запуск и т д')

@router.message(Command("users"))
async def on_users(message: Message):
    users = await get_users()

    if not users:
        await message.answer("В базе нет пользователей")
        return

    text = "Пользователи в базе:\n\n"
    for l1,l2,l3 in users:
        text += f"- {l1} - {l2} - {l3}"
    await message.answer(text)