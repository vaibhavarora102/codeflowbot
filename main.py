import constant as keys
# from python-telgram-bot import *
import responses as R
from telegram.ext import Updater, CommandHandler, CallbackContext

def start_command(update, context):
    
    update.message.reply_text("Hey, DSA bootcamp is going to start from 1st of June, \n for registrationfill the form https://forms.gle/BHbAqkCnAViVkeF76 ")

def anyupdate_command(update, context):
    
    update.message.reply_text("""Currently we are going to organise the 4 week bootcamp \n
    \n
     We will be starting bootcamp from 1st june, shortly will be updating you with the whole Schedule
     \n if any community wants to collaborate could dm any of the admin of the group :)     
     """)

def codeflow(update, context):
    
    update.message.reply_text("""
        Codeflow is a students driven organization running for students empowerment \n
        We are currently working in three domains: \n
        1. Open-Source \n
        2. Content Delivery \n
        3. Community building and networking \n
        \n 
        We belive in strengthening the skills of each other while learning in community.

     """)
def Welcome(update, context):
    
    update.message.reply_text("""
        Thanks for calling bot: let me know How can I help you \n
        
        Here is what can I do and How?\n
        /codeflow   to know about codeflow\n
        /dsaform    to get regestration form DSA bootcamp\n
        /update     to know about updates\n
        /handles    to get the link of all codeflow handles\n
     """)

def handles(update, context):
    
    update.message.reply_text("""
        You can find all the links of codeflow here: \n
        https://linktr.ee/codefloworg
     """)

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)
    update.message.reply_text(response)


def error(update, context):
    print("error")

def main():
    updater = Updater(keys.API_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", Welcome))
    dp.add_handler(CommandHandler("codeflow", codeflow))
    dp.add_handler(CommandHandler("update", anyupdate_command))
    dp.add_handler(CommandHandler("dsaform", start_command))
    dp.add_handler(CommandHandler("handles", handles))

    updater.start_polling()
    updater.idle()

main()