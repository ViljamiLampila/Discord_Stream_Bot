import discord
from discord.ext import commands

async def on_guild_emojis_update(self, guild:discord.Guild, before, after):
@commands.command()
async def hello(ctx):
    await ctx.send('Hello {0.display_name}.'.format(ctx.author))


def setup(bot):
    bot.add_command(hello)
