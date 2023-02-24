from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import get_callback

# FIRST CHOICE KEYBOARD
choice = InlineKeyboardMarkup(row_width=1)

get_news = InlineKeyboardButton(text="Get News", callback_data='get')
choice.insert(get_news)

post_news = InlineKeyboardButton(text="Post News", callback_data='post')
choice.insert(post_news)

delete_news = InlineKeyboardButton(text="Delete News", callback_data='delete')
choice.insert(delete_news)

exit = InlineKeyboardButton(text="Exit", callback_data='exit')
choice.insert(exit)

# GET KEYBOARD
get_keyboard = InlineKeyboardMarkup(row_width=1)

get_keyboard.insert(InlineKeyboardButton(text='Get all Artciles', callback_data='get_all_articles'))
get_keyboard.insert(InlineKeyboardButton(text='Get Articles by Category', callback_data='get_category'))
get_keyboard.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))

get_category_keyboard = InlineKeyboardMarkup(row_width=1)

get_category_keyboard.insert(InlineKeyboardButton(text='chatGPT', callback_data='get_chatGPT'))
get_category_keyboard.insert(InlineKeyboardButton(text='bitcoin', callback_data='get_bitcoin'))
get_category_keyboard.insert(InlineKeyboardButton(text='ai', callback_data='get_ai'))
get_category_keyboard.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))


get_keyboard_continue = InlineKeyboardMarkup(row_width=1)

get_keyboard_continue = InlineKeyboardMarkup(row_width=1)
get_keyboard_continue.insert(InlineKeyboardButton(text='Load More', callback_data='get_all_articles'))
get_keyboard_continue.insert(InlineKeyboardButton(text='Get Content', callback_data='get_content'))
get_keyboard_continue.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))

get_content_keyboard = InlineKeyboardMarkup(row_width=1)

get_content_keyboard.insert(InlineKeyboardButton(text='chatGPT', callback_data='content_chatGPT'))
get_content_keyboard.insert(InlineKeyboardButton(text='bitcoin', callback_data='content_bitcoin'))
get_content_keyboard.insert(InlineKeyboardButton(text='ai', callback_data='content_ai'))
get_content_keyboard.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))


get_content_continue = InlineKeyboardMarkup(row_width=1)

get_content_continue.insert(InlineKeyboardButton(text='Get Content', callback_data='get_content'))
get_content_continue.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))

get_post_continue = InlineKeyboardMarkup(row_width=1)

get_post_continue.insert(InlineKeyboardButton(text='Load More', callback_data='load_more_category'))
get_post_continue.insert(InlineKeyboardButton(text='Get Content', callback_data='get_content'))
get_post_continue.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))

get_end = InlineKeyboardMarkup(row_width=1)
get_end.insert(InlineKeyboardButton(text='Get Content', callback_data='get_content'))
get_end.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))

#POST KEYBOARDS
post_keyboard = InlineKeyboardMarkup(row_width=1)

post_keyboard.insert(InlineKeyboardButton(text='Add Articles from all Categories', callback_data='post_all_articles'))
post_keyboard.insert(InlineKeyboardButton(text='Add Articles by Category', callback_data='post_category'))
post_keyboard.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))

post_all_articles_continue = InlineKeyboardMarkup(row_width=1)

post_all_articles_continue.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))

post_category_keyboard = InlineKeyboardMarkup(row_width=1)

post_category_keyboard.insert(InlineKeyboardButton(text='chatGPT', callback_data='post_chatGPT'))
post_category_keyboard.insert(InlineKeyboardButton(text='bitcoin', callback_data='post_bitcoin'))
post_category_keyboard.insert(InlineKeyboardButton(text='ai', callback_data='post_ai'))
post_category_keyboard.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))

#DELETE KEYBOARD
delete_keyboard = InlineKeyboardMarkup(row_width=1)

delete_keyboard.insert(InlineKeyboardButton(text='chatGPT', callback_data='delete_chatGPT'))
delete_keyboard.insert(InlineKeyboardButton(text='bitcoin', callback_data='delete_bitcoin'))
delete_keyboard.insert(InlineKeyboardButton(text='ai', callback_data='delete_ai'))
delete_keyboard.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))


delete_keyboard_continue = InlineKeyboardMarkup(row_width=1)

delete_keyboard_continue.insert(InlineKeyboardButton(text='Delete News', callback_data='delete'))
delete_keyboard_continue.insert(InlineKeyboardButton(text='Go Back', callback_data='return'))
