
# bot.py
import os
import discord
from discord.ext import commands
import json


# Get configuration.json
with open("config.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]


class Greetings(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self._last_member = None

# Intents
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(prefix, intents = intents)


# Load cogs
initial_extensions = [
    "Cogs.help",
    "Cogs.ping",
    "Cogs.maincog",
    "Cogs.hello"
]

print(initial_extensions)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)           
        except Exception as e:
            print(f"Failed to load extension {extension}")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))
    print(discord.__version__)
    

    

bot.run(token)


