
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    FSInputFile,
    InputMediaPhoto,
    BufferedInputFile
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramRetryAfter, TelegramForbiddenError
from handlers.inline_keyboards import *

from asyncio import sleep

import logging

from os import getenv
from dotenv import load_dotenv
load_dotenv()
ADM_IDS=getenv('ADMIN_ID')


import aiosqlite

# --- База данных

DB_NAME = "redlinebot.sql"
DB_MESSAGES_NAME = "messages.sql"

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
    async with aiosqlite.connect(DB_MESSAGES_NAME) as db1:
        await db1.execute("""
                        CREATE TABLE IF NOT EXISTS messages (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        full_name TEXT,
                                        message TEXT
                        )
                        """)
        await db1.commit()

async def add_message_to_db(full_name: str, message_text: str):
    async with aiosqlite.connect(DB_MESSAGES_NAME) as db:
        await db.execute(
            "INSERT INTO messages (full_name, message) VALUES (?, ?)",
            (full_name, message_text)
        )
        await db.commit()

async def get_messages():
    async with aiosqlite.connect(DB_MESSAGES_NAME) as db:
        cursor = await db.execute("SELECT full_name, message FROM messages")
        result = await cursor.fetchall()
        return result

async def add_user(user_id, full_name):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT OR IGNORE INTO users (user_id, full_name) VALUES(?, ?)", (user_id,full_name))
        await db.commit()

async def remove_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DELETE FROM users WHERE user_id = ?",(user_id,))
        await db.commit()


async def get_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT COUNT(DISTINCT id) FROM users")
        result = await cursor.fetchall()
        return result


async def get_chats():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT user_id FROM users")
        result = await cursor.fetchall()

        if not result:
            return 0

        chats = []
        for i in result:
            chats.append(i[0])
        return chats


# --- Конец базы данных

router = Router()

# --- FSM context machine начало

class Form(StatesGroup):
    br_message = State()
    yes_or_no = State()

# --- FSM context machine конец


# Тут начинаются callback_query

@router.callback_query(lambda c: c.data == "menu")
async def on_menu(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/redline_shop_1.png"),
                              caption="Для просмотра цен на донаты нажмите на кнопку <b>Каталог</b> под сообщением 😎\n"
                                      "\n"
                                      'Чтобы купить донат напишите <a href="https://t.me/Mobile_Game_YT1">Артуру</a> в лс название доната и способ, которым вы хотите его купить. \n'
                                      '\n'
                                      'Для покупки акции, которой нет в списке, скиньте <b>фото/скриншот</b> акции <a href="https://t.me/Mobile_Game_YT1">Артуру</a> в лс.',
                              parse_mode="HTML"),
        reply_markup=start_inline_keyboard()
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "catalog")
async def on_catalog(callback: CallbackQuery):
    # if callback.data == ""
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/redline_shop_1.png"),
                              caption="<b>Выберите игру из каталога товаров:</b>",
                              parse_mode="HTML"),
        reply_markup=catalog_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "clash_royal")
async def on_brawl_67(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/clash_royale.jpg"),
                              caption="🤩 Новый сезон в Clash Royale 🤩\n"
                                      "\n"
                                      "Способы покупки Pass Royale:\n"
                                      "📩 Заходом по почте и коду:\n"
                                      "• Pass Royale — 2399 ₽ / 90 BYN\n"
                                      "🛒 Через Supercell Store:\n"
                                      "• Pass Royale — 2599 ₽ / 97 BYN\n"
                                      "🎁 Подарком через Supercell ID:\n"
                                      "• Pass Royale — 3299 ₽ / 125 BYN\n"
                                      "\n"
                                      "Для покупки любой другой акции отправьте фото акции <a href='https://t.me/Mobile_Game_YT1'>Артуру</a> при покупке"
                                      ,parse_mode="HTML"),
        reply_markup=backward_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "sim_city")
async def on_brawl_67(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/SimCity.jpg"),
                              caption="👊Новый Пропуск в Sim City Buildit👊"
                                      "\n"
                                      "• Абонемент мэра - 1399 руб - 52 BYN\n"
                                      "Абонемент мэра+ - 2199 руб - 82 BYN\n"
                                      "Повышение сезонной валюты - 1899 руб - 74 byn\n"
                                      '\n'
                                      '• Элитный абонемент By 1 - 1199 руб - 45 BYN \n'
                                      'Элитный абонемент By 2 - 1999 руб - 80 BYN \n'
                                      'Элитный абонемент By 3 - 3599 руб - 137 BYN \n'
                                      '\n'
                                      '• 250 SimCash - 1199 руб - 45 BYN\n'
                                        '550 SimCash - 2199 руб - 82 BYN\n'
                                        '1300 SimCash - 3999 руб - 148 BYN\n'
                                        '2625 SimCash - 7499 руб - 277 BYN\n'
                                        '4000 SimCash - 10499 руб - 387 BYN\n'
                                        '8500 SimCash - 18999 руб - 698 BYN\n'
                                      '\n'
                                      '• 1800 Симолеоны - 599 руб - 23 BYN\n'
                                        '19.200 Симолеоны - 1499 руб - 56 BYN\n'
                                        '68.000 Симолеоны - 3399 руб - 125 BYN\n'
                                        '129.600 Симолеоны - 5499 руб - 203 BYN\n'
                                        '228.000 Симолеоны - 8499 руб - 313 BYN\n'
                                        '480.000 Симолеоны - 12999 руб - 479 BYN\n'
                                      "Любые другие акции также доступны для покупки"
                                      ),
        reply_markup=backward_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "brawl")
