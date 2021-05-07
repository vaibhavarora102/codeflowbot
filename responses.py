import constant as keys
# from python-telgram-bot import *
import responses as R
# from mk.telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

def start_command(update, context):
    update.message.reply_text('type something')

def help_command(update, context):
    update.message.reply_text('type something --- 2')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)


def error(update, context):
    print("error")

def main():
    updater = Updater(keys.API_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling(60)
    updater.idle()

main()