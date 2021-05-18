import constant as keys
# from python-telgram-bot import *
import responses as R
from telegram.ext import Updater, CommandHandler, CallbackContext

def start_command(update, context):
    
    update.message.reply_text(""" https://forms.gle/BHbAqkCnAViVkeF76 \n

So, Finally wait is over 🎉Codeflow is going to organize 4 weeks of DSA Bootcamp for the students 👩‍🎓 to bridge  the gap between knowledge and practical implemenation 🎓 caused due to pandemic   by providing mentorship 🥳🥳 from experts to students willing to learn and grow with the community. 

💯📌\n \n
Join telegram to be part of it: https://lnkd.in/dkBEsNS \n


Stay tuned for more updates !\n
Perks:  \n
1. Mentorship for 4 weeks \n
2. DSA contest at end of the program \n
3. Goodies to top 5 in coding competition  \n
4. More (based on collaborations) 🙌 \n """)

def anyupdate_command(update, context):
    update.message.reply_text("""
    📌 Schedule is updated, Do check it out by using /schedule \n
    📌 Cash prizes and more goodies are introduced during Bootcamp\n
    📌 Whole Bootcamp will be in the form of Live lectures of Codeflow youtube channel 
    ( https://www.youtube.com/c/codefloworg )\n
    📌 Live lectures will have the duration of 2 hours (approx) each\n
    📌 Most of the lectures are Scheduled from 7 p.m to 9 p.m (it may vary acc. to mentor)\n  
    """)

def group_command(update, context):
    update.message.reply_text("""
    📌 To make your experience even more better, we welcome your suggestion (in nicely presented way)\n
    📌 Don't ask same questions again and again\n
    📌 Be helpful in group (try to help each other, as this is what we call community)\n
    📌 Dont promote any paid resource, campus ambassador stuff and irrelevant material\n
    📌 Be respectful to each other and humble
    """)


def schedule_command(update, context):
    
    update.message.reply_text("""Schedule For DSA bootcamp🌟🌟🌟: \n 
1.) 1 June   Introduction To boot camp, space and time complexity \n

2.) 3 June Strings and Array \n
3.) 5 June Bit manipulation, Mathematics \n
4.) 7 June Recursion and greedy \n
5.) 9 June Searching and sorting \n
6.) 11 June Linked List, Stack, Queue Deque \n
7.) 13 June Trees\n
-📌📌 Codeflow Ninjas (coding contest) on 14 June\n
8.) 15 June Hashing \n
---    Internship Preparation Webinar on 16 June\n
9.) 17 June Graph \n
10.) 19 June Graph \n
---    Interview Prep Webinar on 20 June\n
11.) 21 June Disjoint Set \n
12.) 23 June Heap and priority queues \n
13.) 25 June Backtracking \n
14.) 27 June Dynamic programming \n
15.) 29 June Dynamic programming  \n   

📌📌 Codeflow Endgame on 30 June,2021 \n 

     """)

def codeflow(update, context):
    
    update.message.reply_text("""
        Codeflow 😊 is a students driven organization running for students empowerment 🤗\n
        We are currently working in three domains: \n
        🌟 Open-Source ( https://github.com/codeflow201 )\n
        🌟 Worksops and webinars from industry experts ( https://www.youtube.com/c/codefloworg ) \n
        🌟 Community building ( https://www.linkedin.com/company/codefloworg ) \n
        \n 
        We belive in strengthening the skills of each other while learning in community🤗.

     """)
def Welcome(update, context):
    
    update.message.reply_text("""
        Thanks for calling bot🤗: let me know How can I help you \n
        
        Here is what can I do and How?\n
        /codeflow    to know about codeflow\n
        /dsaform     to get regestration form DSA bootcamp\n
        /schedule    to know about schedule\n
        /group       to know about codeflow telegram instructions\n
        /update      to know about updates\n
        /handles     to get the link of all codeflow handles\n
        /motivation  to be happy withh codeflow family
     """)

def handles(update, context):
    
    update.message.reply_text("""
        
    🌟Youtube  : https://www.youtube.com/c/codefloworg \n
    🌟Linkedin : https://www.linkedin.com/company/codefloworg \n
    🌟Telegram : https://t.me/joinchat/FdJhyMumJK5sryCv \n
    🌟GitHub   : https://github.com/codeflow201 \n
    🌟Instagram: https://www.instagram.com/codefloworg \n
    🌟Twitter  : https://twitter.com/codefloworg \n
    \n
    🤗You can find all the links of codeflow here🤗: \n
        https://linktr.ee/codefloworg \n

     """)

def motivation(update, context):
    update.message.reply_text(""" 🤸🏻‍♂️ अपना हर दिन ऐसे जियो, जैसे की आखरी हो \n
जियो तोह इस पल ऐसे जियो, जैसे की आखरी हो \n
अपना हर दिन ऐसे जियो, जैसे की आखरी हो \n
जियो तोह इस पल ऐसे जियो, जैसे की आखरी हो 🤸🏻‍♂️""")

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
    dp.add_handler(CommandHandler("schedule", schedule_command))
    dp.add_handler(CommandHandler("group", group_command))
    dp.add_handler(CommandHandler("dsaform", start_command))
    dp.add_handler(CommandHandler("motivation", motivation))
    dp.add_handler(CommandHandler("handles", handles))

    updater.start_polling()
    updater.idle()

main()