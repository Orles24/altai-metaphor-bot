import os
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import InputFile
from aiogram.client.default import DefaultBotProperties

TOKEN = os.getenv("BOT_TOKEN")

# Новый способ задания параметров бота
bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

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
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
