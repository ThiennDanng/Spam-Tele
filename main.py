import requests
import mysql.connector
import telebot
import time
from PIL import Image
from io import BytesIO
import urllib.parse
import os,re
import datetime
import sys
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

bot = telebot.TeleBot("7871878256:AAFckp7IZj446BMJalEfuZ3cq1RJraI2FaE")
admin_id = "6764044761"
verification_codes = {}  
pending_emails = {}  

conn = mysql.connector.connect(
    host="hotrosub.site",      # Ví dụ: "127.0.0.1" hoặc "yourdomain.com"
    user="qhotrosubsite_telebot",     
    password="qhotrosubsite_telebot",  
    database="qhotrosubsite_telebot"    
)
cursor = conn.cursor(dictionary=True)

def get_user_info(telegram_id):
    cursor.execute("SELECT * FROM users WHERE id_telegram = %s", (telegram_id,))
    user = cursor.fetchone()
    return user

def is_user_banned(user_id):
    cursor.execute("SELECT banned FROM users WHERE id_telegram = %s", (user_id,))
    result = cursor.fetchone()
    if result is None:
        return False 
    return result["banned"] == 1  

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    mess = message.chat.id
    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return
    bot.send_message(chat_id=mess, text="Xin chào bạn! Để sử dụng bot, vui lòng xác thực email bằng lệnh /gmail.")

@bot.message_handler(commands=['gmail'])
def gmail_handler(message):
    user_id = message.from_user.id
    mess = message.chat.id

    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return
    cursor.execute('SELECT gmail FROM users WHERE id_telegram = %s', (user_id,))
    user = cursor.fetchone()

    if user and user['gmail']: 
        bot.send_message(chat_id=mess, text="Bạn đã xác thực email trước đó.")
        return

    args = message.text.split()
    if len(args) == 1:
        bot.send_message(chat_id=mess, text="Vui lòng sử dụng lệnh: `/gmail [email của bạn]`", parse_mode='Markdown')
        return

    email = args[1].strip()
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        bot.send_message(chat_id=mess, text="*Định dạng email không hợp lệ! Vui lòng nhập email đúng định dạng.*", parse_mode='Markdown')
        return

    cursor.execute('SELECT id_telegram FROM users WHERE gmail = %s', (email,))
    existing_user = cursor.fetchone()
    if existing_user:
        bot.send_message(chat_id=mess, text="❌ Email này đã được đăng ký bởi một tài khoản khác. Vui lòng sử dụng email khác.")
        return

    verification_code = str(random.randint(100000, 999999))
    verification_codes[user_id] = verification_code 
    pending_emails[user_id] = email  

    sender_email = "cntdbot@gmail.com"
    sender_password = "xbbc ttyj okev aocr"
    subject = "Xác minh tài khoản của bạn"
    body = f"Chào bạn,\n\nMã xác minh của bạn là: {verification_code}\n\nCảm ơn bạn đã đăng ký!"
    message_email = MIMEMultipart()
    message_email['From'] = sender_email
    message_email['To'] = email
    message_email['Subject'] = subject
    message_email.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message_email.as_string())
        server.quit()
        bot.send_message(chat_id=mess, text=f"📩 Đã gửi mã xác minh tới {email}. Vui lòng nhập mã xác minh bằng lệnh `/verify [mã xác minh]`.")
    except Exception as e:
        bot.send_message(chat_id=mess, text=f"❌ Không thể gửi mã xác minh: {e}")

