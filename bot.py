import requests
import time

import os
from telethon import TelegramClient, events
import PyBypass as bypasser
from telethon import Button, events, TelegramClient
from telethon import events, custom, Button
import logging

logging.basicConfig(level=logging.INFO)
# replace the values with your own API ID, API Hash, and bot token
api_id = 11891876
api_hash = 'b48fe8105495265d1095038f8b5778cf'
bot_token = '6216317473:AAFEIvVyn3Cr45h5D7S4qNbfXPXyaqpzIQ4'

channel_ids = [-1001371265936, -1001963763050]
msg = """
<b>We kindly request you to join our channels first.<b/>
"""

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# define bypass variable globally
bypass = ""
buttons = [
    [
        Button.url("𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑪𝒉𝒂𝒏𝒏𝒆𝒍", url ="https://t.me/Raj_Files" )
    ],
    [
        Button.url("𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑺𝒆𝒄𝒐𝒏𝒅 𝑪𝒉𝒂𝒏𝒏𝒆𝒍", url = "https://t.me/BotsHubs")
    ]
]


@client.on(events.NewMessage(pattern="^[!?/]start$"))
async def start_handler(event):
    # Get the user's name
    user = await client.get_entity(event.sender_id)
    name = user.first_name
    username = event.sender.username
    message = f"""
<b>Hello {name}</b> 👋

<i>I am Link Bypasser Bot. I can Bypass Link For You and Get Original Link.</i>

<b>Simply Send Me a Valid Link and Get Original Link.</b>

    """
    button = Button.inline("About", data="redirect")


    await event.respond(message, buttons = buttons, link_preview=False, parse_mode='HTML')


about = f"""
<b>Mʏ Nᴀᴍᴇ: </b> <a href="https://t.me/LinkBypasserBotHub_Bot">Lɪɴᴋ Bʏᴘᴀssᴇʀ</a>

<b>Vᴇʀsɪᴏɴ: 0.0.0-Lɪɴᴋ_Bʏᴘᴀssᴇʀ_Bᴏᴛ_Tɢ</v>

<b>Lᴀɴɢᴜᴀɢᴇ: </b> <a href="https://www.python.org/">Pʏᴛʜᴏɴ 3.11.1</a>

<b>Dᴇᴠᴇʟᴏᴘᴇʀ: </b><a href="https://t.me/ART_OF_WORKING">Unknown</a>

<b>Pᴏᴡᴇʀᴇᴅ Bʏ: </b> <a href="https://t.me/BotsHubs">Bots Hub</a>
    """


@client.on(events.CallbackQuery())
async def callback_handler(event):
    try:
        # Check if the callback data is equal to a specific value
        if event.data == b'redirect':
            await event.respond(about, link_preview=False, parse_mode='HTML')
            # Define the URL to redirect to
            # Respond to the callback query with an answer and redirect to the URL
#            await event.answer("hello", cache_time=0, alert=False)
    except Exception as e:
        print(f"Error - {str(e)}")

@client.on(events.NewMessage(pattern="^[!?/]about$"))
async def start_handler(event):
    await event.respond(about, link_preview=False, parse_mode='HTML')

