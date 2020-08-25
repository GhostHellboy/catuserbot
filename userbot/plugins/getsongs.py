"""
credits to @mrconfused and @sandy1709
"""
#    Copyright (C) 2020  sandeep.n(π.$)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
from telethon import events
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
from userbot.utils import admin_cmd , sudo_cmd
import glob
import os  
from userbot import CMD_HELP, ALIVE_NAME
from userbot.plugins import catmusic , catmusicvideo
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
import pybase64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
USERNAME = str(Config.LIVE_USERNAME) if Config.LIVE_USERNAME else "@Jisan7509"

@borg.on(admin_cmd(pattern="song(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8..! I am finding your song....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your song....")
    else:
    	await event.edit("`What I am Supposed to find `")
    	return
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await event.client(cat)
    except:
        pass
    await catmusic(str(query),"128k")
    l = glob.glob("./temp/*.mp3")
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
        return
    thumbcat = glob.glob("./temp/*.jpg") + glob.glob("./temp/*.webp") 
    if thumbcat:
        catthumb = thumbcat[0]
    else:
        catthumb = None
    loa = l[0]
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=False,
                allow_cache=False,
                caption=f"➥ __**Song :- {query}**__\n__**➥ Uploaded by :-**__ [{DEFAULTUSER}]({USERNAME})",
                thumb = catthumb,
                supports_streaming=True,
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf ./temp/*.mp3") 
    os.system("rm -rf ./temp/*.jpg")
    os.system("rm -rf ./temp/*.webp")
    
@borg.on(admin_cmd(pattern="song320(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8..! I am finding your song....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your song....")
    else:
    	await event.edit("`What I am Supposed to find `")
    	return
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await event.client(cat)
    except:
        pass
    await catmusic(str(query),"320k")
    l = glob.glob("./temp/*.mp3")
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
        return
    thumbcat = glob.glob("./temp/*.jpg") + glob.glob("./temp/*.webp")
    if thumbcat:
        catthumb = thumbcat[0]
    else:
        catthumb = None
    loa = l[0]
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=False,
                allow_cache=False,
                caption=f"➥ __**Song :- {query}**__\n__**➥ Uploaded by :-**__ [{DEFAULTUSER}]({USERNAME})",
                thumb = catthumb,
                supports_streaming=True,
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf ./temp/*.mp3") 
    os.system("rm -rf ./temp/*.jpg")
    os.system("rm -rf ./temp/*.webp")
    
@borg.on(admin_cmd(pattern="vsong(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("wi8..! I am finding your videosong....")
    elif reply.message:
        query = reply.message
        await event.edit("wi8..! I am finding your videosong....")
    else:
        await event.edit("What I am Supposed to find")
        return
    await catmusicvideo(query)
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await event.client(cat)
    except:
        pass
    l = glob.glob(("./temp/*.mp4")) 
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
        return
    thumbcat = glob.glob("./temp/*.jpg") + glob.glob("./temp/*.webp")
    if thumbcat:
        catthumb = thumbcat[0]
    else:
        catthumb = None
    loa = l[0]  
    metadata = extractMetadata(createParser(loa))
    duration = 0
    width = 0
    height = 0
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("width"):
        width = metadata.get("width")
    if metadata.has("height"):
        height = metadata.get("height")
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=False,
                allow_cache=False,
                thumb = catthumb,
                caption=f"➥ __**Song :- {query}**__\n__**➥ Uploaded by :-**__ [{DEFAULTUSER}]({USERNAME})",
                supports_streaming=True,
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf ./temp/*.mp4") 
    os.system("rm -rf ./temp/*.jpg")
    os.system("rm -rf ./temp/*.webp")
    
@borg.on(sudo_cmd(pattern="song(?: |$)(.*)", allow_sudo = True))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        san = await event.reply("wi8..! I am finding your song....`")
    elif reply.message:
        query = reply.message
        san = await event.reply("wi8..! I am finding your song....`")
    else:
    	san = await event.reply("`What I am Supposed to find `")
    	return
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await event.client(cat)
    except:
        pass
    await catmusic(str(query),"320k")
    l = glob.glob("./temp/*.mp3")
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
        return
    thumbcat = glob.glob("./temp/*.jpg") +  glob.glob("./temp/*.webp")
    if thumbcat:
        catthumb = thumbcat[0]
    else:
        catthumb = None
    loa = l[0]
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=False,
                allow_cache=False,
                caption=f"➥ __**Song :- {query}**__\n__**➥ Uploaded by :-**__ [{DEFAULTUSER}]({USERNAME})",
                thumb = catthumb,
                supports_streaming=True,
                reply_to=reply_to_id
            )
    await san.delete()
    os.system("rm -rf ./temp/*.mp3") 
    os.system("rm -rf ./temp/*.jpg")
    os.system("rm -rf ./temp/*.webp")
  

@borg.on(sudo_cmd(pattern="vsong(?: |$)(.*)", allow_sudo = True))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        san = await event.reply("wi8..! I am finding your videosong....`")
    elif reply.message:
        query = reply.message
        san = await event.reply("wi8..! I am finding your videosong....`")
    else:
    	san = await event.reply("`What I am Supposed to find `")
    	return
    await catmusicvideo(query)
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await event.client(cat)
    except:
        pass
    l = glob.glob(("./temp/*.mp4")) 
    if l:
        await event.edit("yeah..! i found something wi8..🥰")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
        return
    thumbcat = glob.glob("./temp/*.jpg") + glob.glob("./temp/*.webp")
    if thumbcat:
        catthumb = thumbcat[0]
    else:
        catthumb = None
    loa = l[0]  
    metadata = extractMetadata(createParser(loa))
    duration = 0
    width = 0
    height = 0
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("width"):
        width = metadata.get("width")
    if metadata.has("height"):
        height = metadata.get("height")
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=False,
                allow_cache=False,
                thumb = catthumb,
                caption=f"➥ __**Song :- {query}**__\n__**➥ Uploaded by :-**__ [{DEFAULTUSER}]({USERNAME})",
                supports_streaming=True,
                reply_to=reply_to_id
            )
    await san.delete()
    os.system("rm -rf ./temp/*.mp4") 
    os.system("rm -rf ./temp/*.jpg")
    os.system("rm -rf ./temp/*.webp")

CMD_HELP.update({"getmusic":
    "`.song` query or `.song` reply to song name :\
    \nUSAGE:finds the song you entered in query and sends it"
    "`.vsong` query or `.vsong` reply to song name :\
    \nUSAGE:finds the video song you entered in query and sends it"
})
