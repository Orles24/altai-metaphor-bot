import os
import random
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InputFile
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.token import TokenValidationError

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

CARDS_DIR = "cards"

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет 🌿\n\nЭто бот с метафорической колодой Алтая.\n\nНажми /card, чтобы вытянуть карту.")

@dp.message(Command("card"))
async def card_handler(message: types.Message):
    cards = os.listdir(CARDS_DIR)
    card_file = random.choice(cards)
    photo = InputFile(os.path.join(CARDS_DIR, card_file))
    await message.answer_photo(photo)

async def main():
    try:
        await dp.start_polling(bot)
    except TokenValidationError:
        print("❌ Неверный токен. Проверь BOT_TOKEN в настройках окружения!")

if __name__ == "__main__":
    asyncio.run(main())
