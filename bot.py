import re
import time
import os
import logging
from pyrogram import Client, filters

logging.basicConfig(level=logging.INFO)

api_id = 14953313  # Replace with your API ID
api_hash = "4f26f8e9f0d42ea55ab19325b5e613d1"  # Replace with your API hash
session_name = "ArtOfWorking"  # Replace with your desired session name

# Define a filter for URLs in messages
pattern = r"\/(\d+)\/(\d+)"  # Updated pattern to escape the slashes properly
pattern1 = r"/full\s+(\w+),\s+(\w+)"


from_channel = 'a'




def copy_messages(to_chat, message, client):
    try:
        time.sleep(20)
        if message.text:
            # Edit the message with the text content
            app.send_message(to_chat, message.text)
            return
        if message.media:
            file_path = app.download_media(message)
            file_extension = os.path.splitext(file_path)[1].lower()
            if message.caption:
                caption = message.caption
            else:
                caption = "@ART_OF_WORKING"
            if os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                        app.send_photo(to_chat, file, caption=caption)
                    elif file_extension in ['.mp4', '.mpeg4', '.gif']:
                        app.send_video(to_chat, file, caption=caption, supports_streaming=True)
                    elif file_extension in ['.mp3', '.aac', '.ogg']:
                        app.send_audio(to_chat, file, caption=caption)
                    else:
                        app.send_document(to_chat, file, caption=caption)
        os.remove(file_path)
            
    except Exception as e:
        print(e)








# Define the copy_channel function
def copy_channel(client, message):
    chat_id = message.chat.id
    try:
        global from_channel
        # Match the pattern in the message text
        match = re.match(r"/full (-?\d+), (-?\d+)", message.text)
        if match:
            # Extract the channel IDs using group numbers
            from_channel = match.group(1)
            to_channel = match.group(2)
            print(f"From Channel ID: {from_channel}")
            print(f"To Channel ID: {to_channel}")

            try:
                if from_channel.startswith("-100"):
                    from_chat = int(from_channel)
                else:
                    from_chat = client.get_chat(from_channel).id

                if to_channel.startswith("-100"):
                    to_chat = int(to_channel)
                else:
                    to_chat = client.get_chat(to_channel).id

                messages = client.get_chat_history(from_chat)

                for message in reversed(list(messages)):
                    print (message)
                    copy_messages(to_chat, message, client)

            except Exception as e:
                print(f"Error: {str(e)}")

    except Exception as e:
        print(f"Error: {str(e)}")














# Create a Pyrogram client
app = Client(session_name, api_id, api_hash)


@app.on_message(filters.command("give") & filters.me)
def echo_handler(client, message):
    chat_id = message.chat.id
    print (message)
    try:
        text = message.text.split(" ", 1)[1]
        if 'https://t.me/c/' in text:
            matches = re.findall(pattern, text)
            if matches:
                channel_id = int('-100' + matches[0][0])
                message_id = int(matches[0][1])

        elif 'https://t.me/' in text:
            try:
                split_url = text.split("/")
                channel_name = split_url[3]
                message_id = int(split_url[4])
                chat = app.get_chat(channel_name)
                # Extract the channel ID from the chat information
                channel_id = chat.id
            except Exception as e:
                
                print(f"Public Channel Error--{e}")
                return

        try:
            msg = app.get_messages(int(channel_id), message_id)
            print (msg)
            if msg.caption:
                caption = msg.caption
            else:
                caption = "@ART_OF_WORKING"

            if msg.text:
                # Edit the message with the text content
                app.edit_message_text(chat_id, message.id, msg.text)
                return

            if msg.media:
                file_path = client.download_media(msg, progress=progress)
                file_extension = os.path.splitext(file_path)[1].lower()

                time.sleep(10)

                if os.path.exists(file_path):
                    with open(file_path, "rb") as file:
                        if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                            # Send as photo
                            app.send_photo(chat_id, file, caption=caption, reply_to_message_id=message.id)
                        elif file_extension in ['.mp4', '.mpeg4', '.gif']:
                            # Send as video
                            app.send_video(chat_id, file, caption=caption, supports_streaming=True, reply_to_message_id=message.id)
                        elif file_extension in ['.mp3', '.aac', '.ogg']:
                            # Send as audio
                            app.send_audio(chat_id, file, caption=caption, reply_to_message_id=message.id)
                        else:
                            app.send_document(chat_id, file, caption=caption, reply_to_message_id=message.id)

                    try:
                        os.remove(file_path)  # Delete downloaded file
                    except Exception as e:
                        print(e)
                else:
                    print("File not found:", file_path)
        except Exception as e:
            print(e)
            return

    except Exception as e:
        print(e)



# Register the copy_channel function as a command handler
@app.on_message(filters.command("full") & filters.me)
def handle_copy_channel(client, message):
    copy_channel(client, message)
    



# Define and run the main function
def main():
    app.run()


if __name__ == '__main__':
    main()
