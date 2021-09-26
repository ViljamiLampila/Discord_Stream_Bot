from os import getenv
import json
import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!")

client.load_extension("Cogs.maincog")

client.run("ODg5OTY5NDY0MDU2MTAyOTQy.YUzneQ.Jjp4D-SpgfGd9MYzfrOG1TfM2rk")