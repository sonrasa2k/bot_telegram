from telegram.ext import Updater, CommandHandler,CallbackContext
import datetime
def callback_alarm(context: CallbackContext):
    print(id)
    context.bot.send_message(chat_id=id, text='Hi, This is a daily reminder')

def reminder(update,context):
   context.bot.send_message(chat_id = update.effective_chat.id , text='Daily reminder has been set! You\'ll get notified at 8 AM daily')
   context.job_queue.run_daily(callback_alarm, context=update.message.chat_id,days=(0, 1, 2, 3, 4, 5, 6),time = datetime.time(hour = 11, minute = 5, second = 10))

updater = Updater('1947192196:AAFEPEaVg9RnJP0ELjbTZUujN3rGkYUHLQA')
updater.dispatcher.add_handler(CommandHandler('notify', reminder))
updater.start_polling()