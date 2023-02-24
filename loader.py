from aiogram import Bot, Dispatcher
import config
import logging
from logging.handlers import SysLogHandler

PAPERTRAIL_HOST = 'logs5.papertrailapp.com'
PAPERTRAIL_PORT = 14909

logger = logging.getLogger("news_telegram_bot")
logger.setLevel(logging.INFO)
handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
logger.addHandler(handler)

logger.info("Telegram BOT running.")


bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)
