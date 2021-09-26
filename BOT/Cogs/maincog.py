import discord
import random
from discord import client
from discord.ext import commands



class test(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.bot = client

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    async def on_ready(self):
        print('Logged on as', self.user)



def setup(client: commands.Bot):
    client.add_cog(test(client))