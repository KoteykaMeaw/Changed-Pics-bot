import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    attachments = ctx.message.attachments
    for attachment in attachments:
        file_name = attachment.filename
        file_url = attachment.url
        await attachment.save(f'./images/{file_name}')
        await ctx.send('Картинка сохранена')

bot.run("MTE2MDQ4MjExMTMyNTc0NTIwMg.G8XvkM.4dl2Co6dQwrjuTiJzTswAlVhswnt5rSbPBHvJM")