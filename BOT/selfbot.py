from logging import exception, raiseExceptions
from subprocess import Popen
import discord
import validators
import subprocess
from discord.ext import commands

def nodePuppet():
    subprocess.Popen(["node", "./BOT/BrowserPuppet.js"])

class main(discord.Client):

    async def on_message(self, message):
        if message.author == self.user:
            return


        if "!play" in message.content:
            userText = message.content
            var1, var2 = userText.split(" ") #checking if the url provided is valid
            nodePuppet()
            if ((var1 == "!play") and (validators.url(var2) == True)):

                   
                sp = subprocess.Popen(["vlc", var2])               
                poll = sp.poll()
                #if poll returns none vlc is active then add selected song to que
                if poll is None:
                    subprocess.Popen(["vlc --started-from-file --playlist-enqueue", var2])
                #if not active start subprocess and check for errors
                else:                            
                    raiseExceptions()


#client = commands.Bot(command_prefix="!")

client = main()

client.run("token here")