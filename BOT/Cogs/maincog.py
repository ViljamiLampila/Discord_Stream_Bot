import discord
import random
import validators
import subprocess
from discord import client
from discord import message
from discord.ext import commands



class test(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.bot = client

    @commands.command(name = "anal")
    async def play(self, ctx):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

#    @commands.command(name = (if validators.url(message.content) == True))
#    async def on_message(self, message):
#            
#
           # don't respond to ourselves
#           if message.author == self.user:
#               return
#
#            else:
#            
#               await message.send('coom')

           #if message.content == 'ping':
           #     await message.channel.send('pong')


#if(validators.url(urlvalue) == True){
 #   subprocess.run(["vlc", urlvalue])
#}
 

def setup(client: commands.Bot):
    client.add_cog(test(client))