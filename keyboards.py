from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from database import *


def phone_button():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text="Send the telefon nomber ☎", request_contact=True)]
    ], resize_keyboard=True)


def generate_main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='✅ Place an Order')],
        [KeyboardButton(text='📜  History'), KeyboardButton(text='🛒 Cart'), KeyboardButton(text='📍 Location')]
    ], resize_keyboard=True)


def generate_category_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(
        InlineKeyboardButton(text='MENU 📒', url='https://telegra.ph/Fast-Food-11-30')
    )

    categories = get_all_categories()
    buttons = []
    for category in categories:
        btn = InlineKeyboardButton(text=category[1], callback_data=f'category_{category[0]}')
        buttons.append(btn)
    markup.add(*buttons)
    return markup


def products_by_category(category_id):
    markup = InlineKeyboardMarkup(row_width=2)
    products = get_products_by_category(category_id)
    buttons = []
    for product in products:
        btn = InlineKeyboardButton(text=product[1], callback_data=f'product_{product[0]}')
        buttons.append(btn)
    markup.add(*buttons)
    markup.row(
        InlineKeyboardButton(text='⬅️Back', callback_data='main_menu')
    )
    return markup


def generate_product_detail_menu(product_id, category_id):
    markup = InlineKeyboardMarkup(row_width=3)
    numbers = [i for i in range(1, 10)]
    buttons = []
    for number in numbers:
        btn = InlineKeyboardButton(text=str(number), callback_data=f'cart_{product_id}_{number}')
        buttons.append(btn)

    markup.add(*buttons)
    markup.row(
        InlineKeyboardButton(text='⬅️Back', callback_data=f'back_{category_id}')
    )
    return markup


def generate_cart_menu(cart_id):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text='🚀 Order confirmation', callback_data=f'order_{cart_id}')
    )

    cart_products = get_cart_product_for_delete(cart_id)

    for cart_product_id, product_name in cart_products:
        markup.row(
            InlineKeyboardButton(text=f'❌ {product_name}', callback_data=f'delete_{cart_product_id}')
        )
    return markup