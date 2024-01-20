import telebot
import datetime
import time
import os,sys,re
import subprocess
import requests
import datetime
import psutil
from aiogram import Bot, Dispatcher, executor, types
from keep_alive import keep_alive
keep_alive()

bot_token = Bot(token=os.environ.get('token'))
bot = telebot.TeleBot(bot_token)
chat_id_test = -1002135489631
processes = []
ADMIN_ID = '6764044761'
allowed_group_id = -1001992953662
last_used_times = {}
blocked_numbers = []
from telebot import types

def thay_doi_so_cuoi(input_str):


    # Lấy 5 số cuối cùng của dãy số
    so_cuoi = input_str[-5:]

    # Thay thế 5 số cuối bằng "*"
    so_cuoi_thay_doi = '*' * 7
    result_str = input_str[:-7] + so_cuoi_thay_doi

    return result_str

@bot.message_handler(commands=['spam'])
def spam(message):
    gr = message.chat.id
    user = message.from_user.full_name
    if gr != allowed_group_id:
        bot.send_message(chat_id=message.from_user.id,text=f'Bot chỉ hoạt động trong nhóm SPAM SMS CALL (PRIVATE)')
        return
    if len(message.text.split()) == 1:
        bot.send_message(chat_id=allowed_group_id,text='/spam <sđt>')
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except Exception as e:
            print(f"Không thể xóa tin nhắn: {e}")
        return
    phone_number = message.text.split()[1]
    phone_number_thay_doi = thay_doi_so_cuoi(phone_number)
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
        bot.send_message(chat_id=allowed_group_id,text='SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except Exception as e:
            print(f"Không thể xóa tin nhắn: {e}")
        return
    if phone_number in ["0355806801"]:
        # Số điện thoại nằm trong danh sách cấm
        bot.send_message(chat_id=allowed_group_id,text="Số này nằm trong danh sách cấm!")
        try:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        except Exception as e:
            print(f"Không thể xóa tin nhắn: {e}")
        return
    current_time = time.time()
    if phone_number in last_used_times:
        last_used_time = last_used_times[phone_number]
        if current_time - last_used_time < 30:
            # Thông báo cho người dùng rằng số đang trong quá trình tấn công, cần chờ thời gian
            remaining_time = int(30 - (current_time - last_used_time))
            bot.send_message(chat_id=allowed_group_id,text=f"Số {phone_number} đang trong quá trình tấn công. Vui lòng chờ {remaining_time} giây mới tấn công lại số này.")
            try:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            except Exception as e:
                print(f"Không thể xóa tin nhắn: {e}")
            return
    time.sleep(1)
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Không thể xóa tin nhắn: {e}")
    bot.send_message(chat_id=allowed_group_id,text=f'Thành công spam số: {phone_number_thay_doi}\nNgười Gửi Lệnh: {user}\nThời gian tấn công: 200s\nOwner: Châu Ngọc Thiên Đăng\nLưu ý: Chỉ nên dùng troll bạn bè')
    last_used_times[phone_number] = current_time
    file_path = os.path.join(os.getcwd(), "api.py")
    process = subprocess.Popen(["python", file_path, phone_number])
    processes.append(process)



@bot.message_handler(commands=['help'])
def help(message):
    help_text = '''/spam + sđt\n/admin'''
    bot.send_message(chat_id=allowed_group_id,text=help_text)

@bot.message_handler(commands=['admin'])
def admin(message):
  user_id = message.from_user.id
  if str(user_id) != ADMIN_ID:
      bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
      return
  admin_panel = '''
  Danh sách lệnh:
  - /status : xem cpu,ram,disk hiện tại
  - /ongoing : xem số quy trình đang chạy
  - /resetbot : reset tất cả bot
  - /stopall : dừng lại tất cả các bot
  - /admin : Admin Panel (ADMIN)
  '''
  bot.send_message(chat_id=ADMIN_ID,text= admin_panel)
# status
@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime_text = f"Bot đã hoạt động trong {uptime}"

    cpu_usage = psutil.cpu_percent()
    cpu_text = f"CPU Đang Dùng: {cpu_usage}%"

    memory_usage = psutil.virtual_memory().percent
    memory_text = f"Memory Đang Dùng: {memory_usage}%"

    disk_usage = psutil.disk_usage('/').percent
    disk_text = f"Disk Đang Dùng: {disk_usage}%"

    status_text = f"{uptime_text}\n{cpu_text}\n{memory_text}\n{disk_text}"
    bot.send_message(chat_id=ADMIN_ID,text=status_text)

@bot.message_handler(commands=['ongoing'])
def ongoings(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    process_count = len(processes)
    bot.send_message(chat_id=ADMIN_ID,text=f'Số quy trình đang chạy: {process_count}.')
# khoir dong lai bot
@bot.message_handler(commands=['resetbot'])
def restart(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    bot.send_message(chat_id=ADMIN_ID,text='Bot sẽ được khởi động lại trong giây lát...')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.message_handler(commands=['stopall'])
def stop(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    bot.send_message(chat_id=ADMIN_ID,text='Đã dừng tệp api.py')
    time.sleep(2)
    bot.stop_polling()


# lenh lo 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(chat_id=allowed_group_id, text='Mày nhắn gì vậy? xài lệnh /spam đi chứ !!')
    time.sleep(1)
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Không thể xóa tin nhắn: {e}")
bot.polling()

