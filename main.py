import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Filters, MessageHandler

# الحصول على التوكن من متغير البيئة
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# دالة للتعامل مع الأمر /start
def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Play Game", url='https://your-game-url.com')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome! Click the button below to play the game:', reply_markup=reply_markup)

# دالة لمعالجة الرسائل النصية الأخرى (اختياري)
def handle_message(update: Update, context: CallbackContext):
    if update.message.text.lower() == 'play':
        update.message.reply_text('You can start the game by clicking the "Play Game" button.')

# إعداد البوت
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # تعيين معالجات الأوامر والرسائل
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
