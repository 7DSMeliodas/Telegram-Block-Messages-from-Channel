from pyrogram import Client, filters

app = Client("my_session", "API_ID", "API_Hash")

LOG_GROUP = -9876
GROUPS_TO_PROTECT = [-1234, -4321]
LOG = "nice"


@app.on_message(filters.chat(GROUPS_TO_PROTECT)
def check_for_user(Client, msg):
    if msg.sender_chat:
        msg.delete()
        if LOG == "max":
            app.send_message(LOG_GROUP, "I deleted the following message:")
            app.send_message(LOG_GROUP, msg)
        elif LOG == "nice":
            if len(msg.text) < 4062:
                app.send_message(LOG_GROUP, "I deleted the following message:\n{}".format(msg.text))
            else:
                app.send_message(LOG_GROUP, "I deleted the following message:")
                app.send_message(LOG_GROUP, msg.text)
            app.send_message(LOG_GROUP,
                             "The message was from this channel:\nChannelname: {}\nChannellink: @{}\n".format(
                                 msg.sender_chat.title, msg.sender_chat.username))
            app.send_message(LOG_GROUP, "The message was in this group:\n{}".format(msg.chat.title))
        else:
            pass

    else:
        pass

app.run()
