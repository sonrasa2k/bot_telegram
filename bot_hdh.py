import discord
from discord.ext import commands
client = commands.Bot( command_prefix="/")

with open("lenh.txt","r+",encoding="utf-8") as f:
    data = f.readlines()
list_lenh = []
list_chuc_nang = []
for i in data:
    list_lenh.append(i.split(':')[0])
    list_chuc_nang.append(i.split(':')[1])


@client.event
async def on_ready():
    print("Bot is ready")
@client.command()
async def l(ctx, *, lenh: str):
    print(lenh)
    if lenh in list_lenh:
        index = list_lenh.index(lenh)
        await ctx.send(lenh + ": "+list_chuc_nang[index])
    else:
        await ctx.send("Hệ thống không có hoặc chưa cập nhật lệnh này!")
client.run("ODg2ODgwMDQwMjU4NzgxMjA1.YT8BZw.QySP3KbwHTdIEAzKTH8sHmE3Fd8")