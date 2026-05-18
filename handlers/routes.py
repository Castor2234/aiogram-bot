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

router = Router()


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
                                      "• Абонемент мэра+ - 2199 руб - 82 BYN\n"
                                      "Все другие акции тоже покупаются!"),
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



# Отсюда начинаются команды

@router.message(Command("start"))
async def on_start(message: Message):
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
    await message.answer_photo(media=FSInputFile("Images/redline_shop_1.png"),
                              caption="Для просмотра цен на донаты нажмите на кнопку <b>Каталог</b> под сообщением 😎\n"
                                      "\n"
                                      'Чтобы купить донат напишите <a href="https://t.me/Mobile_Game_YT1">Артуру</a> в лс название доната и способ, которым вы хотите его купить. \n'
                                      '\n'
                                      'Для покупки акции, которой нет в списке, скиньте <b>фото/скриншот</b> акции <a href="https://t.me/Mobile_Game_YT1">Артуру</a> в лс.',
                              reply_markup=start_inline_keyboard(),
                              parse_mode="HTML")