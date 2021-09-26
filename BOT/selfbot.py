from logging import exception, raiseExceptions
from os import getenv
import scraper
import json
import discord
import validators
import subprocess
from discord.ext import commands


class main(discord.Client):

    async def on_message(self, message):

        if message.author == self.user:
            return

        else:
            userText = message.content
            var1, var2 = userText.split(" ")
            if ((var1 == "!play") and (validators.url(var2) == True)):

                #if (validators.url(message.content) == True):
                    subprocess.run(["vlc", var2])
                    scraper.scrape()
            else:
                raiseExceptions()


client = commands.Bot(command_prefix="!")

client.load_extension("Cogs.maincog")

client.run("ODg5OTY5NDY0MDU2MTAyOTQy.YUzneQ.Jjp4D-SpgfGd9MYzfrOG1TfM2rk")