@bot.message_handler(commands=['verify'])
def verify_handler(message):
    user_id = message.from_user.id
    mess = message.chat.id

    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return

    args = message.text.split()
    if len(args) == 1:
        bot.send_message(chat_id=mess, text="Vui lòng sử dụng lệnh: `/verify [mã xác minh]`", parse_mode='Markdown')
        return

    input_code = args[1]
    if user_id not in verification_codes or verification_codes[user_id] != input_code:
        bot.send_message(chat_id=mess, text="❌ Mã xác minh không hợp lệ hoặc đã hết hạn.")
        return

    cursor.execute('SELECT * FROM users WHERE id_telegram = %s', (user_id,))
    user = cursor.fetchone()

    if user:
        bot.send_message(chat_id=mess, text="✅ Bạn đã xác thực email trước đó.")
    else:
        email = pending_emails.get(user_id)
        if not email:
            bot.send_message(chat_id=mess, text="❌ Lỗi: Không tìm thấy email đã đăng ký. Vui lòng thử lại.")
            return
        
        username = message.from_user.username or "NoUsername"
        registration_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute(
            'INSERT INTO users (id_telegram, gmail, balance, registration_time, username) VALUES (%s, %s, %s, %s, %s)',
            (user_id, email, 0, registration_time, username)
        )
        conn.commit()

        bot.send_message(chat_id=mess, text="✅ Xác thực email thành công! Bạn đã đăng ký tài khoản.\nSử dụng lệnh /services để sử dụng Bot.")

    del verification_codes[user_id]  
    del pending_emails[user_id]  

@bot.message_handler(commands=['naptien'])
def naptien(message):
    user_id = message.from_user.id
    mess = message.chat.id
    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return

    id_user = str(message.from_user.id)
    cursor.execute('SELECT balance FROM users WHERE id_telegram = %s', (id_user,))
    user = cursor.fetchone()

    if user:
        noi_dung = f"CNTDN{id_user}"
        tentk = "CHAU NGOC THIEN DANG"
        stk = '9704229202550376763'
        url = f"https://img.vietqr.io/image/MBBank-{stk}-1.png?amount=&addInfo={noi_dung}&accountName={urllib.parse.quote(tentk)}"

        try:
            response = requests.get(url)
            qr_image = Image.open(BytesIO(response.content))
            bot.send_photo(
                message.chat.id, qr_image, 
                caption=(
                    "💰 *CỔNG THANH TOÁN TỰ ĐỘNG 24/7* 💰\n\n"
                    "🏦 *Ngân hàng:* `MBBank (Hoặc VIETTEL MONEY)`\n"
                    "👤 *Chủ tài khoản:* `CHAU NGOC THIEN DANG`\n"
                    f"💳 *Số tài khoản:* `{stk}`\n"
                    f"📝 *Nội dung nạp của bạn:* `{noi_dung}`\n"
                    "\[Nhấp vào STK và ND để COPY\]\n\n"
                    "⚠️ *Lưu ý:* \n"
                    "🔸 *Nạp tối thiểu:* `10,000 VND`, cộng tiền sau 30\-60s\n"
                    "🔹 *Chuyển sai nội dung:* _Có thể bị mất tiền\!_\n"
                    "🔸 *Nếu sau 10 phút chưa thấy cộng tiền vui lòng liên hệ để được hỗ trợ*\n\n"
                    "📞 *Hỗ trợ:* Dùng lệnh `/hotro` để được trợ giúp\!"
                ),
                parse_mode="MarkdownV2"
            )
        except:
            pass
    else:
        bot.send_message(chat_id=mess, text=f"Để sử dụng bot, vui lòng dùng lệnh /start để đăng ký!")
    conn.commit()

     
@bot.message_handler(commands=['services'])
def helper(message):
    user_id = message.from_user.id
    mess = message.chat.id

    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return

    id_user = str(message.from_user.id)
    cursor.execute('SELECT balance FROM users WHERE id_telegram = %s', (id_user,))
    user = cursor.fetchone()

    if user:
        message_text = (
            "🌟 *Danh sách lệnh của thành viên* 🌟\n\n"
            "💰 /naptien - Nạp tiền vào tài khoản\n"
            "🛠️ /tools - Tools các loại\n"
            "🛒 /buy - Mua tools\n"
            "🪪 /info_user - Thông tin tài khoản của bạn\n"
            "📊 /lichsunap - Kiểm tra lịch sử nạp tiền của bạn\n"
            "📊 /lichsumua - Kiểm tra lịch sử mua hàng của bạn\n"
            "🆘 /hotro - Gửi yêu cầu hỗ trợ đến Admin\n"
        )
        bot.send_message(chat_id=mess, text=message_text)
    else:
        bot.send_message(chat_id=mess, text=f"Để sử dụng bot, vui lòng dùng lệnh /start để đăng ký!")
    conn.commit()
     
