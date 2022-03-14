import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.filters.start import IsPrivate
from tgbot.filters.test_filter import SomeF
from tgbot.handlers.admin import register_admin
from tgbot.handlers.answer import register_answer
from tgbot.handlers.echo import register_echo
from tgbot.handlers.error_handler import register_errors_handler
from tgbot.handlers.start import register_bot_start
from tgbot.handlers.testing import register_testing
from tgbot.handlers.user import register_user
from tgbot.middlewares.big_brother import BigBrother
from tgbot.middlewares.db import DbMiddleware
from tgbot.middlewares.throttling import ThrottlingMiddleware

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    dp.setup_middleware(DbMiddleware())
    dp.setup_middleware(BigBrother())
    dp.setup_middleware(ThrottlingMiddleware())


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(SomeF)


def register_all_handlers(dp):
    # register_admin(dp)
    register_bot_start(dp)
    register_user(dp)
    register_testing(dp)

    register_answer(dp)
    register_echo(dp)
    register_errors_handler(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
