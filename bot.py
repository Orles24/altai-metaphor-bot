
import os
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

CARDS_DIR = "cards"

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет 🌿\n\nЭто бот с метафорической колодой Алтая.\n\nНажми /card, чтобы вытянуть карту.")

@dp.message_handler(commands=['card'])
async def send_card(message: types.Message):
    cards = os.listdir(CARDS_DIR)
    card_file = random.choice(cards)
    photo = InputFile(os.path.join(CARDS_DIR, card_file))
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

if __name__ == '__main__':
    executor.start_polling(dp)