# define an event handler for incoming messages
@client.on(events.NewMessage(pattern='(?i)https?://\S+'))
async def handle_new_message(event):
    if 'mdisk.me' in event.text:
        return
    global bypass
    url = event.text.strip()
    user = await event.get_sender()
    sender_id = user.id

    # check if user has joined all the channels
    num_channels_joined = 0
    for channel_id in channel_ids:
        async for user1 in client.iter_participants(channel_id):
            if user1.id == sender_id:
                print(f"User has joined channel {channel_id}")
                num_channels_joined += 1
                break
    if num_channels_joined != len(channel_ids):
        message = f"{user.first_name}, you need to join all the channels to use the bot."
        await event.respond(message, buttons = buttons, link_preview=False, parse_mode='HTML')
        return
            # handle the case where the user has not joined all channels here
    global bypass
    sender_id = event.sender_id
    sender_username = event.sender.username

    try:
        start_time = time.time()
        # get the URL from the message
        url = event.pattern_match.string
        bypass = bypasser.bypass(url)
        print (bypass)
        end_time = time.time()
        # send a reply back to the user with the URL
        elapsed_time = end_time - start_time
        bypass_message = f"""
<b>Ads Link:</b> <code>{url}</code>

<b>Original Link:</b> <code>{bypass}</code>

<b>Time Elapsed:</b> <i>{elapsed_time:.2f} seconds</i>

<b>Generated With </b> <a href="https://t.me/Raj_Files/">Link Bypasser 🤖</a>
        """
        button = Button.url("Open Original Link", url = bypass)
        await event.reply(bypass_message, buttons=button, link_preview=False, parse_mode='HTML')
        bypass_message = f"""
<b>Username:</b> @{sender_username}

<b>Telegram ID:</b> <code>{sender_id}</code>

<b>Ads Link:</b> <code>{url}</code>

<b>Original Link:</b> <code>{bypass}</code>

<b>Time Elapsed:</b> <i>{elapsed_time:.2f} seconds</i>

<b>Generated With </b> <a href="https://t.me/ART_OF_WORKING/">Link Bypasser 🤖</a>
        """
        await client.send_message(1927696336, bypass_message, buttons=button, link_preview=False, parse_mode='HTML')
    except Exception as e:
        print(f"Error: {str(e)}")
        bypass_message = f"""
<b>Username:</b> @{sender_username}

<b>Telegram ID:</b> <code>{sender_id}</code>

<b>Ads Link:</b> <code>{url}</code>

<b>Error:</b> <code>{e}</code>

<b>Generated With </b> <a href="https://t.me/ART_OF_WORKING/">Link Bypasser 🤖</a>
    """
        msg1 = """
<b>Sorry, I Can't Bypass This Link.</b>
<b>plz try other.</b>
        """
        await event.reply("<b>Sorry, I Can't Bypass This Link.</b>", parse_mode='HTML')
        await client.send_message(1927696336, bypass_message, link_preview=False, parse_mode='HTML')







#############{{{{{{{MDISK}}}}}}}##########


@client.on(events.NewMessage(pattern=r'https://mdisk\.me/\S+'))
async def handle_new_message(event):
    id = event.text.split("/")[-1]
    print(id)
    url = f"https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={id}"
    print(url)
    res = requests.get(url)
    print(res.text)
    if 'The content is deleted' in res.text:
        await event.reply(f'<b>{res.text}</b>', link_preview=False, parse_mode='HTML')
        return
    
    try:
        response = res.json()
        print (response)
        title = response["filename"]
        download_url_dash = response["source"]
        download_url_mxv = response["download"]
        uploader_user_id = response["from"]
        uploader_user_name = response["display_name"]
        video_width = response["width"]
        video_height = response["height"]
        video_duration = response["duration"]
        video_size = response["size"]# convert from bytes to MB
        # do something with the extracted data
        print(title, download_url_dash, download_url_mxv, uploader_user_id, uploader_user_name, video_width, video_height, video_duration, video_size)
        
        
        
        msg5 = f"""
<b>📂 Title : </b> <code>{title}</code>

<b>📥 Download URL (If mxv Present in link then it support only MX player </b>


<b>If dash, mpd, M3U8, hls present in link then it support all player) :-</b> {download_url_dash}

<b>📤 Download URL (Support Only MX Player) :- </b> {download_url_mxv}

<b>💎 Uploader User ID :-  </b> <code>{uploader_user_id}</code>

<b>💠 Uploader User Name :-  </b> <code>@{uploader_user_name}</code>


<b>📹 Video Width :-  </b> <code>{video_width}</code>

<b>🎞 Video Height :- </b> <code>{video_height}</code>

<b>📦 Video Duration :-  </b> <code>{video_duration}s</code>

<b>📊 Video Size :-  </b> <code>{video_size}kb</code>
        
        
        
    """
        
        
        await event.reply(msg5, parse_mode='HTML')
    except Exception as e:
        print(f"Error: {str(e)}")





#non Stop
client.run_until_disconnected()
