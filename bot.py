from pyrogram import Client, filters
import asyncio
import config
from html import escape
from urllib.parse import urlparse
import direct_link
import download
from pyrogram.errors import UserNotParticipant, PeerIdInvalid
from pyrogram.errors.exceptions import UsernameInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import base64
from cfscrape import create_scraper
import time
import requests
import sys
import math
import os
import subprocess
import json
import logging
logging.basicConfig(level=logging.INFO)

user_ids = []
owner_list = [1927696336, 5489376698]


url_filter = filters.create(lambda _, __, message: any(urlparse(word).scheme for word in message.text.split()))

keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Button 1", callback_data="button1")],
         [InlineKeyboardButton("Button 2", url="https://t.me/RajFiles")]]
    )


if not os.path.exists('users.txt'):
    with open('users.txt', 'w') as file:
        pass
if not os.path.exists('admin.txt'):
    with open('admin.txt', 'w') as file:
        pass




app = Client('@ART_OF_WORKING', config.api_id, config.api_hash, bot_token=config.bot_token)


# Handle the /start command
@app.on_message(filters.command('start'))
def start_command(client, message):
    with open('users.txt', 'r') as file:
        # Read the contents of the file
        contents = file.read()
        # Split the contents by commas and create the users list
        users = contents.split(",")
        if str(message.from_user.id) not in users:
            with open('users.txt', 'a') as file:
                file.write(f"{message.from_user.id}, ")
        start = f"""
<b>ＨＥＹ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<i>THIS IS TERABOX DOWNLOADER POWERED BY:- Raj Files</i>

ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- Raj Files

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- <a href="tg://user?id=1927696336">𝘜𝘯𝘬𝘯𝘰𝘸𝘯𝘜𝘴𝘦𝘳</a>

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
</b>
"""

    
        
        # Forward the photo with the caption to the private group
        xx = client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=config.chat_id,
            message_id=config.message_id,
            caption=start,
            
        )        
        #reply_markup=keyboard
        if message.chat.type == 'group' or message.chat.type == 'supergroup':
            time.sleep(60)
            client.delete_messages(
                chat_id=xx.chat.id,
                message_ids=xx.message_id,
                # 60 seconds delay
            )
    



@app.on_message(url_filter)

def terabox_link_handler(client, message):
    user_id = message.from_user.id
    with open('admin.txt', 'r+') as file:
        
        lines = [int(line.strip()) for line in file.readlines()]
        file.seek(0)
        combined_list = lines + owner_list
        
        if user_id not in combined_list:
            message.reply_text("I can't do Anything")
            return
    with open('users.txt', 'r') as file:
        # Read the contents of the file
        contents = file.read()
        # Split the contents by commas and create the users list
        users = contents.split(",")
        
        if str(message.from_user.id) not in users:
            with open('users.txt', 'a') as file:
                file.write(f"{message.from_user.id}, ")
               
        
    proc = client.send_message(
        chat_id=message.chat.id,
        text='processing'
    )
    try:
        user = message.from_user.username
    except Exception as e:
        print("Error retrieving user:", str(e))
        user = user_id
    user_id = message.from_user.id
    url = next(urlparse(word) for word in message.text.split() if urlparse(word).scheme).geturl()
    # Reply with a terabox link message
    if any(x in url for x in ['terabox', 'nephobox', '4funbox', 'mirrobox', 'momerybox', 'teraboxapp']):
        bypass = direct_link.terabox(url)
    else:
        bypass = url
    print (bypass)
    if bypass == "error":
        proc.edit("Problem In Url :(")
        return
    start_time1 = time.time()
    proc.edit("Downloading....")
    print ("Downing.....")
    #title = download.down(bypass, client, proc)
    title = download.down(bypass)
    end_time1 = time.time()
    time_taken = round(end_time1 - start_time1)
    if time_taken < 60:
        download_time = "Time taken:", time_taken, "seconds"
    else:
        minutes = time_taken // 60
        seconds = time_taken % 60
        download_time = "Time taken:", minutes, "min", seconds, "sec"
    db_caption = f"""
<b>UserName:</b> <a href="tg://user?id={message.from_user.id}">@{user}</a>
<b>UserId:</b> <code>{user_id}</code>
<b>File Name: <b>{title}</b>
<b>TeraBox Link:</b> {url}
<b>Download Time:</b> <i>{download_time}</i>
    """
    file_extension = os.path.splitext(title)[1].lower()
    file_size = os.path.getsize(title)
    with open(title, "rb") as file:
        proc.edit("Now Sending...")
        start_time = time.time()
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
            # Send as photo
            xx = app.send_photo(config.chat_id, file, caption=db_caption)
        elif file_extension in ['.mp4', '.mpeg4', '.gif']:
            # Send as video
            xx = app.send_video(config.chat_id, file, caption=db_caption, supports_streaming=True)
            #file_id = xx.video.file_id
        elif file_extension in ['.mp3', '.aac', '.ogg']:
            # Send as audio
            xx = app.send_audio(config.chat_id, file, caption=db_caption)
        elif file_extension in ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx']:
            # Send as document
            xx = app.send_document(config.chat_id, file, caption=db_caption)
        else:
            # Send as document by default
            xx = app.send_document(config.chat_id, file, caption=db_caption)
    forward_caption = f"""
File Name: {title}
Uploaded By @RF_TeraBot
    """
    xx.copy(chat_id = message.from_user.id, caption=forward_caption, disable_notification=True)
    os.remove(title)
    #proc.edit(f"""<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>Your File: {title} Send In Inbox.""")
    
    
    
    
    
    
    
    
    
