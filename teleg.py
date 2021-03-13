from telegram import *
from telegram.ext import *
import os

#If you going to use this bot on cloud (Google cloud etc.)I used OS library for safety to get all keys/tokens from local environment variables.
#If you don't want to do that and you'll run this code on your local, you can define all thoose variables as a string.
token1 = os.getenv("token1")
bot=Bot(token1)
#print(bot.get_me())
updater=Updater(token1,use_context=True)
disp=updater.dispatcher

def get_id(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Elon Musk her tweet attığında bildirim alacaksınız. Bu işlemi iptal etmek için /dur yazınız."
    )

    with open("ids.txt","r+") as ids:
        if str(update.effective_chat.id) not in [i.strip("\n") for i in ids.readlines()]:
            ids.write(f"{update.effective_chat.id}\n")


def del_id(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Size haber uçurmak güzeldi..."
    )
    removed=update.effective_chat.id

    with open("ids.txt","r") as ids:
        all_id=[i.strip("\n") for i in ids.readlines()]
    
    with open("ids.txt","w") as ids:
        for i in all_id:
            if i !=str(removed):
                ids.write(f"{i}\n")
        

def sontw(update:Update,context:CallbackContext):
    with open("ftweet.txt","r") as ft:
        tweet_link=ft.readlines()[0]
    
    bot.send_message(chat_id=update.effective_chat.id,text=f"Elon Musk'ın son tweeti\n|\n|\n -->{tweet_link}")


def message(s):
    with open("ids.txt","r") as ids:
        for ch_id in [i.strip("\n") for i in ids.readlines()]:
            bot.send_message(chat_id=ch_id,text="Elon Musk yeni bir tweet attı !\n\nTweet :"+s)


start_value = CommandHandler("basla",get_id)
start_value2=CommandHandler("start",get_id)
sntw=CommandHandler("sontw",sontw)
end_value=CommandHandler("dur",del_id)

disp.add_handler(start_value)
disp.add_handler(start_value2)
disp.add_handler(end_value)
disp.add_handler((sntw))
updater.start_polling()
