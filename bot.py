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
    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
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


openai.api_key = CHATGPT_TOKEN

def generate_text(prompt):
    model_engine = "text-davinci-003"
    prompt = prompt

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=1.0,
    )

    response = completion.choices[0].text
    return response

bot = TelegramClient('bin', API_ID, API_HASH)
bin = bot.start(bot_token=TOKEN)
@bin.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):
    await event.reply(f"**Heya {event.sender.first_name}**\nIts CHAT GPT LIVE ", buttons=[
    [Button.url("Mʏ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", "https://art_of_working.t.me")]
    ])


@bot.on(events.NewMessage)
async def binc(event):
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

        response = requests.post(url, data=params)
        print (response.text)
        print (response)
        print ("lol")
    except Exception as e:
        print (e)
    

logging.info("Bot started successfully")
bin.run_until_disconnected()