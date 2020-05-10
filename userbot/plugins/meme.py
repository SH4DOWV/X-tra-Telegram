"""
Memes Plugin for Userbot
usage = .meme someCharacter //default delay will be 3


"""
from telethon import events
import asyncio
import os
import sys
from userbot.events import register, errors_handler
from userbot import CMD_HELP


@borg.on(events.NewMessage(pattern=r"\.meme", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return   
    memeVar = event.text
    sleepValue = 3
    memeVar = memeVar[6:] 
           
    await event.edit("-------------"+memeVar)
    await event.edit("------------"+memeVar+"-")
    await event.edit("-----------"+memeVar+"--")
    await event.edit("----------"+memeVar+"---")
    await event.edit("---------"+memeVar+"----")    
    await event.edit("--------"+memeVar+"-----")
    await event.edit("-------"+memeVar+"------")
    await event.edit("------"+memeVar+"-------")
    await event.edit("-----"+memeVar+"--------")
    await event.edit("----"+memeVar+"---------")
    await event.edit("---"+memeVar+"----------")
    await event.edit("--"+memeVar+"-----------")
    await event.edit("-"+memeVar+"------------")
    await event.edit(memeVar+"-------------")
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)

"""
Bonus : Flower Boquee Generater
usage:- .flower

"""
@borg.on(events.NewMessage(pattern=r"\.flower", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return   
    flower =" 🌹"
    sleepValue = 5
           
    await event.edit(flower+"        ")
    await event.edit(flower+flower+"       ")
    await event.edit(flower+flower+flower+"      ")
    await event.edit(flower+flower+flower+flower+"     ")
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await asyncio.sleep(sleepValue)
        

   @borg.on(pattern=r"\.type")
@errors_handler
async def typewriter(typew):
    """ Just a small command to make your keyboard become a typewriter! """
    if not typew.text[0].isalpha() and typew.text[0] not in ("/", "#", "@",
                                                             "!"):
        textx = await typew.get_reply_message()
        message = typew.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await typew.edit("`Give a text to type!`")
            return
        sleep_time = 0.03
        typing_symbol = "|"
        old_text = ''
        await typew.edit(typing_symbol)
        await asyncio.sleep(sleep_time)
        for character in message:
            old_text = old_text + "" + character
            typing_text = old_text + "" + typing_symbol
            await typew.edit(typing_text)
            await asyncio.sleep(sleep_time)
            await typew.edit(old_text)
            await asyncio.sleep(sleep_time)

     
 
@borg.on(outgoing=True, pattern=r"\.bm")
@errors_handler
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    if not mock.text[0].isalpha() and mock.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await mock.get_reply_message()
        message = mock.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
            return

        for charac in message:
            if charac.isalpha() and random.randint(0, 1):
                to_app = charac.upper() if charac.islower() else charac.lower()
                reply_text.append(to_app)
            else:
                reply_text.append(charac)

        await mock.edit("".join(reply_text))




@borg.on(outgoing=True, pattern=r"\.vpr")
@errors_handler
async def vapor(vpr):
    """ Vaporize everything! """
    if not vpr.text[0].isalpha() and vpr.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await vpr.get_reply_message()
        message = vpr.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
            return

        for charac in message:
            if 0x21 <= ord(charac) <= 0x7F:
                reply_text.append(chr(ord(charac) + 0xFEE0))
            elif ord(charac) == 0x20:
                reply_text.append(chr(0x3000))
            else:
                reply_text.append(charac)

        await vpr.edit("".join(reply_text))