@bot.message_handler(commands=['tools'])
def sanpham(message):
    user_id = message.from_user.id
    mess = message.chat.id

    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return

    cursor.execute('SELECT ma_file, name, file_type, price, status, description FROM tools')
    tools = cursor.fetchall()
    
    if tools:
        message_text = "📦 Danh sách các công cụ có sẵn:\n"
        for tool in tools:
            message_text += (
                f"\n🔹 {tool['name']}\n"
                f"- Mã file: {tool['ma_file']}\n"
                f"- Loại file: {tool['file_type']}\n"
                f"- Giá: {tool['price']} VND\n"
                f"- Trạng thái: {tool['status']}\n"
                f"- Mô tả: {tool['description']}\n"
            )
        message_text += "\n🛒 Để mua tool, vui lòng sử dụng lệnh /buy + [mã file]."
        bot.send_message(chat_id=user_id, text=message_text,)
    else:
        bot.send_message(chat_id=user_id, text="Hiện tại chưa có công cụ nào.", parse_mode='Markdown')

@bot.message_handler(commands=['info_user'])
def info(message):
    user_id = message.from_user.id
    mess = message.chat.id

    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return

    id_user = message.from_user.id
    user_info = get_user_info(id_user)

    if user_info:
        bot.send_message(chat_id=user_id, text=f"ID của bạn: {user_info['id_telegram']}\nGmail: {user_info['gmail']}\nĐã nạp: {user_info['paid']} VND\nSố dư của bạn: {user_info['balance']} VND\nThời gian tạo: {user_info['registration_time']}")
    else:
        bot.send_message(chat_id=mess, text="Không tìm thấy thông tin của bạn. Vui lòng đăng ký bằng lệnh /start")

@bot.message_handler(commands=['lichsunap'])
def check_giaodich(message):
    user_id = message.from_user.id
    mess = message.chat.id

    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return

    cursor.execute('SELECT * FROM giaodich WHERE id_telegram = %s', (user_id,))
    records = cursor.fetchall()
    
    if records:
        file_content = f"Lịch sủ nạp tiền của bạn (ID Telegram: {user_id}):\n\n"
        for record in records:
            file_content += f"ID: {record['id']}\n"
            file_content += f"ID Telegram: {record['id_telegram']}\n"
            file_content += f"Số tiền: {record['money']} VND\n"
            file_content += f"Mã giao dịch: {record['ma_giao_dich']}\n"
            file_content += f"Nội dung: {record['noidung']}\n"
            file_content += f"Thời gian: {record['thoi_gian']}\n\n"

        file_path = f"lsnap_{user_id}.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_content)

        with open(file_path, "rb") as file:
            bot.send_document(chat_id=user_id, document=file)
        
        os.remove(file_path)
    else:
        bot.reply_to(message, "Không tìm thấy giao dịch nào của bạn.")
    
@bot.message_handler(commands=['lichsumua'])
def check_giaodich(message):
    user_id = message.from_user.id
    mess = message.chat.id

    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return

    cursor.execute('SELECT * FROM muahang WHERE id_telegram = %s', (user_id,))
    records = cursor.fetchall()
    
    if records:
        file_content = f"Lịch sử mua hàng của bạn (ID Telegram: {user_id}):\n\n"
        for record in records:
            file_content += f"ID: {record['id']}\n"
            file_content += f"ID Telegram: {record['id_telegram']}\n"
            file_content += f"Mã file: {record['ma_file']}\n"
            file_content += f"Số tiền: {record['price']} VND\n"
            file_content += f"Thời gian: {record['thoi_gian']}\n\n"

        file_path = f"lsmua_{user_id}.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_content)

        with open(file_path, "rb") as file:
            bot.send_document(chat_id=user_id, document=file)

        os.remove(file_path)
    else:
        bot.reply_to(message, "Không tìm thấy giao dịch nào của bạn.")

