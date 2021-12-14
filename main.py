from pyrogram import Client, filters

app = Client("BlockMsgFromChannel", "API_ID", "API_Hash")

LOG_GROUP = -9876
GROUPS_TO_PROTECT = [-1234, -4321]
LOG = true

@app.on_message(filters.chat(GROUPS_TO_PROTECT))
def check_for_user(Client, msg):
    if msg.sender_chat:
        msg.delete()
        if log:
          app.send_message(LOG_GROUP, "I deleted the following message:")
          app.send_message(LOG_GROUP, msg)
         else:
          pass
    else:
        pass

app.run()
