from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from get_covic import Covic
import requests
from tiktok import Download
from random import randrange
from get_coin import Get_Coin
from sogiday import SoGiDay
from datetime import datetime
tiktoks = Download()
covic = Covic()
coin = Get_Coin()
so = SoGiDay()
updater = Updater(token='1947192196:AAFEPEaVg9RnJP0ELjbTZUujN3rGkYUHLQA', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher
def help(update,context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id,text="Chào {0} Mình là Bot Của Anh Son 2k!. Mình Có Các Chức Năng :".format(name))
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Để xem thông tin covic tại việc nam bạn hãy nhập: /covicvn\n"
                                  "Để xem thông tin về các ca nhiễm covic tại việc nam bạn hãy nhập: /covic_new\n"
                                  "Để xem thông tin Covic tất cả tỉnh thành có covic hãy nhập: /covic all \n"
                                  "Để xem thông tin Covic từng tỉnh thành hãy nhập: /covic tên tỉnh thành viết thường có dấu\n"
                                  "Để nghe và tải nhạc hãy nhập : /p tên bài hát\n"
                                  "Để lấy danh sách video của 1 user tiktok bạn hãy nhập: /titok usernaname <tên username>\n. VD: /tiktok username h2son\n"
                                  "Để phát 1 video từ danh sách video hãy nhập /v <số thứ tự trong list video tiktok>. Ví dụ: /v 1")
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="")
def hello(update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text='Chao {0} Nhe ! Minh La Bot Cua Anh Son Dep Trai'.format(name))
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Để xem thông tin về chức năng của bot hãy nhập /help")

def tin_ca_nhiem_moi(update,context):
    data = covic.covic_tinnhanh()
    if data['code'] == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hệ thống đang bị lỗi rồi bạn yêu ♥")
    else:
        text = data['content']
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)



def play_music(update, context):
    name = update.message.from_user.id
    text = update.message.text
    if '/p' in text:
        text = text.split('/p ')[1]
        api_zing = "http://ac.mp3.zing.vn/complete?type=artist,song,key,code&num=15&query={0}".format(text)
        data = requests.get(api_zing).json()
        list_data = data["data"][0]['song']
        link_api_music = "http://api.mp3.zing.vn/api/streaming/audio/"
        list_link_music = []
        for data in list_data:
            list_link_music.append(link_api_music + str(data['id']) + '/320')
        text = ""
        for i in range(1, len(list_link_music) + 1):
            text = text + str(i) + ". " + list_link_music[i - 1] + "\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    elif '/covic' in text:
        text = text.split('/covic ')[1]
        if "all" in text:
            data = covic.covic_diaphuong("all")
            if data['code'] == 0:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Hệ thống đang bị lỗi rồi bạn yêu ♥")
            elif data['code'] == 99:
                text = "Tên Tỉnh |Tổng |Hôm Nay | CHẾT\n"
                for i in range(0, len(data['name_tinh'])):
                    text = text + "{0} | {1} | {2} | {3}\n".format(data['name_tinh'][i], data['scn'][i],
                                                                   data['scnhn'][i], data['chet'][i])
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        else:
            print(text)
            data = covic.covic_diaphuong(text)
            print(data)
            if data['code'] == 0:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Hệ thống đang bị lỗi rồi bạn yêu ♥")
            elif data['code'] == 200:
                text = "Thông tinh về Covic Tại {0}:\nTổng Số Ca Nhiễm: {1}\nSố Ca Nhiễm Hôm Nay: {2}\nSố Người Chết: {3}".format(
                    data['name_tinh'], data['scn'], data['scnhn'], data['chet'])
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Tên tĩnh sai rồi bạn yêu ♥")
    elif "/tiktok username" in text:
        text = text.split('/tiktok username ')[1]
        list_id,list_caption,list_nick,list_play = tiktoks.get_all_id_video__of_user(text)
        if len(list_id) == 0:
            text_return = "Username bạn nhập sai hoặc người dùng không có Video Nào!"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
        else:
            with open(str(name) + ".txt", "w",encoding="utf-8") as f:
                text_return = "Danh Sách Các ID Video Của " + text + ":\n"+"STT | Caption:\n "
                for i in range(0, len(list_id)):
                    f.writelines(str(list_id[i])+"||"+str(list_caption[i])+"||"+str(list_nick[i])+"||"+str(list_play[i])+"\n")
                    text_return = text_return + str(i) + " | " + str(list_caption[i]) + "\n"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
                f.close()
    elif "/v " in text:
        with open(str(name)+".txt","r",encoding="utf-8") as f:
            data = f.readlines()
        f.close()
        stt = -2
        text = text.split('/v ')[1]
        if text == "r":
            stt = randrange(0,len(data))
        try:
            if stt == -2:
                stt = int(text)
        except:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Bạn nhập sai số thứ tự của video tiktok hoặc chưa có danh sách video tiktok\n"
                                                                            "Hãy nhập danh sách video tiktok bằng cách nhâp: /tiktok username <username bạn yêu thích>\n"
                                                                            "Ví dụ: /tiktok username h2son")
        if len(data) == 0 or stt >= len(data):
            context.bot.send_message(chat_id=update.effective_chat.id,text="Bạn đã nhập sai số thứ tự của video ! Hãy nhập /list để kiểm tra lại!")
        else:
            # text_return = "Video của bạn: \n"
            # text_return = text_return + str(tiktoks.downloadVideoNoWatermarkByID(data[stt].strip(),"son"))
            # context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
            url_video = tiktoks.downloadVideoNoWatermarkByID(data[stt].strip().split('||')[0],"son2")
            print(url_video)
            caption = "Video ID: {0}\n Caption: {1}\n Lượt view: {2}\n Tác giả: {3}\n".format(
                data[stt].strip().split('||')[0],data[stt].strip().split('||')[1],data[stt].strip().split('||')[3],data[stt].strip().split('||')[2]
            )
            context.bot.sendVideo(chat_id=update.effective_chat.id,video=url_video,caption=caption)
    elif "/lấy" in text and "video" in text:
        text = text.split('/lấy ')[1].split(' video')[0]
        try:
            so_video = int(text)
            if so_video > 28:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Bạn đã nhập sai số video cần lấy từ list! Hãy nhập /list để kiểm tra lại!")
                return False
        except:
            context.bot.send_message(chat_id=update.effective_chat.id,text = "Bạn nhập cú pháp không chính xác! Cú Pháp : Lấy X video. VD: lấy 5 video\n")
            return False
        with open(str(name)+".txt","r",encoding="utf-8") as f:
            data = f.readlines()
        for i in range(0,so_video):
            url_video = tiktoks.downloadVideoNoWatermarkByID(data[i].strip().split('||')[0], "son2")
            caption = "Video ID: {0}\n Caption: {1}\n Lượt view: {2}\n Tác giả: {3}\n".format(
                data[i].strip().split('||')[0], data[i].strip().split('||')[1], data[i].strip().split('||')[3],
                data[i].strip().split('||')[2]
            )
            context.bot.sendVideo(chat_id=update.effective_chat.id, video=url_video, caption=caption)

    elif "/coin" in text:
        text = text.split('/coin ')[1]
        if text == "all":
            text_return = coin.get_all()
            context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
        else:
            text_return = coin.get_by_name(text)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
    elif text == "/tiktok trend" or text == "/Tiktok trend":
        try:
            list_id, list_caption, list_nick, list_play = tiktoks.get_all_id_video_from_trending()
        except:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Có Lỗi Khi Get Data . Sorry!")
        with open(str(name) + ".txt", "w", encoding="utf-8") as f:
            text_return = "Danh Sách Các ID Trên TikTok Trending"+":\n" + "STT | Caption:\n "
            for i in range(0, int(len(list_id)/2)):
                f.writelines(str(list_id[i]) + "||" + str(list_caption[i]) + "||" + str(list_nick[i]) + "||" + str(
                    list_play[i]) + "\n")
                text_return = text_return + str(i) + " | " + str(list_caption[i]) + "\n"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
            text_return = ""
            for i in range(int(len(list_id)/2),len(list_id)):
                text_return = text_return + str(i) + " | " + str(list_caption[i]) + "\n"
                f.writelines(str(list_id[i]) + "||" + str(list_caption[i]) + "||" + str(list_nick[i]) + "||" + str(
                    list_play[i]) + "\n")
            context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
            f.close()
        # try:
        #     list_id = tiktoks.get_all_id_video__of_user(text)
        #     if len(list_id) == 0:
        #         text_return = "Username bạn nhập sai hoặc người dùng không có Video Nào!"
        #         context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
        #     else:
        #         with open(name+".txt","a+") as f:
        #             text_return = "Danh Sách Các ID Video Của " + text +":\n"
        #             for i in range(0,len(list_id)):
        #                 f.write(list_id[i])
        #                 text_return = text_return + str(i) + ". "+ str(list_id[i])+"\n"
        #             context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
        #             f.close()
        # except:
        #     text_return = "Loi He Thong!"
        #     context.bot.send_message(chat_id=update.effective_chat.id, text=text_return)
    elif text == "/so":
        so1 = randrange(0,10)
        so = randrange(10000,99999)
        so_result = str(so1)+str(so)
        context.bot.send_message(chat_id=update.effective_chat.id,text = "Số May Mắn Của Bạn Hôm Nay LÀ : ")
        context.bot.send_message(chat_id=update.effective_chat.id, text=so_result)

