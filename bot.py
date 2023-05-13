import requests
from cfscrape import create_scraper
import json

import subprocess
import time
import re
import os
from telethon import TelegramClient, events, sync
from telethon import Button
import logging

logging.basicConfig(level=logging.INFO)

# replace the values with your own API ID, API Hash, and bot token
api_id = 11891876
api_hash = 'b48fe8105495265d1095038f8b5778cf'
bot_token = '6295817509:AAGM3PsswyvTDGyQ5RE757mlTdmHLnBxXBY'
#admin_ids_str = os.environ.get("CHANNEL_IDS", None) 
#admin_ids = [int(id) for id in channel_ids_str.split(",")]
admin_ids = [1927696336]
channel_id = --1001789071935


########cookies#########
cookies = {
    'browserid': 'KHMv2XNnaae0wXLdzF78LHDgYl4R7FmxJtzoPDBf3V6iUciGhPcvkpLcTw0=',
    'lang': 'en',
    'TSID': '3aFX8GZ9HTPktFiGuG19Bh1exS4ufVyM',
    '__bid_n': '187d1b7844eeb0bb034207',
    '_ga': 'GA1.1.17000904.1682850689',
    'ndus': 'YSLmcKCteHuiK7X0KVRPaICUh0V7Pg-f6xsRbgXo',
    'ndut_fmt': 'F81D6FBB029A30852D0C78BF8FE3536F570B56A4DC0044FF7EFECBF9FDD51B89',
    '_ga_RSNVN63CM3': 'GS1.1.1682856747.2.1.1682856779.28.0.0'
}
#########################









client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.CallbackQuery())
async def callback_handler(event):
    try:
        if event.data == b'redirect':
            about = "Hello Bro" 
            button2 = Button.inline("exit", data="exit")
            await xx.edit(about, buttons = button2, parse_mode='HTML')
        elif event.data == b'exit':
            print ("exit")
            # delete the xx message
            await xx.delete()

    except Exception as e:
        print(f"Error - {str(e)}")


def terabox(url) -> str:
    session = create_scraper()
    try:
        try:
            res = session.request('GET', url)
        except Exception as e:
            return (f"ERROR: {e}")
        key = res.url.split('?surl=')[-1]
        print (key)
        if cookies is None: return f"Terabox Cookie is not Set"
        url2 = f'https://www.4funbox.com/share/list?app_id=250528&shorturl={key}&root=1'
        res = requests.get(url2, cookies=cookies)
        print (res.text)
        return json.loads(res.text)
    except Exception as e:
        return (f"ERROR: {e}")







@client.on(events.NewMessage(pattern="^[!?/]start"))
async def handle_new_message(event):
    print (event.sender_id)
    if event.sender_id not in admin_ids:
        return
    global xx
    message = "Hello I Can Download Terabox files"
    button1 = Button.inline("About", data="redirect")
    xx = await event.respond(message, buttons = button1, link_preview=False, parse_mode='HTML')





    






@client.on(events.NewMessage(pattern="^[!?/]down"))
async def handle_new_message(event):
    main = event.message
    if event.sender_id not in admin_ids:
        return
    global yy
    yy = await event.reply("<b>processing</b>", parse_mode='HTML')
    async def progress_bar(current, total):
        if timer.can_send():
            await msg.edit("{} {}%".format(type_of, current * 100 / total))
    url = event.text.split(" ", maxsplit=1)[1]
    #url = event.message.message
    print (url)
    bypass = terabox(url)
    print (bypass)
    print (type(bypass))
    if isinstance(bypass, str):
        print ('error')
        return
    elif int(bypass['errno']) != 0:
        print (bypass['errno'])
        print (type(bypass['errno']))
        return
    print (bypass)
    try:
        print ("try")
        down = bypass['list'][0]['dlink']
        print (down)
        # Extract the server_filename value
        title = bypass['list'][0]['server_filename']

    except Exception as e:
        print ("real error")
        print (e)
        title = bypass['list'][0]['server_filename']
    print (down)
    print (f'title --- { title}')
    # Extract the filename from the URL
    start_time1 = time.time()
    subprocess.run(['aria2c', '--console-log-level=warn', '-x 32', '-s 32', '-j 16', '-k 2M', '--file-allocation=none', '-o', title, down])

    end_time1 = time.time()
    time_taken = round(end_time1 - start_time1)
    if time_taken < 60:
        print("Time taken:", time_taken, "seconds")
        download_time = "Time taken:", time_taken, "seconds"
    else:
        minutes = time_taken // 60
        seconds = time_taken % 60
        download_time = "Time taken:", minutes, "min", seconds, "sec"
    
    msg = f"""
<i>{title}</i>
<b>Uploaded By - @RF_TeraBot </b>
<code>{download_time}</code>
    """
    file = await event.client.send_file(
        event.chat_id,
        title,
        caption=msg, parse_mode='HTML',)
    await yy.delete()
    await client.forward_messages(channel_id, file)
 
    
    
    
    
    
    
    
    
    
################USER-BANNING-CODE########
    
    
    
    
client.run_until_disconnected()