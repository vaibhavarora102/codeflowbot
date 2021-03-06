import constant as keys
# from python-telgram-bot import *
import responses as R
from telegram.ext import Updater, CommandHandler, CallbackContext

def start_command(update, context):
    
    update.message.reply_text(""" https://forms.gle/BHbAqkCnAViVkeF76 \n

So, Finally wait is over πCodeflow is going to organize 4 weeks of DSA Bootcamp for the students π©βπ to bridge  the gap between knowledge and practical implemenation π caused due to pandemic   by providing mentorship π₯³π₯³ from experts to students willing to learn and grow with the community. 

π―π\n \n
Join telegram to be part of it: https://lnkd.in/dkBEsNS \n


Stay tuned for more updates !\n
Perks:  \n
1. Mentorship for 4 weeks \n
2. DSA contest at end of the program \n
3. Goodies to top 5 in coding competition  \n
4. More (based on collaborations) π \n """)

def anyupdate_command(update, context):
    update.message.reply_text("""
    π Schedule is updated, Do check it out by using /schedule \n
    π Cash prizes and more goodies are introduced during Bootcamp\n
    π Whole Bootcamp will be in the form of Live lectures of Codeflow youtube channel 
    ( https://www.youtube.com/c/codefloworg )\n
    π Live lectures will have the duration of 2 hours (approx) each\n
    π Most of the lectures are Scheduled from 7 p.m to 9 p.m (it may vary acc. to mentor)\n  
    """)

def group_command(update, context):
    update.message.reply_text("""
    π To make your experience even more better, we welcome your suggestion (in nicely presented way)\n
    π Don't ask same questions again and again\n
    π Be helpful in group (try to help each other, as this is what we call community)\n
    π Dont promote any paid resource, campus ambassador stuff and irrelevant material\n
    π Be respectful to each other and humble
    """)


def schedule_command(update, context):
    
    update.message.reply_text("""Schedule For DSA bootcampπππ: \n 
1.) 1 June   Introduction To boot camp, space and time complexity \n

2.) 3 June Strings and Array \n
3.) 5 June Bit manipulation, Mathematics \n
4.) 7 June Recursion and greedy \n
5.) 9 June Searching and sorting \n
6.) 11 June Linked List, Stack, Queue Deque \n
7.) 13 June Trees\n
-ππ Codeflow Ninjas (coding contest) on 14 June\n
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

ππ Codeflow Endgame on 30 June,2021 \n 

     """)

def codeflow(update, context):
    
    update.message.reply_text("""
        Codeflow π is a students driven organization running for students empowerment π€\n
        We are currently working in three domains: \n
        π Open-Source ( https://github.com/codeflow201 )\n
        π Worksops and webinars from industry experts ( https://www.youtube.com/c/codefloworg ) \n
        π Community building ( https://www.linkedin.com/company/codefloworg ) \n
        \n 
        We belive in strengthening the skills of each other while learning in communityπ€.

     """)
def Welcome(update, context):
    
    update.message.reply_text("""
        Thanks for calling botπ€: let me know How can I help you \n
        
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
        
    πYoutube  : https://www.youtube.com/c/codefloworg \n
    πLinkedin : https://www.linkedin.com/company/codefloworg \n
    πTelegram : https://t.me/joinchat/FdJhyMumJK5sryCv \n
    πGitHub   : https://github.com/codeflow201 \n
    πInstagram: https://www.instagram.com/codefloworg \n
    πTwitter  : https://twitter.com/codefloworg \n
    \n
    π€You can find all the links of codeflow hereπ€: \n
        https://linktr.ee/codefloworg \n

     """)

def motivation(update, context):
    update.message.reply_text(""" π€Έπ»ββοΈ ΰ€ΰ€ͺΰ€¨ΰ€Ύ ΰ€Ήΰ€° ΰ€¦ΰ€Ώΰ€¨ ΰ€ΰ€Έΰ₯ ΰ€ΰ€Ώΰ€―ΰ₯, ΰ€ΰ₯ΰ€Έΰ₯ ΰ€ΰ₯ ΰ€ΰ€ΰ€°ΰ₯ ΰ€Ήΰ₯ \n
ΰ€ΰ€Ώΰ€―ΰ₯ ΰ€€ΰ₯ΰ€Ή ΰ€ΰ€Έ ΰ€ͺΰ€² ΰ€ΰ€Έΰ₯ ΰ€ΰ€Ώΰ€―ΰ₯, ΰ€ΰ₯ΰ€Έΰ₯ ΰ€ΰ₯ ΰ€ΰ€ΰ€°ΰ₯ ΰ€Ήΰ₯ \n
ΰ€ΰ€ͺΰ€¨ΰ€Ύ ΰ€Ήΰ€° ΰ€¦ΰ€Ώΰ€¨ ΰ€ΰ€Έΰ₯ ΰ€ΰ€Ώΰ€―ΰ₯, ΰ€ΰ₯ΰ€Έΰ₯ ΰ€ΰ₯ ΰ€ΰ€ΰ€°ΰ₯ ΰ€Ήΰ₯ \n
ΰ€ΰ€Ώΰ€―ΰ₯ ΰ€€ΰ₯ΰ€Ή ΰ€ΰ€Έ ΰ€ͺΰ€² ΰ€ΰ€Έΰ₯ ΰ€ΰ€Ώΰ€―ΰ₯, ΰ€ΰ₯ΰ€Έΰ₯ ΰ€ΰ₯ ΰ€ΰ€ΰ€°ΰ₯ ΰ€Ήΰ₯ π€Έπ»ββοΈ""")

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