from telegram.ext import Updater,CommandHandler
updater = Updater(token='1983778167:AAE37mC4rhCdZz0rOvf0U6rrI0lGCbuZuSU', use_context=True) #Token của bot bạn
dispatcher = updater.dispatcher

def hello(update,context):
    name = update.message.from_user.first_name #lấy tên của người gửi tin nhắn tới bot
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Chào {0} Mình là Bot Của Anh Son 2k!".format(name))
    context.bot.send_message(chat_id=update.message.chat_id,text="Tôi có thể giúp gì cho bạn!")
    return True
hello_hand = CommandHandler('start', hello) #Hàm cấu hình lệnh từ người dùng, ở đây là lệnh start thực hiện hàm hello
dispatcher.add_handler(hello_hand)
updater.start_polling()


