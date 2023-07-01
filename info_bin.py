from bs4 import BeautifulSoup
import requests
from flag import _get_flag




def _info_bin(bin):
    bin = str(bin)[:6]
    try:
        req = 'https://bincheck.io/details/' + bin
        r = requests.get(req)
        soup = BeautifulSoup(r.content, "html.parser")
        k = soup.findAll('td', width="65%")
        try:
            a1 = k[0].text
        except:
            a1 = ""
        try:
            a2 = k[1].text.strip()
        except:
            a2 = ""
        try:
            a3 = k[2].text.strip()
        except:
            a3 = ""
        try:
            b1 = k[3].text.strip()
        except:
            b1 = ""
        #try:
        #    b2 = k[10].text.strip()
        #except:
        #    b2 = ""
        #try:
        #    b3 = k[8].text.strip()
        #except:
        #    b3 = ""
        try:
            c1 = k[6].text.strip()
        except:
            c1 = ""
        try:
            c2 =_get_flag(k[8].text)
        except:
            c2 = ""
        return {
            "Bin":f"{a1} - {a2} - {a3}",
            "Bank":f"{b1}",
            "Country":f"{c1} {c2}"
        }
    except Exception as e:
        print(e)
        return {
            "Bin":"",
            "Bank":"",
            "Country":""
        }