import requests
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import schedule
import asyncio

from discord import Intents
intents = Intents.default()
intents.members = True

intents = discord.Intents.default()
intents.all()

client = discord.Client(intents=intents)
channel_id = '1107062745095995402'
url_site = 'https://www.gameinformer.com'
#sites backup:
#https://www.rockpapershotgun.com
#https://www.ign.com
#https://www.gameinformer.com
client_token = 'MTEwNzAwNzk5MjM4NzM0MjQwNw.Gko-hD.33SFEsSXdt4QdFz58l2GXiK_lrShaIKZVLoMAs'
hora_os = '13:00'

latest_news = []

#webscrapping
def get_latest_news():

  response = requests.get(url_site)

  soup = BeautifulSoup(response.text, 'html.parser')
  latest_news = soup.find_all('div', class_='latest-news')
  return latest_news

#contact discord
@client.event
async def on_ready():
  print(f'{client.user} - ready!')

@client.event
async def on_message(message):

  if message.content == 'Piguinhas?':
    await message.channel.send(latest_news)

async def send_news():
  global latest_news
  new_news = get_latest_news()
  if new_news != latest_news:
    latest_news = new_news
    channel = client.get_channel(channel_id)
    for news in latest_news:
      await channel.send(news)

#trigger
schedule.every().day.at(hora_os).do(asyncio.run, send_news)

async def check_schedule():
  while True:
    schedule.run_pending()
    await asyncio.sleep(60) # verificar a programação a cada 60 segundos

async def start_bot():
  await client.start(client_token)

# start bot
async def main():
  await asyncio.gather(start_bot(), check_schedule())

asyncio.run(main())