@app.on_message(filters.command("add", prefixes="/") & filters.private)
def add_user(client, message):
    #owner_list = [1927696336, 5489376698]  # Replace with your own list of owner user IDs
    user_id = message.from_user.id

    if user_id not in owner_list:
        message.reply_text("You are not authorized to use this command.")
        return

    command = message.text.split(" ", 1)[1].strip()

    if command.startswith("@"):
        username = command[1:]
        try:
            user = client.get_users(username)
            user_id = user.id if user else None
        except ValueError:
            message.reply_text("Invalid username. Please provide a valid username.")
            return
    else:
        try:
            user_id = int(command)
        except ValueError:
            message.reply_text("Invalid user ID. Please provide a valid user ID.")
            return

    if user_id:
        try:
            user = client.get_users(user_id)
            username = user.username if user.username else "---"
            first = user.first_name if user.first_name else "---"
            last = user.last_name if user.last_name else "---"

            with open('admin.txt', 'r') as file:
                lines = [line.strip() for line in file.readlines()]

                if str(user_id) in lines:
                    message.reply_text("User already added.")
                    return

            with open('admin.txt', 'a') as file:
                file.write(str(user_id) + "\n")

            message.reply_text(f"User added successfully:\n\n"
                               f"User ID: {user_id}\n"
                               f"Username: {username}\n"
                               f"First Name: {first}\n"
                               f"Last Name: {last}")
        except UserNotParticipant:
            message.reply_text("The user is not a participant in this chat.")
        except Exception as e:
            message.reply_text("Failed to add user. Please try again.")
            print(e)
    else:
        message.reply_text("Invalid user ID. Please provide a valid user ID.")







@app.on_message(filters.command("remove", prefixes="/") & filters.private)
def remove_user(client, message):
    #owner_list = [123456789, 987654321]  # Replace with your own list of owner user IDs
    user_id = message.from_user.id

    if user_id not in owner_list:
        message.reply_text("You are not authorized to use this command.")
        return

    command = message.text.split(" ", 1)[1].strip()

    if command.startswith("@"):
        username = command[1:]
        try:
            user = client.get_users(username)
            user_id = user.id if user else None
        except ValueError:
            message.reply_text("Invalid username. Please provide a valid username.")
            return
    else:
        try:
            user_id = int(command)
        except ValueError:
            message.reply_text("Invalid user ID. Please provide a valid user ID.")
            return

    if user_id:
        with open('admin.txt', 'r+') as file:
            lines = [line.strip() for line in file.readlines()]
            file.seek(0)

            if str(user_id) not in lines:
                message.reply_text("User is not in the users list.")
                return

            file.writelines(line + "\n" for line in lines if line.strip() != str(user_id))
            file.truncate()

        message.reply_text("User ID has been removed from the users list.")
    else:
        message.reply_text("Invalid user ID or username.")







@app.on_message(filters.command("users", prefixes="/") & filters.private)
def admin_list(client, message):
    #owner_list = [123456789, 987654321]  # Replace with your own list of owner user IDs
    user_id = message.from_user.id

    if user_id not in owner_list:
        message.reply_text("You are not authorized to use this command.")
        return

    with open('admin.txt', 'r') as file:
        admin_ids = file.read().strip().split('\n')

    if admin_ids:
        response = f"Total Users: {len(admin_ids)}\n\nUsers in the bot:\n"
        for admin_id in admin_ids:
            try:
                username_or_firstname = config.get_username_or_firstname(client, int(admin_id))
                response += f"@{username_or_firstname}\n"
            except Exception:
                response += f"User ID: {admin_id}\n"

        message.reply_text(response)
    else:
        message.reply_text("No users found.")










    """
    with open('admin.txt', 'r') as file:
        admin_ids = file.readlines()
        admin_ids = [admin_id.strip() for admin_id in admin_ids]
    """
    #print(admin_ids)

    
    

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
app.run()

