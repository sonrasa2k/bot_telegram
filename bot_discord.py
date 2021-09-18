import discord
from discord.ext import commands
import requests

client = discord.Client()
@client.event
async def on_ready():
    print("Bot is ready")
@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    data = {
        "sender": str(message.author),
        "message": str(message.content)
    }
    kq = requests.post('https://sonbot2021.herokuapp.com/webhooks/rest/webhook',json=data).json()
    print(kq)
    await message.channel.send(kq[0]["text"])
client.run('ODg4NzYwNDg3NjQxMjI3MjY0.YUXYtA.UDQhvE4SgWvQTc4WL9wC4gSv-Co')
