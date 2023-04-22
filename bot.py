import logging
import os
import html
import telegram
import re
import random
import requests
import openai
from telethon import events, Button, TelegramClient

logging.basicConfig(level=logging.INFO)

try:

    API_ID = 24409305
    API_HASH = "e32ed02d2daeabea2d433464a8c2a53d"
    TOKEN = "6188938989:AAHwD-PD60Tgs450qR2_eqDzmvA-Z-4T_kQ"
    CHATGPT_TOKEN = os.environ.get("CHATGPT_TOKEN", None)

    print (API_ID)
    print (API_HASH)
    print (TOKEN)
    print (CHATGPT_TOKEN)
except ValueError:
    print("You forgot to fullfill vars")
    print("Bot is quitting....")
    exit()
except Exception as e:
    print(f"Error - {str(e)}")
    print("Bot is quitting.....")
    exit()
except ApiIdInvalidError:
    print("Your API_ID or API_HASH is Invalid.")
    print("Bot is quitting.")
    exit()



buttons = [
[
Button.url("𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑪𝒉𝒂𝒏𝒏𝒆𝒍", url="https://t.me/Raj_Files"),
],
[
Button.url("𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑺𝒆𝒄𝒐𝒏𝒅 𝑪𝒉𝒂𝒏𝒏𝒆𝒍", url="https://t.me/BotsHubs"),
],
]
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

bot = TelegramClient('bin', API_ID, API_HASH)
bin = bot.start(bot_token=TOKEN)



@bin.on(events.NewMessage(pattern="^[!?/]help$"))
async def start(event):

    msg = """
/chat For Group Chat

Normal Message For Inbox Chat
    """
    await event.reply(msg)







@bin.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):
    await event.reply(f"**Heya {event.sender.first_name}**\n\nWelcome To Chat Bot.", buttons=buttons)


@bot.on(events.NewMessage)
async def binc(event):
    if event.is_group:
        if '/chat' not in event.message.message:
            return
    sender_id = event.sender_id
    sender_username = event.sender.username
    # Get the client details from the event object
    # Get the sender information
    sender = await event.get_sender()
    if sender.username:
        name = f"@{sender.username}"
    else:
        name = f"{sender.first_name} {sender.last_name}"

    client = event.client
    sender = await event.get_sender()
    chat_id = event.chat_id
    message_text = event.message.message



    # Send the client details as a message to the bot
#    message = f"Client details:\nSender: {sender}\nChat ID: {chat_id}\n{name}\nMessage: {message_text}"
    msg = event.message.message
    if msg == "/start":
        return

    xx = await event.reply("`Processing.....`")
    logging.info(f"Received message: {msg}")
    try:
        prompt = msg
        global generated_text
        generated_text = generate_text(prompt)
        # print the generated text
        logging.info(f"Generated text: {generated_text}")
        message = f"""
<b>Username:</b> @{sender_username}

<b>Telegram ID:</b> <code>{sender_id}</code>

<b>USER SEND:</b> <code>{msg}</code>

<b>Bot Response:</b> <code>{generated_text}</code>

<b>Generated With </b> <a href="https://t.me/ART_OF_WORKING/">Unknown Chatgpt🤖</a>
    """
        print (message)
        await xx.edit(generated_text, parse_mode="HTML")
    except Exception as e:
        print (e)
        generated_text = (f"Error:- {e}")
        logging.error(f"Error generating text: {str(e)}")
        await xx.edit("Error generating text.")
        message = (f"""
<b>Username:</b> @{sender_username}

<b>Telegram ID:</b> <code>{sender_id}</code>

<b>USER SEND:</b> <code>{msg}</code>

<b>Bot Response:</b> <code>{generated_text}</code>

<b>Generated With </b> <a href="https://t.me/ART_OF_WORKING/">Link Bypasser 🤖</a>
""")
    print (message)
    bot_token = "5699025475:AAG3_S0qJMFWz_d1QxQClk-w1RvCa9pi28E"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Set the parameters for the request (the message and chat ID)
    print ("hello")
    try:
        params = {
        "chat_id": chat_id,
        "text": message,
        "disable_web_page_preview": True,
        "parse_mode": 'HTML'
        
        }

    # Send the request to the Telegram API

    except Exception as e:
        print (e)
    

logging.info("Bot started successfully")
bin.run_until_disconnected()