@bot.message_handler(commands=['hotro'])
def hotro(message):
    mess = message.chat.id
    id_user = str(message.from_user.id)
    cursor.execute('SELECT balance FROM users WHERE id_telegram = %s', (id_user,))
    user = cursor.fetchone()
    if user:
        try:
            user_id = message.from_user.id
            if is_user_banned(user_id):
                bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
                return
            id_user = message.from_user.id
            username = message.from_user.username
            issue_message = message.text.replace("/hotro", "").strip()
            
            if not issue_message:
                bot.reply_to(message, "Vui lòng nhập chi tiết vấn đề cần hỗ trợ sau lệnh /hotro.")
                return
            admin_message = (
                f"User: @{username} (ID: {id_user}) cần hỗ trợ!\n"
                f"Nội dung vấn đề: \"{issue_message}\""
            )

            admin_ids = [6764044761]
            for admin_id in admin_ids:
                bot.send_message(chat_id=admin_id, text=admin_message)

            bot.reply_to(message, "Yêu cầu hỗ trợ của bạn đã được gửi đi. Admin sẽ liên hệ với bạn sớm nhất có thể.")
        
        except Exception as e:
            bot.reply_to(message, "Có lỗi xảy ra khi thực hiện lệnh hỗ trợ.")
    else:
        bot.reply_to(message, text="Để sử dụng bot, vui lòng dùng lệnh /start để đăng ký!")
    conn.commit()

@bot.message_handler(commands=['buy'])
def buy(message):
    user_id = message.from_user.id
    mess = message.chat.id
    if is_user_banned(user_id):
        bot.send_message(chat_id=mess, text="🚫 *Bạn đã bị cấm sử dụng bot này*", parse_mode='MarkdownV2')
        return

    id_user = str(message.from_user.id)
    try:
        ma_file = message.text.split()[1]
    except IndexError:
        bot.send_message(chat_id=id_user, text="Vui lòng cung cấp mã hàng muốn mua(xem tại /tools). Ví dụ: /buy MA123")
        return
    file_path = f"./tools/{ma_file}.zip"
    if not os.path.exists(file_path):
        bot.send_message(chat_id=id_user, text="Mã hàng không hợp lệ hoặc file không tồn tại.")
        return
    cursor.execute('SELECT balance FROM users WHERE id_telegram = %s', (id_user,))
    user = cursor.fetchone()
    
    if user:
        balance = float(user['balance'])
        cursor.execute('SELECT price, name FROM tools WHERE ma_file = %s', (ma_file,))
        tool = cursor.fetchone()
        
        if tool:
            price = float(tool['price'])
            tool_name = tool['name']
            
            if balance >= price:
                new_balance = balance - price
                cursor.execute('UPDATE users SET balance = %s WHERE id_telegram = %s', (new_balance, id_user))
                thoi_gian = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute('INSERT INTO muahang (id_telegram, price, ma_file, thoi_gian) VALUES (%s, %s, %s, %s)',
                               (id_user, str(price), ma_file, thoi_gian))
                conn.commit()
                
                # Send the file 
                bot.send_message(chat_id=id_user, text=f"Bạn đã mua thành công tool {tool_name} với mã {ma_file} giá {price} VND.\nSố dư hiện tại của bạn là {new_balance} VND.")
                bot.send_message(chat_id=admin_id, text=f"{user_id} vừa mua thành công tool {tool_name} với giá {price} VND vào lúc {thoi_gian}")
                with open(file_path, 'rb') as file:
                    bot.send_document(chat_id=id_user, document=file)
            else:
                bot.send_message(chat_id=id_user, text="Số dư của bạn không đủ để mua tool này. Vui lòng nạp thêm tiền.")
        else:
            bot.send_message(chat_id=id_user, text="Mã hàng không hợp lệ hoặc không tồn tại.")
    else:
        bot.send_message(chat_id=id_user, text="Không tìm thấy thông tin của bạn. Vui lòng đăng ký bằng lệnh /start (Chat với bot)")

     

