




api_id = 14953313
api_hash = '4f26f8e9f0d42ea55ab19325b5e613d1'
bot_token = "6295817509:AAGM3PsswyvTDGyQ5RE757mlTdmHLnBxXBY"
chat_id = -1001985490607
message_id = 194






forward_caption = f"""
hello
"""


def get_username_or_firstname(client, user_id):
    try:
        user = client.get_users(user_id)
        if user.username:
            return user.username
        elif user.first_name:
            return f"""<a href="tg://user?id={user_id}">{user.first_name}</a>"""
        else:
            return "Unknown"
    except Exception:
        return "Unknown"
