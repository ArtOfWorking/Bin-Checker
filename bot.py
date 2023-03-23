import openai
import os
import requests
from telethon import TelegramClient, events

# Set up OpenAI API key and model

CHATGPT_TOKEN = os.environ.get("CHATGPT_TOKEN", None)
openai.api_key = CHATGPT_TOKEN

# Set up Telegram bot and API key
api_id = 11891876
api_hash = 'b48fe8105495265d1095038f8b5778cf'
bot_token = '6157888032:AAHWuiSqpGLFknEaYohj9T-Jpnj0Iv_O1Rs'
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Handle incoming messages
@client.on(events.NewMessage(pattern='/generate'))
async def handle_generate(event):
    # Get the input from the user and split it into separate lines.
    me = (await event.client.get_me()).username
    prompt = event.text.split(" ", maxsplit=1)[1]
    print ("enter")
    # Get user's prompt from message text
    prompt = event.message.text.replace('/generate', '').strip()
    try:
        # Generate image using OpenAI's DALL-E API
        response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
        )
    

    # Get image URL from OpenAI response
        image_url = response['data'][0]['url']
        print (image_url)
        

        # Download image from URL
        image_data = requests.get(image_url).content
        await client.send_file(event.chat_id, image_data)
    except Exception as e:
        # Handle the error here
        print(f"Error: {e}")
        await event.reply(e)
        #    print (image_data)
        # Send image to user
        

# Start bot
client.run_until_disconnected()
