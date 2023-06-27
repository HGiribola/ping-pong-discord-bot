import discord
from discord.ext import commands

#BARD#
#from bardapi import Bard
#import os
#os.environ["_BARD_API_KEY"] = {
#    'Xwj2TA6QSk8csb0uecrbp2LKzTUa_mrW-KzWSieYVEo0Aze1lZDLRhO8-cjL8sOLu2cV1g.'
#}
#pergunta = input("")
#reposta bot:
#print(Bard.getanswer(str(message)))#

prefix = "/"
intent = discord.Intents.default()
bot = commands.Bot(command_prefix=prefix, intents=intent, help_command=None)

@bot.event
async def on_ready():
    print(f"{bot.user.name}: Loaded")

perguntas = {}
pergunta = input("")
perguntas.append(pergunta)
aux = len(perguntas)

while aux > 0:
    @bot.event
    async def on_message(message):
        print(f"Bot envia: {repr(message.content)}")
        await bot.process_commands(message)
        await message.channel.send("ping")
    aux - 1

bot.run("MTEwNzAwNzk5MjM4NzM0MjQwNw.GLP0aY.RUqpefuvyyHSZn_n1vCShfNYdJF6E6Rinhcuus")
