import os
import json
import discord
from discord.ext import commands



with open("config.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('logged on as ', self.user)

    async def on_message(self, message):

        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        

    

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
 


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)           
        except Exception as e:
            print(f"Failed to load extension {extension}")

print(initial_extensions)

client = MyClient()
client.run(token)