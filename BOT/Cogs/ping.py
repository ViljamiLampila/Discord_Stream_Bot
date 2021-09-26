import discord
from discord.ext import commands
from discord.ext.commands import Bot

class penisCrabs(discord.client):

    async def on_message(self, message):

           # don't respond to ourselves
           if message.author == self.user:
               return

           if message.content == 'ping':
                await message.channel.send('pong')

