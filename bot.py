from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import openai
import os
import time
import re
import logging
# create a session using the session string
CHATGPT_TOKEN = os.environ.get("CHATGPT_TOKEN", None)
session_string = '1BVtsOK0Bu14yWl_aGjrmF6V0IV4iCdMBJWp_8HADH3EzEFk1jLtYVW8KHeJgiMpcohjyf2hcyu6IYODtcsjlJgmiPTQz96ROMAOFkhEe_RNBoVGMh4YcXV_3yOl_QC6EVuSDiRlOLFk71dIlc092Udbv7Cen3YSAajcUj95w1TNhK_p3Apgr-8ZaBhmZKatETugmoSJ74alLXXIceRNrMJWVjh2d3loSDSbUmP8McIr2wQcJ1c53nChn4ut2F17pXqeeKzQS4Xqy295SV1VR3CbLfxQ_w8iA8oxWuPEulfqPogSjL1sCeqdSrLMqy-LFL3Np0QAtq-6Z_3FPr-TMsKRwPjOaHvs='
session = StringSession(session_string)
# configure Telethon
api_id = 11891876
api_hash = 'b48fe8105495265d1095038f8b5778cf'
client = TelegramClient(session, api_id, api_hash)
logging.basicConfig(level=logging.INFO)

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
# Loop to keep the client online
while True:
    try:
        # Send a message to yourself every minute to keep the client active
        client.send_message('me', 'I am online!')

        # Wait for 30 seconds
        time.sleep(30)

    except KeyboardInterrupt:
        # Exit the loop on keyboard interrupt (Ctrl + C)
        break
@client.on(events.NewMessage(pattern="^[!?!]q"))
async def binc(event):
    try:
        print ("Enter")
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
        message = await event.reply(f"Error generating text: {str(e)}")
        await asyncio.sleep(180)
        await client.delete_messages(event.chat_id, message)
# start the client
async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':

    asyncio.run(main())
