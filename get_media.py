from telethon import TelegramClient,events, sync
#import logging
import asyncio
api_id = 4397380
api_hash= "c714283ab4be5fccaa9e1db1956c904a"
phone = "+84838273502"
#logging.basicConfig(level=logging.DEBUG)

client = TelegramClient('+84838273502',
    api_id, api_hash,
    # You may want to use proxy to connect to Telegram
    #proxy=(socks.SOCKS5, 'PROXYHOST', PORT, 'PROXYUSERNAME', 'PROXYPASSWORD')
)
client.start()
def callback(current, total):
    print('Downloaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))
for message in client.iter_messages('son_dz2k_bot'):
    client.download_media(message,progress_callback=callback)