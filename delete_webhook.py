import os
from telegram import Bot

# Если у тебя переменная окружения называется TOKEN, берем её:
TOKEN = os.getenv("TOKEN")

# Если хочешь вставить токен прямо в код, раскомментируй и замени строку выше:
# TOKEN = "7973405224:AAF8fZHZtSp7Yot9xOoVRvdnoejHWoKFhBA"

def delete_webhook():
    bot = Bot(token=TOKEN)
    bot.delete_webhook(drop_pending_updates=True)
    print("Webhook удалён, все накопленные апдейты сброшены.")

if __name__ == "__main__":
    delete_webhook()
