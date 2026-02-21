import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Создаем инлайн клавиатуру с кнопкой
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🔐 Перейти на сайт",
                url=Config.WEB_APP_URL
            )]
        ]
    )
    
    text = (
        "👋 Добро пожаловать!\n\n"
        "Нажмите кнопку ниже, чтобы пройти верификацию:"
    )
    
    await message.answer(text, reply_markup=keyboard)

async def main():
    print("🤖 Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())