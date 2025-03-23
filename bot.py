import os
import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

CARDS_DIR = "cards"

@dp.message(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Привет 🌿\n\nЭто бот с метафорической колодой Алтая.\n\nНажми /card, чтобы вытянуть карту.")

@dp.message(commands=["card"])
async def send_card(message: types.Message):
    cards = os.listdir(CARDS_DIR)
    card_file = random.choice(cards)
    photo = InputFile(os.path.join(CARDS_DIR, card_file))
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