async def on_brawl_stars(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/brawlgems.jpg"),
                              caption='Заходом на аккаунт через почту:\n'
                            '• Бравл Пасс - 1799 руб - 70 BYN\n'
                            '• Бравл Пасс Плюс - 2599 руб - 100 BYN\n'
                            '• Улучшение до Бравл Пасс Плюс - 999 руб - 40 BYN\n'
                            '• Про Пасс - 4999 руб - 190 BYN\n'
                            '\n'
                            'Через Supercell Store:\n'
                            '• Brawl Pass - 1999 руб - 80 BYN\n'
                            '• Brawl Pass Plus - 2899 руб - 112 BYN\n'
                            '• Про Пасс - 5499 руб - 210 BYN\n'
                            '\n'
                            'Подарком через Supercell Id:\n'
                            '• Brawl Pass Plus - 3999 руб - 151 BYN\n'
                            '• Про Пасс - 6999 руб - 265 BYN\n'
                            '• 30 гемов - 449 руб - 18 BYN\n'
                            '• 80 гемов - 999 руб - 38 BYN\n'
                            '• 170 гемов - 1999 руб - 75 BYN\n'
                            '• 360 гемов - 3937 руб - 147 BYN\n'
                            '• 950 гемов - 9907 руб - 365 BYN\n'
                            '• 2000 гемов - 19927 руб - 735 BYN\n'
                            '\n'
                            'Для покупки любой другой акции отправьте фото акции <a href="https://t.me/Mobile_Game_YT1">Артуру</a> при покупке',
                              parse_mode="HTML"
                              ),
        reply_markup=brawl_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "67brawl")
async def on_brawl_67(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/67meme.jpg"),
                              caption="67 гемов - 967 руб"),
        reply_markup=back_to_brawl_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "stalker2")
async def on_brawl_stars(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/stalker2.jpg"),
                              caption='Хочешь купить S.T.A.L.K.E.R. 2: Heart of Chornobyl в России или Беларуси? Поможем быстро оформить игру на твой Steam-аккаунт или создадим новый аккаунт с нужным регионом.\n'
                            'Цены:\n'
                            '• Standard Edition — 8999 ₽ - 350 BYN\n'
                            '• Deluxe Edition — 12499 ₽ - 480 BYN\n'
                            '• Ultimate Edition — 15999 ₽ - 595 BYN\n'
                            '\n'
                            '<b>Для покупки необходимо:</b>\n'
                            '• Сменить регион вашего Steam-аккаунта 1999 ₽ / 75 BYN\n\n'
                            'или\n\n'
                            '• Создать новый Steam-аккаунт с нужным регионом на ваши данные:\n'
                            '1499 ₽ / 58 BYN — при покупке игры\n'
                            '1799 ₽ / 68 BYN — без покупки игры\n',
                              parse_mode="HTML"
                              ),
        reply_markup=backward_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "tiktok")
async def on_tiktok(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/tiktok.jpg"),
                              caption="""
Валюта:
• 70 монет - 799 руб - 31 BYN
• 330 монет - 1599 руб - 61 BYN
• 660 монет - 2799 руб - 106 BYN
• 1321 монет - 4999 руб - 188 BYN
• 3500 монет - 12499 руб - 465 BYN
• 7000 монет - 24999 руб - 920 BYN

<b>Возможна покупка любого количества, при большем количестве лучше курс</b>
""",
                              parse_mode="HTML"
                              ),
        reply_markup=backward_inline_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "telegram")
