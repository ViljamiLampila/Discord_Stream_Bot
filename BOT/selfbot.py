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
            nodePuppet() #runs BrowserPuppet.js
            subprocess.Popen(["ffmpeg", "-f", "x11grab", "-r", "24", "-s", "1920x1080", "-i", ":0.0+0", "-vcodec", "rawvideo", "-pix_fmt", "yuv420p", "-threads", "0", "-f", "v4l2", "/dev/video0"]) #runs virtual camera feed
            #one for audio too would be nice
            if ((var1 == "!play") and (validators.url(var2) == True)):

                   
                sp = subprocess.Popen(["vlc", var2])               
                poll = sp.poll()
                #if poll returns none vlc is active then add selected song to que
                if poll is None:
                    subprocess.Popen(["vlc -f --started-from-file --playlist-enqueue", var2])
                #if not active start subprocess and check for errors
                else:                            
                    raiseExceptions()


#client = commands.Bot(command_prefix="!")

client = main()

client.run("token here ")