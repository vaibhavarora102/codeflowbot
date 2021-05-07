import constant as keys
# from python-telgram-bot import *
import responses as R
from telegram.ext import Updater, CommandHandler, CallbackContext

def start_command(update, context):
    line = "Hey, DSA bootcamp is going to start from 1st of June, \n for registrationfill the form https://forms.gle/BHbAqkCnAViVkeF76 "
    update.message.reply_text(line)

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

    updater.start_polling(0)
    updater.idle()

main()