import asyncio
from src.settings import BOT_TOKEN
from src.handlers import user_handlers
from src.keyboards.main_menu import set_main_menu
from aiogram import Bot, Dispatcher
import logging

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    await set_main_menu(bot)

    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