def so_gi_day(bot,update,job_queue):
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id,text="Bạn đã đăng ký nhận thông báo số gì đây Shopee thành công!")
    t = datetime.time(8,57,00,000000)
    job_queue.run_daily(send_sogiday(chatid=chat_id,gio=9),t,context=update)

def send_sogiday(bot,job,chatid,gio):
    bot.send_message(chat_id=chatid, text = "Số gì đây : "+so.ket_qua_hientai(gio))

def summary(update, context):
    datavn = covic.covic_vn()
    if datavn['code']  == 0:
        context.bot.send_message(chat_id=update.effective_chat.id,text="Hệ thống đang bị lỗi rồi bạn yêu ♥")
    else:
        text = "THÔNG TIN COVIC TẠI VIỆT NAM :\n" \
               "Số ca nhiễm: {0}\n" \
               "Số ca đang điều trị: {1}\n" \
               "Số ca đã khỏi bệnh: {2}\n" \
               "Số người chết: {3}\n".format(datavn['scn'],datavn['scdt'],datavn['khoi'],datavn['chet'])
        context.bot.send_message(chat_id=update.effective_chat.id,text=text)
corona_summary_handler = CommandHandler('covicvn', summary)
dispatcher.add_handler(corona_summary_handler)
help_r = CommandHandler('help',help)
dispatcher.add_handler(help_r)
tin_nhanh = CommandHandler('covic_new',tin_ca_nhiem_moi)
dispatcher.add_handler(tin_nhanh)
updater.dispatcher.add_handler(CommandHandler('sogiday', so_gi_day,pass_job_queue=True))
start = tin_nhanh = CommandHandler('start',help)
dispatcher.add_handler(start)
# hello_handler = MessageHandler(Filters.text, hello)
# dispatcher.add_handler(hello_handler)
play_handler = MessageHandler(Filters.text, play_music)
dispatcher.add_handler(play_handler)

updater.start_polling()