async def on_telegram(callback: CallbackQuery):
    await callback.message.edit_media(
        media=InputMediaPhoto(media=FSInputFile("Images/telegram.jpg"),
                              caption="""
Звезды по id - @ или подарком:
• 50 звезд - 699 руб - 25 BYN
• 100 звезд - 800 руб - 32 BYN
• 150 звезд - 1199 руб - 46 BYN
• 250 звезд - 1749 руб - 68 BYN
• 500 звезд - 2999 руб - 117 BYN
• 1000 звезд - 5999 руб - 225 BYN
• 2500 звезд - 12499 руб - 470 BYN
• 5000 звезд - 24999 руб - 935 BYN

<b>Возможна покупка любого количества, при большем количестве лучше курс</b>

Telegram премиум:
• 1 месяц заходом - 1499 руб - 55 BYN
Подарком:
• 3 месяца  - 3999 руб - 150 BYN
• 6 месяца - 4999 руб - 188 BYN
• 1 год - 9999 руб - 375 BYN

• Буст Telegram каналов: 5 шт 1 месяц - 1499 руб - 55 BYN
Подробнее, любое кол-во и срок обговариваемый в лс

Всё необходимое для вашего Telegram — в одном месте 💙
⭐️ Telegram Stars — покупайте звёзды для подарков, оплаты контента и сервисов внутри Telegram.
💎Telegram Premium — больше возможностей, повышенные лимиты, эксклюзивные функции и оформление.
🚀Telegram Бусты — прокачивайте каналы и открывайте дополнительные возможности.
""",
                              parse_mode="HTML"
                              ),
        reply_markup=backward_inline_keyboard()
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

@router.message(Command("catalog"))
async def on_catalog_command(message: Message):
    await message.answer_photo(photo=FSInputFile("Images/redline_shop_1.png"),
                               caption='<b>Выберите игру из каталога товаров:</b>',
                               reply_markup=catalog_inline_keyboard(),
                               parse_mode="HTML")

@router.message(Command("menu"))
async def on_menu_command(message: Message):
    await message.answer_photo(photo=FSInputFile("Images/redline_shop_1.png"),
                              caption="Для просмотра цен на донаты нажмите на кнопку <b>Каталог</b> под сообщением 😎\n"
                                      "\n"
                                      'Чтобы купить донат напишите <a href="https://t.me/Mobile_Game_YT1">Артуру</a> в лс название доната и способ, которым вы хотите его купить. \n'
                                      '\n'
                                      'Для покупки акции, которой нет в списке, скиньте <b>фото/скриншот</b> акции <a href="https://t.me/Mobile_Game_YT1">Артуру</a> в лс.',
                              reply_markup=start_inline_keyboard(),
                              parse_mode="HTML")

@router.message(Command("users"))
async def on_users(message: Message):
    if str(message.from_user.id) in ADM_IDS:
        users = await get_users()

        if not users:
            await message.answer("В базе нет пользователей")
            return
        await message.answer('Количество пользователей в базе:\n' + str(users[0][0]))
    else:
        await message.answer("Нет доступа к админ панели")

@router.message(Command("messages"))
async def on_messages(message: Message):
    if str(message.from_user.id) in ADM_IDS:
        rows = await get_messages()

        if not rows:
            await message.answer("В базе нет сообщений")
            return

        content = "\n".join(f"{full_name}: {text}" for full_name, text in rows)
        file = BufferedInputFile(content.encode("utf-8"), filename="messages.txt")

        await message.answer_document(
            document=file,
            caption=f"Всего сообщений: {len(rows)}"
        )
    else:
        await message.answer("Нет доступа к админ панели")

# Broadcast начало

@router.message(Command("broadcast"))
async def on_broadcast(message: Message,state: FSMContext):
    if str(message.from_user.id) in ADM_IDS:
        await message.answer('Введите сообщение, которое будет переслано всем пользователям бота.')
        await state.set_state(Form.br_message)
    else:
        await message.answer("Нет доступа к админ панели")


@router.message(Form.br_message)
async def broadcast_message(message: Message,state: FSMContext):
    await state.update_data(br_id=message.message_id)
    await message.copy_to(chat_id=message.chat.id)
    await message.answer('<b>Вы уверены, что хотите переслать это сообщение? Напишите Рассылка, если уверены.</b>',parse_mode='HTML')
    await state.set_state(Form.yes_or_no)

@router.message(Form.yes_or_no)
async def broadcast_confirm(message: Message,state: FSMContext):
    if message.text.lower() != 'рассылка':
        await message.answer(f'Рассылка не была подтверждена. {message.text.lower()}')
        await state.clear()
    else:
        data = await state.get_data()
        br_text_id = data.get('br_id')
        await state.clear()
        chats = await get_chats()
        count=0
        remove_count=0
        await message.answer('Рассылка в процессе...')
        for user_id in chats:
            try:
                await message.bot.copy_message(chat_id=user_id, from_chat_id=message.chat.id,message_id=br_text_id)
                count+=1
                await sleep(0.05)
            except TelegramForbiddenError:
                logging.warning(f"Target [ID:{user_id}]: blocked by user. Removing from DB.")
                await remove_user(user_id)
                remove_count+=1



            except TelegramRetryAfter as e:
                logging.error(f"Target [ID:{user_id}]: Flood limit hit. Sleeping for {e.retry_after}s")
                await sleep(e.retry_after)

                try:
                    await message.bot.copy_message(chat_id=user_id, from_chat_id=message.chat.id,message_id=br_text_id)
                    count += 1
                except Exception:
                    logging.error(f"Target [ID:{user_id}]: Second attempt failed.")

            except Exception as e:
                logging.error(f"Target [ID:{user_id}]: Failed to send message. Error: {e}")


        await message.answer(f"Рассылка завершена. Сообщение успешно отправлено {count} пользователям. Из базы данных удалено {remove_count} пользователей.")


# Broadcast конец


@router.message()
async def on_any_message(message: Message):
    await add_message_to_db(message.from_user.full_name, message.text)