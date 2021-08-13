import os
import discord
from discord.ext import commands
from decouple import config
from discord_components import DiscordComponents

intents = discord.Intents.default()
intents.members = True
intents.presences = True

#kana variables
kana_id = 857835279259664403
client = commands.Bot(command_prefix=commands.when_mentioned_or('kanna ', 'kana ', 'k.', 'K.', 'Kanna ', 'Kana '), case_insensitive=True, intents=intents)
client.remove_command("help")

print(">> Kanna is awaking...")

def load_cogs():
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.load_extension(f"cogs.{file[:-3]}")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='Asheeshh Onii Chan'))
  load_cogs()
  DiscordComponents(client)
  print(">> Cogs loaded.")
  print(f">> Logged in as : {client.user.name} \n>> ID : {client.user.id}")
  print(f">> Total Servers : {len(client.guilds)}\n")
  print('>> Kanna is Online.')

@client.command()
@commands.is_owner()
async def reload(ctx):
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.reload_extension(f"cogs.{file[:-3]}")
  await ctx.send("```>> Kanna reloaded cogs```")

token = config("TOKEN")
client.run(token)

