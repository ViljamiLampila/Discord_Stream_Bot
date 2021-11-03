# Discord_Stream_Bot
Experimental discord bot for streaming internet media.

Setup guide will be added at a later date.

## The way it works

#### discord.py-[self]

Discord.py-[self] allows you to use normal accounts as if they were bots.

validate youtube urls.

start vlc player wihtout interface and load inserted link.

responds to commands and relays information to Puppeteer.



#### Puppeteer

Puppeteer is used to manipulate the discord website since discord API does not allow for video streaming from code.

Joins the channel wich a video playback is requested from.


#### V4l2Loopback

create virtual video device and record vlc player.


#### Ffmpeg

realy the video device to discord.

