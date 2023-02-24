import sys

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_buttons import *

sys.path.insert(1, '/Users/annabutko/Documents/python_projects/News_Data_requests/')
import news_flask
from loader import dp, bot, logger


def check_user_input(update, context):
    user_input = update.message.text
    user_data = context.user_data
    return user_data


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Welcome! You can request news information here!",
                         reply_markup=choice)


# ------------GET-------------
@dp.callback_query_handler(text="get")
async def getting_news(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer("You selected 'Get News'", reply_markup=get_keyboard)


def counter_get_all_articles():
    counter_get_all_articles.counter += 10
    return counter_get_all_articles.counter


counter_get_all_articles.counter = 0


@dp.callback_query_handler(text="get_all_articles")
async def get_all_articles(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    load_more = counter_get_all_articles()
    articles = news_flask.return_all_titles()
    for article in articles[load_more - 10:load_more]:
        await call.message.answer(article)
    await call.message.answer('Select Next:', reply_markup=get_keyboard_continue)


@dp.callback_query_handler(text="get_category")
async def get_all_articles(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer("You selected 'Get Articles by Category'. Please Select your Category:",
                              reply_markup=get_category_keyboard)


def counter_post_chatGPT():
    counter_post_chatGPT.counter += 10
    return counter_post_chatGPT.counter


counter_post_chatGPT.counter = 0


def counter_post_bitcoin():
    counter_post_bitcoin.counter += 10
    return counter_post_bitcoin.counter


counter_post_bitcoin.counter = 0


def counter_post_ai():
    counter_post_ai.counter += 10
    return counter_post_ai.counter


counter_post_ai.counter = 0


@dp.callback_query_handler(text=['get_chatGPT', 'get_bitcoin', 'get_ai'])
async def get_all_articles(call: CallbackQuery):
    await call.answer(cache_time=60)

    global category_load
    category_load = call.data

    logger.info(f"{category_load=}")

    if category_load == 'get_chatGPT':
        load_more = counter_post_chatGPT()
    elif category_load == 'get_bitcoin':
        load_more = counter_post_bitcoin()
    else:
        load_more = counter_post_ai()

    articles = news_flask.articles_from_collection(category_load.split('_')[1])
    if not articles[load_more - 10:load_more]:
        await call.message.answer('No More Articles are available. Select Next option from the List:',
                                  reply_markup=get_end)
    else:
        for article in articles[load_more - 10:load_more]:
            await call.message.answer(article)
        await call.message.answer('Next:', reply_markup=get_post_continue)


@dp.callback_query_handler(text=['load_more_category'])
async def get_all_articles_continue(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    if category_load == 'get_chatGPT':
        load_more = counter_post_chatGPT()
    elif category_load == 'get_bitcoin':
        load_more = counter_post_bitcoin()
    else:
        load_more = counter_post_ai()
    articles = news_flask.articles_from_collection(category_load.split('_')[1])
    if not articles[load_more - 10:load_more]:
        await call.message.answer('No More Articles are available. Select Next option from the List:',
                                  reply_markup=get_end)
    else:
        for article in articles[load_more - 10:load_more]:
            await call.message.answer(article)
        await call.message.answer('Next:', reply_markup=get_post_continue)


@dp.callback_query_handler(text=['get_content'])
async def pick_category(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer("Pick Your Category:", reply_markup=get_content_keyboard)


@dp.callback_query_handler(text=['content_chatGPT', 'content_bitcoin', 'content_ai'])
async def get_content(call: CallbackQuery):
    await call.answer(cache_time=60)

    global category_get_content
    category_get_content = call.data.split('_')[1]
    logger.info(f"{get_content=}")

    await call.message.answer(
        f"You selected {category_get_content.upper()} collection. Enter the Number of the Article to view Content:")

    @dp.message_handler(content_types=['text'])
    async def get_article_index_content(msg: Message):
        index = msg.text

        response = news_flask.article_from_collection_by_index(category_get_content, int(index))
        await call.message.answer(response[:4096], reply_markup=get_content_continue)


# --------------------------------


# -------------POST--------------
@dp.callback_query_handler(text='post')
async def posting_news(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer("You selected 'Post News'", reply_markup=post_keyboard)


@dp.callback_query_handler(text='post_all_articles')
async def add_all(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer(
        'Searching for new News Articles.\nPlease do not click any buttons, this can take up to several minutes.')
    response = news_flask.run_program()
    await call.message.answer(response, reply_markup=post_all_articles_continue)


@dp.callback_query_handler(text='post_category')
async def add_category(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer("You selected 'Post Articles by Category'. Please Select your Category",
                              reply_markup=post_category_keyboard)


@dp.callback_query_handler(text=['post_chatGPT', 'post_bitcoin', 'post_ai'])
async def post_articles_by_category(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    callback_data = call.data.split('_')[1]
    await call.message.answer(
        f'Searching for new {callback_data.upper()} News Articles.\nPlease do not click any buttons, this can take up to several minutes.')
    response = news_flask.run_program_by_collection(callback_data)
    await call.message.answer(response, reply_markup=post_all_articles_continue)


# --------------------------------


# ------------DELETE-------------
@dp.callback_query_handler(text="delete")
async def deleting_news(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer("You selected 'Delete News'.\nPlease Select a Category", reply_markup=delete_keyboard)


@dp.callback_query_handler(text=['delete_chatGPT', 'delete_bitcoin', 'delete_ai'])
async def delete_articles(call: CallbackQuery):
    await call.answer(cache_time=60)

    global delete_callback_data
    delete_callback_data = call.data.split('_')[1]
    logger.info(f"{delete_callback_data=}")

    await call.message.answer(
        f"You selected {delete_callback_data.upper()} collection. Enter the Number of the Article you would like to Delete.")

    @dp.message_handler(content_types=['text'])
    async def get_article_index_delete(msg: Message):
        index = msg.text

        response = news_flask.delete_item(delete_callback_data, int(index))
        await call.message.answer(response, reply_markup=delete_keyboard_continue)


# --------------------------------


# ------------RETURN-------------
@dp.callback_query_handler(text=['exit'])
async def exit(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer("Good Bye!")
    await call.answer("Good Bye!", show_alert=True)
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text=['return'])
async def go_back(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logger.info(f"{callback_data=}")

    await call.message.answer(text="Choose from options below:", reply_markup=choice)
# --------------------------------
