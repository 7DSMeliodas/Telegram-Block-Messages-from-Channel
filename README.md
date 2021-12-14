# Telegram-Block-Messages-from-Channel
This scripts blocks messages sent from channels in your group(s)


Install:


apt install pyrogram

apt install tgcrypto

Edit API_ID and API_Hash to yours you get from https://my.telegram.org

Edit LOG_GROUP to your loggroups id (or disable it and keep the stock value)

Edit GROUPS_TO_PROTECT to the the group you want to protect (bot will delete messages sent from channel)

If you want to log keep LOG to true, if you dont need any logging set LOG = false (set LOG_GROUP if you want to log)

Add the bot in every group you want to protect with the admin privilegs "can_delete_messages"

python3 bot.py

# This file/readme could be more userfriendly
Yes, of course! Feel free to pull request

i just set this up for a problem just occured in our groups.

this bot should work on windoof, linux and macOS

i'm lazy so feel free to pr more userfriendly readme/code

and yes, i could've set up an .env, but i made it single file only 

cuz im lazy

at least it should do what we want, so dont blame me

and "we wish you a marry xmas"
