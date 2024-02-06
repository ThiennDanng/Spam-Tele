import telebot
import datetime
import time
import os,sys,re
import subprocess
import requests
import datetime
import psutil
from telebot import types
from datetime import datetime, timedelta
from keep_alive import keep_alive
keep_alive()

bot_token = '6839204888:AAFIglxn5nB5Yf9NiaKSDzZzIdftmiGyJCo' 
bot = telebot.TeleBot(bot_token)
processes = []
ADMIN_ID = '6764044761'
allowed_group_id = -1002003023432
last_used_times = {}


def thay_doi_so_cuoi(input_str):
    so_cuoi = input_str[-7:]
    so_cuoi_thay_doi = '*' * 7
    result_str = input_str[:-7] + so_cuoi_thay_doi
    return result_str

def TimeStamp():
    now = str(datetime.date.today())
    return now

@bot.message_handler(commands=['sppre'])
def superspam(message):
  gr = message.chat.id
  user = message.from_user.full_name
  if gr != allowed_group_id:
    bot.send_message(chat_id=message.from_user.id,text=f'Bot chỉ hoạt động trong nhóm: t.me/spamnonstopv2')
    return
  user_id = message.from_user.id
  if not os.path.exists(f"./vip/{user_id}.txt"):
    bot.send_message(chat_id=allowed_group_id, text='Vui lòng đăng kí 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 để sử dụng\nSử dụng lệnh /premium để xem chi tiết.')
    return
  fo = open(f"./vip/{user_id}.txt")
  data = fo.read().split("|")
  qua_khu = data[0].split('-')
  qua_khu = datetime(int(qua_khu[0]), int(qua_khu[1]), int(qua_khu[2]))  # Sửa lại đây
  ngay_hien_tai = datetime.now()  # Sửa lại đây để sử dụng datetime
  so_ngay = (ngay_hien_tai - qua_khu).days
  if so_ngay < 0:
    bot.send_message(chat_id=allowed_group_id, text='𝐏𝐑𝐄𝐌𝐈𝐔𝐌 cài vào ngày khác !')
    return
  if so_ngay >= int(data[1]):
    bot.send_message(chat_id=allowed_group_id,text='𝐏𝐑𝐄𝐌𝐈𝐔𝐌 Hết Hạn Vui Lòng ib Admin ')
    os.remove(f"./vip/{user_id}.txt")
    return
  if len(message.text.split()) == 1:
        bot.send_message(chat_id=allowed_group_id,text='/sppre + [SĐT]')
        return
  phone_number = message.text.split()[1]
  phone_number_thay_doi = thay_doi_so_cuoi(phone_number)
  if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
    bot.send_message(chat_id=allowed_group_id,text='SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
    return
  if phone_number in ["035580687"]:
    bot.send_message(chat_id=allowed_group_id,text="Số này nằm trong danh sách cấm!")
    return
  bot.send_message(chat_id=allowed_group_id,text=f'Thành công spam số: {phone_number_thay_doi}\nNgười Gửi Lệnh: {user}\nThời gian: 200s\nOwner: Châu Ngọc Thiên Đăng\nPlan Premium: 𝐀𝐜𝐭𝐢𝐯𝐞 ✅\nLưu ý: Chỉ nên dùng troll bạn bè')
  file_path = os.path.join(os.getcwd(), "api_vip.py")
  process = subprocess.Popen(["python", file_path, phone_number])
  processes.append(process)
###########################################  SPAM
###########################################  SPAM
###########################################  SPAM
@bot.message_handler(commands=['spam'])
def spam(message):
    gr = message.chat.id
    user = message.from_user.full_name
    if gr != allowed_group_id:
        bot.send_message(chat_id=message.from_user.id,text=f'Bot chỉ hoạt động trong nhóm: t.me/spamnonstopv2')
        return
    if len(message.text.split()) == 1:
        bot.send_message(chat_id=allowed_group_id,text='/spam + [SĐT]')
        return
    phone_number = message.text.split()[1]
    phone_number_thay_doi = thay_doi_so_cuoi(phone_number)
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
        bot.send_message(chat_id=allowed_group_id,text='SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return
    if phone_number in ["0355806807"]:
        # Số điện thoại nằm trong danh sách cấm
        bot.send_message(chat_id=allowed_group_id,text="Số này nằm trong danh sách cấm!")
        return
    current_time = time.time()
    if phone_number in last_used_times:
        last_used_time = last_used_times[phone_number]
        if current_time - last_used_time < 30:
            # Thông báo cho người dùng rằng số đang trong quá trình tấn công, cần chờ thời gian
            remaining_time = int(30 - (current_time - last_used_time))
            bot.send_message(chat_id=allowed_group_id,text=f"Số {phone_number} đang trong quá trình tấn công. Vui lòng chờ {remaining_time} giây mới tấn công lại số này.")
            return
    time.sleep(1)
    bot.send_message(chat_id=allowed_group_id,text=f'Thành công spam số: {phone_number_thay_doi}\nNgười Gửi Lệnh: {user}\nThời gian: 90s\nOwner: Châu Ngọc Thiên Đăng\nPlan Premium: 𝐍𝐨𝐧𝐞 ❌\nLưu ý: Chỉ nên dùng troll bạn bè')
    last_used_times[phone_number] = current_time
    file_path = os.path.join(os.getcwd(), "api_free.py")
    process = subprocess.Popen(["python", file_path, phone_number])
    processes.append(process)


@bot.message_handler(commands=['mypre'])
def mypre(message):
    user_id = message.from_user.id
    user_n = message.from_user.full_name
    if not os.path.exists(f"./vip/{user_id}.txt"):
        bot.send_message(chat_id=allowed_group_id, text='Bạn chưa đăng ký 𝐏𝐑𝐄𝐌𝐈𝐔𝐌. Sử dụng lệnh /premium để xem chi tiết.')
        return

    fo = open(f"./vip/{user_id}.txt")
    data = fo.read().split("|")
    ngay_mua_str = data[0]
    so_ngay_het_han = int(data[1])
    today = datetime.now()
    ngay_mua = datetime.strptime(ngay_mua_str, '%Y-%m-%d')
    ngay_het_han = ngay_mua + timedelta(days=so_ngay_het_han)
    so_ngay_con_lai = abs((ngay_het_han - today).days)
    no = f"Thông tin 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 của bạn:\n\nUser: {user_n}\nID: {user_id}\nNgày mua: {ngay_mua.strftime('%Y-%m-%d')}\nNgày hết hạn: {ngay_het_han.strftime('%Y-%m-%d')}\nSố ngày: {so_ngay_het_han}\nSố ngày còn lại: {so_ngay_con_lai}"
    bot.reply_to(message,no)


@bot.message_handler(commands=['start'])
def st(message):
    bot.send_message(chat_id=message.from_user.id,text="Chào Bạn, Chúc Bạn Một Ngày Mới Tốt Lành")

@bot.message_handler(commands=['help'])
def help(message):
    help_text = '''Bảng Menu Lệnh:\n\n~[+] => /spam + [SĐT] (Free)\n~[+] => /sppre + [SĐT] (𝐏𝐑𝐄𝐌𝐈𝐔𝐌)\n~[+] => /premium (Mua Premium)\n~[+] => /mypre (Xem TT Pre của bạn)'''
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['premium'])
def pre(message):
    bot.send_message(chat_id=allowed_group_id,text='Thông Tin Bản 𝐏𝐑𝐄𝐌𝐈𝐔𝐌:\n\n+ Api nhiều hơn free\n+ Có Spam Call (Đặc Biệt)\n+ Thời gian Spam: 200s\n+ Không giới hạn time Spam\n\nBảng Giá Premium:\n+ 15k - 1 Tuần (7 ngày)\n+ 30k - 1 Tháng (30 ngày)\n+ 50k - 5 Tháng (150 ngày)\n+ 99k - 1 Năm (365 ngày)\n\nVui lòng liên hệ @thiendangg để được mua 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 !')

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
  - /adduser : thêm người dùng premium
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
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
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
@bot.message_handler(commands=['adduser'])
def them(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    if len(message.text.split()) == 1:
      bot.reply_to(message, '<iduser> <Năm>-<tháng>-<ngày> (hiện tại)')
      return
    idvip = message.text.split(" ")[1]
    if len(message.text.split()) == 2:
      bot.reply_to(message, 'Ngày hôm nay YYYY/MM/DD')
      return
    ngay = message.text.split(" ")[2]
    if len(message.text.split()) == 3:
      bot.reply_to(message, 'Ngày hết hạn')
      return
    hethan = message.text.split(" ")[3]
    fii = open(f"./vip/{idvip}.txt","w")
    fii.write(f"{ngay}|{hethan}")
    bot.reply_to(message, f'Thêm Thành Công {idvip} Làm Vip. Bây giờ bạn có thể sử dụng lệnh /sppre nhé!')
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text.startswith('/'):  # Kiểm tra nếu tin nhắn bắt đầu bằng '/'
        pass
    else:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

    

bot.polling()
