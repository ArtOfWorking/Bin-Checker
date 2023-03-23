from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio
import openai
import os
import re
import logging
# create a session using the session string
CHATGPT_TOKEN = os.environ.get("CHATGPT_TOKEN", None)
session_string = '1BVtsOK0Bu37XtS4ZFzneR0-HvMJKofMkYJkYRY-UpQJ7vIEa06l1lfC--KFEuixaEZ9i8S-sg5N5HoI8BNXczS86bD_9cQLruKRR2PnEkOVTW8GCcFQKbXA8h1A_EKPi5eq8eNGihO6chY_5DWeA-H0ydrg7s_N2g6V_DXb_x2gOyjyIb43hPlhq6JzabHEqmDQSGnDlNfn4irTpAE39ccWLR52qKNsRd4gFIVTfLua3rYdxF8h0Ttfv1BvxbEZ8Gj3VgqRNC6LHQOxRNWl-FRl51tkzyD4Qw1RRYOHI6R4aJIGb2CZLoong8Q8ce2acr-I7Ejrlw3sAgkfs5MXPdgXL0UiLlTo='
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

@client.on(events.NewMessage(pattern="^[!?/]q"))
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
        await event.reply(generated_text, parse_mode="HTML")
    except Exception as e:
        logging.error(f"Error generating text: {str(e)}")
        await event.reply(f"Error generating text: {str(e)}")
# start the client
async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':

    asyncio.run(main())
