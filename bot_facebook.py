#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
from tiktok import Download
from random import randrange
from sendVideo import sendVideo
guivideo = sendVideo()
tiktoks = Download()
app = Flask(__name__)
ACCESS_TOKEN = 'EAADCmt8dSl0BAD6cl1ckus2UZBJwh4vMYlUXOc4ZAeEL2RvsMpwrUbhlfCg2LHbeZAsUnabZAmfajMZAIaOGDUeYaaxtH6QEVYDKMQ9DczcguafOGj5Gb1TvZB9dBhCt8QqwxS7R5roZBGP7LXCp7qf9EUJbRUts9pjXZBUsT5RISeleYZC2nFju4W2zUksfOa9Eg2FADAJlN4QZDZD'
VERIFY_TOKEN = 'hongtin123456@@@'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                print(message)
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                print(recipient_id)
                if message['message'].get('text'):
                    text = message['message'].get('text')
                    if "tiktok" in text:
                        text_return = get_message(text,recipient_id)
                        send_message(recipient_id,text_return)
                    elif "play" in text:
                        link_video = get_link_video(text, recipient_id)
                        print(bot.send_video_url(recipient_id,"http://son.codes/wp-content/uploads/2021/08/son.mp4"))
                        send_message(recipient_id,"video cua ban")
                    else:
                        text_return = get_message(text, recipient_id)
                        send_message(recipient_id, text_return)
                    # else:
                    #     link_video = get_link_video(text,recipient_id)
                    #     guivideo.gui_video(link_video,recipient_id)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    text = "None"
                    response_sent_nontext = get_message(text,recipient_id)
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def get_link_video(text,recipient_id):
    if "play " in text:
        with open(str(recipient_id)+".txt","r") as f:
            data = f.readlines()
        f.close()
        stt = -2
        text = text.split('play ')[1]
        if text == "r":
            stt = randrange(0,len(data))
        try:
            if stt == -2:
                stt = int(text)
        except:
            text_return = "Bạn nhập sai số thứ tự của video tiktok hoặc chưa có danh sách video tiktok\n"
            "Hãy nhập danh sách video tiktok bằng cách nhâp: /tiktok username <username bạn yêu thích>\n"
            "Ví dụ: /tiktok username h2son"
            return text_return
        if len(data) == 0 or stt >= len(data):
            text = "Bạn đã nhập sai số thứ tự của video ! Hãy nhập /list để kiểm tra lại!"
            return text
        else:
            text_return = str(tiktoks.downloadVideoNoWatermarkByID(data[stt].strip(), "son"))
            return text_return
#chooses a random message to send to the user
def get_message(text,recipient_id):
    if "tiktok " in text:
        username = text.split('tiktok ')[1]
        try:
            list_id = tiktoks.get_all_id_video__of_user(username)
        except:
            text_return = "Username bạn nhập sai hoặc người dùng không có Video Nào!"
            return text_return
        if len(list_id) == 0:
            text_return = "Username bạn nhập sai hoặc người dùng không có Video Nào!"
            return text_return
        else:
            with open(str(recipient_id) + ".txt", "w") as f:
                text_return = "Danh Sách Các ID Video Của " + text + ":\n" + "STT | ID VIDEO:\n "
                for i in range(0, len(list_id)):
                    f.writelines(list_id[i] + "\n")
                    text_return = text_return + str(i) + " | " + str(list_id[i]) + "\n"
                f.close()
                return text_return

    # return selected item to the user
    return "Chào bạn bạn muốn mình làm gì cho bạn ?"

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()