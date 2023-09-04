import discord
from discord.ext import commands

prefix = "/"
intent = discord.Intents.default()
bot = commands.Bot(command_prefix=prefix, intents=intent, help_command=None)


@bot.event
async def on_ready():
    print(f"{bot.user.name}: Loaded")


@bot.event
async def bard(message):

    if message.author == bot.user:
        return

    await bot.process_commands(message)
    await message.channel.send("ping")

bot.run('MTEwNzAwNzk5MjM4NzM0MjQwNw.GHoia9.AABBgyD9zYkZQ2sFv_2EqECz31CFFUIjzGD8Sk')
