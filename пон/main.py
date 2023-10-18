import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(f"./{attachment.filename}"))
    else:
        await ctx.send("Вы забыли загрузить картинку :(")


bot.run("MTE2MDQ4MjExMTMyNTc0NTIwMg.G8XvkM.4dl2Co6dQwrjuTiJzTswAlVhswnt5rSbPBHvJM")