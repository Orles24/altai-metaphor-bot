from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from keep_alive import keep_alive
import os
import random

TOKEN = os.getenv("TOKEN")
CARDS_DIR = "cards"
cards = [os.path.join(CARDS_DIR, f) for f in os.listdir(CARDS_DIR) if f.endswith(".jpg")]

user_draw_counts = {}

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("🔮 Вытянуть карту", callback_data="draw_card")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "🏔 Здесь ты можешь познакомиться с метафорической колодой, "
        "основанной на реальных локациях Алтая.\n\n"
        "Каждая карта — это не просто изображение, а символ, отклик, подсказка, "
        "возможность услышать ответ и задуматься о жизни 💭\n\n"
        "Нажимай на кнопку и смотри, что хочет сказать тебе Алтай.\n\n👇",
        reply_markup=reply_markup
    )

def draw_card(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    user_draw_counts[user_id] = user_draw_counts.get(user_id, 0) + 1
    count = user_draw_counts[user_id]

    card_path = random.choice(cards)

    keyboard = [
        [InlineKeyboardButton("🔮 Вытянуть ещё", callback_data="draw_card")],
        [InlineKeyboardButton("☁️ Связаться с автором", url="https://t.me/Orles_24")]
    ]

    if count % 5 == 0:
        keyboard.append([InlineKeyboardButton("☕ Поблагодарить автора", callback_data="thank_author")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    with open(card_path, 'rb') as photo:
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=photo,
            caption="Вот карта, которая откликнулась тебе ✨",
            reply_markup=reply_markup
        )

def thank_author(update: Update, context: CallbackContext):
    update.callback_query.answer()
    update.callback_query.message.reply_text(
        "Хочешь отблагодарить автора?\n\n"
        "Можно скинуть на кофе ☕ по номеру:\n89131060927 (Т-Банк)\n\n"
        "Спасибо за интерес к колоде 🙌"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(draw_card, pattern="^draw_card$"))
    dp.add_handler(CallbackQueryHandler(thank_author, pattern="^thank_author$"))
    updater.start_polling()
    updater.idle()

# Запуск Flask + бота
keep_alive()
main()