#######################              ADMIN COMMANDS              #######################
@bot.message_handler(commands=['adcmd'])
def admin(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
        return
    bot.send_message(chat_id=admin_id, text=(
        "👑 *Admin Panel* 👑\n\n"
        "🔧 *Danh sách lệnh cho admin*:\n"
        "*01* /admin_overview \\- *Tổng quan bot*\n"
        "*02* /checknaptien \\- *Kiểm tra các giao dịch nạp của khách hàng*\n"
        "*02* /checkmuahang \\- *Kiểm tra các giao dịch mua của khách hàng*\n"
        "*03* /checkusers \\- *Kiểm tra danh sách người dùng và số dư*\n"
        "*04* /addmoney \\- *Cộng tiền cho user*\n"
        "*05* /submoney \\- *Trừ tiền của user*\n"
        "*06* /addtool \\- *Thêm tool*\n"
        "*07* /deltool \\- *Xóa tool*\n"
        "*08* /edittoolstatus \\- *Cập nhật trạng thái tool*\n"
        "*09* /noti \\- *Gửi thông báo tới các user*\n"
        "*10* /reply \\- *Gửi thông báo user*\n"
        "*12* /ban \\- *Ban id user*\n"
        "*13* /unban \\- *Unban id user*\n"
        "*14* /banned_list \\- *Xem danh sách người dùng bị ban*\n"
        "*15* /deleteacc \\- *Xóa tài khoản người dùng*\n"
        "*16* /khuyenmai \\- *Tặng khuyến mãi*\n"
        "*17* /resetbot \\- *Reset bot*\n"
        "*18* /stopall \\- *Dừng bot*\n\n"

        "🚨 *Hãy cẩn thận khi sử dụng các lệnh admin\\!*"
    ), parse_mode='MarkdownV2')

@bot.message_handler(commands=['adminoverview'])
def admin_overview(message):
    user_id = str(message.from_user.id)
    if user_id != admin_id:  
        bot.send_message(chat_id=user_id, text="Bạn không có quyền sử dụng lệnh này.")
        return

    try:
        query = """
        SELECT 
            (SELECT COUNT(*) FROM users) AS total_users,
            (SELECT COUNT(*) FROM users WHERE banned = 1) AS banned_users,
            (SELECT COUNT(*) FROM giaodich) AS total_transactions,
            COALESCE((SELECT SUM(money) FROM giaodich), 0) AS total_income,
            COALESCE((SELECT SUM(price) FROM muahang), 0) AS total_paid,
            (SELECT COUNT(*) FROM tools) AS total_files,
            (SELECT COUNT(*) FROM muahang) AS total_sold_files,
            COALESCE((SELECT khuyenmai FROM bonus LIMIT 1), 0) AS promo_value
        """
        cursor.execute(query)
        result = cursor.fetchone()
        total_users = result.get("total_users", 0)
        banned_users = result.get("banned_users", 0)
        total_transactions = result.get("total_transactions", 0)
        total_income = result.get("total_income", 0)
        total_paid = result.get("total_paid", 0)
        total_files = result.get("total_files", 0)
        total_sold_files = result.get("total_sold_files", 0)
        promo_value = result.get("promo_value", 0)

        bot.send_message(
            chat_id=admin_id,
            text=f"📊 *Báo Cáo Hệ Thống* 📊\n"
                 f"🔹 *Người dùng:*\n"
                 f"👥 Tổng khách hàng: {total_users}\n"
                 f"🚫 Bị cấm: {banned_users}\n\n"
                 f"💰 *Giao dịch:*\n"
                 f"🔄 Số giao dịch: {total_transactions}\n"
                 f"📈 Tổng thu nhập: {total_income} VND\n"
                 f"💸 Tổng tiền đã thanh toán: {total_paid} VND\n\n"
                 f"📂 *Sản phẩm:*\n"
                 f"📌 Số file đang bán: {total_files}\n"
                 f"🛒 Số file đã bán: {total_sold_files}\n"
                 f"🎁 Khuyến mãi: {promo_value}%\n"
        ,parse_mode="Markdown")

    except Exception as e:
        bot.send_message(chat_id=admin_id, text=f"❌ Lỗi khi truy vấn database: {e}")

@bot.message_handler(commands=['checknaptien'])
def check_giaodich(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
        return

    cursor.execute('SELECT * FROM giaodich')
    records = cursor.fetchall()
    
    if records:
        file_content = "Các giao dịch trong bảng giaodich:\n\n"
        for record in records:
            file_content += f"ID: {record['id']}\n"
            file_content += f"ID Telegram: {record['id_telegram']}\n"
            file_content += f"Số tiền: {record['money']}\n"
            file_content += f"Mã giao dịch: {record['ma_giao_dich']}\n"
            file_content += f"Nội dung: {record['noidung']}\n"
            file_content += f"Thời gian: {record['thoi_gian']}\n\n"

        file_path = "naptien.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_content)

        with open(file_path, "rb") as file:
            bot.send_document(chat_id=admin_id, document=file)

        os.remove(file_path)
    else:
        bot.reply_to(message, "Bảng giaodich hiện không có giao dịch nào.")
    
@bot.message_handler(commands=['checkmuahang'])
def check_giaodich(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
        return

    cursor.execute('SELECT * FROM muahang')
    records = cursor.fetchall()
    
    if records:
        file_content = "Các giao dịch trong bảng muahang:\n\n"
        for record in records:
            file_content += f"ID: {record['id']}\n"
            file_content += f"ID Telegram: {record['id_telegram']}\n"
            file_content += f"Mã file: {record['ma_file']}\n"
            file_content += f"Số tiền: {record['price']} VND\n"
            file_content += f"Thời gian: {record['thoi_gian']}\n\n"

        file_path = "muahang.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_content)

        with open(file_path, "rb") as file:
            bot.send_document(chat_id=admin_id, document=file)
        
        os.remove(file_path)
    else:
        bot.reply_to(message, "Bảng muahang hiện không có giao dịch nào.")

@bot.message_handler(commands=['checkusers'])
def check_users(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return

    cursor.execute('SELECT id_telegram, balance, username FROM users')
    records = cursor.fetchall()
    
    if records:
        file_content = "Danh sách các thành viên:\n\n"
        for record in records:
            file_content += f"ID: {record['id_telegram']} (@{record['username']}) - Số dư: {record['balance']}\n"

        file_path = "thanhvien.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(file_content)

        with open(file_path, "rb") as file:
            bot.send_document(chat_id=admin_id, document=file)
        
        os.remove(file_path)
    else:
        bot.reply_to(message, "Bảng muahang hiện không có giao dịch nào.")

@bot.message_handler(commands=['addmoney'])
def addmoney(message):
    if str(message.from_user.id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    
    try:
        args = message.text.split()
        if len(args) != 3:
            bot.reply_to(message, "Sử dụng lệnh /addmoney [ID Telegram] [Số tiền].")
            return

        id_user, amount = args[1], float(args[2])
        
        cursor.execute('UPDATE users SET balance = balance + %s WHERE id_telegram = %s', (amount, id_user))
        conn.commit()
        bot.reply_to(message, f"Đã thêm {amount} VND vào tài khoản của {id_user}.")
         
    except Exception as e:
        bot.reply_to(message, "Có lỗi xảy ra khi thêm tiền: " + str(e))

@bot.message_handler(commands=['submoney'])
def submoney(message):
    if str(message.from_user.id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    
    try:
        args = message.text.split()
        if len(args) != 3:
            bot.reply_to(message, "Sử dụng lệnh /submoney [ID Telegram] [Số tiền].")
            return

        id_user, amount = args[1], float(args[2])
        
        cursor.execute('UPDATE users SET balance = balance - %s WHERE id_telegram = %s', (amount, id_user))
        conn.commit()
        bot.reply_to(message, f"Đã trừ {amount} VND từ tài khoản của {id_user}.")
         
    except Exception as e:
        bot.reply_to(message, "Có lỗi xảy ra khi trừ tiền: " + str(e))

@bot.message_handler(commands=['addtool'])
def add_tool(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return

    msg = bot.send_message(chat_id=user_id, text="Hãy nhập thông tin tool theo định dạng:\nTên tool | Mã file | Loại file | Giá | Trạng thái | Mô tả")
    bot.register_next_step_handler(msg, process_tool_info)

def process_tool_info(message):
    tool_info = message.text

    try:
        tool_name, file_code, file_type, price, status, description = [part.strip() for part in tool_info.split('|')]
        tool_name = tool_name.upper()
        cursor.execute('''
            INSERT INTO tools (ma_file, name, file_type, price, status, description) 
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (file_code, tool_name, file_type, price, status, description))
        conn.commit()
         
        bot.send_message(chat_id=message.chat.id, text="Tool đã được thêm thành công!")
    
    except ValueError:
        bot.send_message(chat_id=message.chat.id, text="⚠️ Vui lòng nhập đúng định dạng:\nTên tool | Mã file | Loại file | Giá | Trạng thái | Mô tả")

@bot.message_handler(commands=['deltool'])
def delete_tool(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return

    msg = bot.send_message(chat_id=user_id, text="Hãy nhập tên tool hoặc mã file của tool cần xóa:")
    bot.register_next_step_handler(msg, process_delete_tool)

def process_delete_tool(message):
    tool_identifier = message.text.strip().upper()


    cursor.execute('DELETE FROM tools WHERE ma_file = %s OR name = %s', (tool_identifier, tool_identifier))
    conn.commit()

    if cursor.rowcount > 0:
        bot.send_message(chat_id=message.chat.id, text=f"Tool '{tool_identifier}' đã được xóa thành công.")
    else:
        bot.send_message(chat_id=message.chat.id, text=f"Không tìm thấy tool '{tool_identifier}'.")

@bot.message_handler(commands=['edittoolstatus'])
def edit_tool_status(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
        return

    msg = bot.send_message(chat_id=user_id, text="Nhập thông tin theo định dạng:\nTên tool | Trạng thái mới | Giá mới")
    bot.register_next_step_handler(msg, process_edit_tool_status)

def process_edit_tool_status(message):
    try:
        tool_info = message.text.split('|')
        if len(tool_info) < 3:
            raise ValueError("Thiếu thông tin")

        tool_identifier = tool_info[0].strip().upper()
        new_status = tool_info[1].strip()
        new_price = float(tool_info[2].strip())

        cursor.execute('''
            UPDATE tools 
            SET status = %s, price = %s 
            WHERE ma_file = %s OR name = %s
        ''', (new_status, new_price, tool_identifier, tool_identifier))
        conn.commit()

        if cursor.rowcount > 0:
            bot.send_message(chat_id=message.chat.id, 
                             text=f"🔄 Tool '{tool_identifier}' đã được cập nhật:\n- Trạng thái: {new_status}\n- Giá: {new_price} VND")
        else:
            bot.send_message(chat_id=message.chat.id, 
                             text=f"⚠️ Không tìm thấy tool '{tool_identifier}'.")

    except ValueError:
        bot.send_message(chat_id=message.chat.id, 
                         text="⚠️ Vui lòng nhập đúng định dạng:\nTên tool | Trạng thái mới | Giá mới\nVí dụ: ToolX | Active | 100000")

@bot.message_handler(commands=['noti'])
def noti_command(message):
    try:
        user_id = message.from_user.id
        if str(user_id) != admin_id:
            bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
            return

        notification_message = message.text.replace("/noti", "").strip()
        
        if not notification_message:
            bot.reply_to(message, "Vui lòng nhập nội dung thông báo sau lệnh /noti.")
            return

        cursor.execute("SELECT id_telegram FROM users")
        users = cursor.fetchall()
        for user in users:
            user_id = user[0]
            try:
                bot.send_message(user_id, notification_message)
            except:pass
        bot.reply_to(message, "Thông báo đã được gửi đến tất cả người dùng.")
    except Exception as e:
        bot.reply_to(message, "Có lỗi xảy ra khi thực hiện lệnh thông báo.")

@bot.message_handler(commands=['reply'])
def reply(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
        return
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        bot.send_message(chat_id=message.chat.id, text='Sử dụng lệnh: /reply + [ID] + [Message]', parse_mode='Markdown')
        return
    id_reply = args[1]
    reply_message = args[2]

    try:
        bot.send_message(chat_id=id_reply, text=reply_message)
        bot.send_message(chat_id=message.chat.id, text=f'Đã gửi tin nhắn tới người dùng {id_reply}.')
        
    except Exception as e:
        bot.send_message(chat_id=message.chat.id, text=f'Lỗi khi gửi tin nhắn: {e}')

@bot.message_handler(commands=['ban'])
def ban_user(message):
    try:
        user_id = message.from_user.id
        if str(user_id) != admin_id:
            bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
            return
        
        command = message.text.split()
        if len(command) >= 3:  
            id_telegram = command[1]
            reason_message = message.text.replace(f"/ban {id_telegram}", "").strip()
            cursor.execute("UPDATE users SET banned = 1, reason = %s WHERE id_telegram = %s", (reason_message, id_telegram))
            conn.commit()
             
            bot.reply_to(message, f"Đã cấm người dùng với ID: {id_telegram} vì lí do: {reason_message}")
            bot.send_message(
                chat_id=id_telegram,
                text=f"Bạn đã bị cấm sử dụng bot @thiendangservices_bot!\nLí do: '{reason_message.upper()}'\nĐể biết thêm chi tiết vui lòng liên hệ @thiendangg"
            )
        else:
            bot.reply_to(message, "Sử dụng lệnh /ban <id_telegram> <reason>")
    except Exception as e:
        bot.reply_to(message, f"Có lỗi xảy ra: {e}")

@bot.message_handler(commands=['unban'])
def unban_user(message):
    try:
        user_id = message.from_user.id
        if str(user_id) != admin_id:
            bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
            return
        command = message.text.split()
        if len(command) == 2:
            id_telegram = command[1]
            cursor.execute("UPDATE users SET banned = 0 WHERE id_telegram = %s", (id_telegram,))
            conn.commit()
             
            bot.reply_to(message, f"Đã mở cấm người dùng với ID: {id_telegram}")
            bot.send_message(
                chat_id=id_telegram,
                text=f"Tài khoản của bạn đã được mở!!"
            )
        else:
            bot.reply_to(message, "Sử dụng lệnh /unban <id_telegram>")
    except Exception as e:
        bot.reply_to(message, f"Có lỗi xảy ra: {e}")

@bot.message_handler(commands=['bannedlist'])
def banned_list(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    
    cursor.execute('SELECT id_telegram, reason FROM users')
    records = cursor.fetchall()
    if records:
        response = "Danh sách các ID bị ban:\n\n"
        for record in records:
            user_id = record['id_telegram']
            if is_user_banned(user_id):
                response += f"ID: {user_id}\nLí do: {record['reason']}\n\n"
    else:
        response = "Bảng users hiện không có ID nào."

    bot.reply_to(message, response)

@bot.message_handler(commands=['deleteacc'])
def delete_account(message):
    try:
        user_id = message.from_user.id
        if str(user_id) != admin_id:
            bot.send_message(chat_id=message.from_user.id, text='Bạn không có quyền sử dụng lệnh này.')
            return
        command = message.text.split()
        if len(command) == 2:
            id_telegram = command[1]
            cursor.execute("DELETE FROM users WHERE id_telegram = %s", (id_telegram,))
            conn.commit()
             
            bot.reply_to(message, f"Đã xóa người dùng với ID: {id_telegram}")
        else:
            bot.reply_to(message, "Sử dụng lệnh /deleteacc <id_telegram>")
    except Exception as e:
        bot.reply_to(message, f"Có lỗi xảy ra: {e}")

@bot.message_handler(commands=['khuyenmai'])
def khuyenmai(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return

    try:
        command = message.text.split()
        if len(command) == 2 and command[1].isdigit():
            promotion_percentage = int(command[1])
            cursor.execute('UPDATE bonus SET khuyenmai = %s', (promotion_percentage,))
            conn.commit()
            bot.send_message(chat_id=user_id, text=f"Khuyến mãi nạp tiền đã được thiết lập thành {promotion_percentage}%")
        else:
            bot.send_message(chat_id=user_id, text="Sử dụng đúng định dạng: /khuyenmai [số%]")
    except Exception as e:
        bot.send_message(chat_id=user_id, text=f"Đã xảy ra lỗi: {str(e)}")

@bot.message_handler(commands=['resetbot'])
def restart(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    bot.send_message(chat_id=admin_id,text='Bot sẽ được khởi động lại trong giây lát...')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.message_handler(commands=['stopall'])
def stop(message):
    user_id = message.from_user.id
    if str(user_id) != admin_id:
        bot.send_message(chat_id=message.from_user.id,text='Bạn không có quyền sử dụng lệnh này.')
        return
    bot.send_message(chat_id=admin_id,text='đã dừng bot')
    bot.stop_polling()


bot.polling()