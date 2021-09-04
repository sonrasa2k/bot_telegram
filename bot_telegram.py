from telegram.ext import Updater,CommandHandler
from data_covic import DataCovicVn
updater = Updater(token='1983778167:AAE37mC4rhCdZz0rOvf0U6rrI0lGCbuZuSU', use_context=True) #Token của bot bạn
dispatcher = updater.dispatcher

def hello(update,context):
    name = update.message.from_user.first_name #lấy tên của người gửi tin nhắn tới bot
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Chào {0} Mình là Bot Của Anh Son 2k!".format(name))
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Hãy nhập /covic để biết thông tin về covic tại Việt Nam!")
    context.bot.send_message(chat_id=update.message.chat_id,text="Tôi có thể giúp gì cho bạn!")
    return True

def covic(update,context):
    covicvn = DataCovicVn()
    data = covicvn.get_data_covic_vn()
    if data["code"] == 402:
        context.bot.send_message(chat_id=update.message.chat_id, text="Hệ thống đang bị lỗi! Bạn vui lòng thử lại" )
        return False

    text_send = "Thông tin Covic tại Việt Nam:\n" \
                "Số Ca Nhiễm: {0}\n" \
                "Đang Điều Trị: {1}\n" \
                "Khỏi: {2}\n" \
                "Tử Vong: {3}\n".format(data["so_ca_nhiem"],data["dang_dieu_tri"],data["khoi"],data["tu_vong"])
    context.bot.send_message(chat_id=update.message.chat_id,text = text_send)
    return True
hello_hand = CommandHandler('start', hello) #Hàm cấu hình lệnh từ người dùng, ở đây là lệnh start thực hiện hàm hello
dispatcher.add_handler(hello_hand)

covic_hand = CommandHandler("covic",covic)
dispatcher.add_handler(covic_hand)
updater.start_polling()


