import discord
from discord.ext import commands
import requests

client = discord.Client()
async def on_message(message):
    if message.author == client.user:
        return
    data = {
        "sender": str(message.author),
        "message": str(message.content)
    }
    kq = requests.post('https://sonbot2021.herokuapp.com/webhooks/rest/webhook',json=data).json()
    await message.channel.send(kq[0]["text"])
if __name__ == '__main__':
    client.run('ODg3MDEyMDMwMTIzNDkxMzc4.YT98Uw.36AOKT-8zehTUBL10YOz8NhY2ZM')
