from cfscrape import create_scraper
import requests
import json



########------------- Bypass------------ ###########
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


def terabox(url) -> str:
    session = create_scraper()
    try:
        try:
            res = session.request('GET', url)
            print (res)
        except Exception as e:
            return (f"ERROR: {e}")
        key = res.url.split('?surl=')[-1]
        if cookies is None: return f"Terabox Cookie is not Set"
        url2 = f'https://www.4funbox.com/share/list?app_id=250528&shorturl={key}&root=1'
        res = requests.get(url2, cookies=cookies)
        bypass = json.loads(res.text)
        if isinstance(bypass, str):
            return "error"
        elif int(bypass['errno']) != 0:
            return "error"
        else:
            return bypass
    except Exception as e:
        return (f"ERROR: {e}")
        


