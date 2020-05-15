""" Google Translate
Available Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate
.tts LanguageCode as reply to a message
.tts LanguageCode | text to speak"""

import emoji
import asyncio
import os
import subprocess
from gtts import gTTS
from datetime import datetime
from googletrans import Translator
from userbot.utils import admin_cmd


@borg.on(admin_cmd("tr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**Tradotto** da {} a {}
{}""".format(
            translated.src,
            lan,
            after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))


@borg.on(admin_cmd("tts (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("Invalid Syntax. Module stopping.")
        return
    text = text.strip()
    lan = lan.strip()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    required_file_name = Config.TMP_DOWNLOAD_DIRECTORY + "voice.ogg"
    try:
        #https://github.com/SpEcHiDe/UniBorg/commit/17f8682d5d2df7f3921f50271b5b6722c80f4106
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
             required_file_name,
             "-map",
             "0:a",
             "-codec:a",
             "libopus",
             "-b:a",
             "100k",
             "-vbr",
             "on",
             required_file_name + ".opus"
        ]
        try:
            t_response = subprocess.check_output(command_to_execute, stderr=subprocess.STDOUT)
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await event.edit(str(exc))
            # continue sending required_file_name
        else:
            os.remove(required_file_name)
            required_file_name = required_file_name + ".opus"
        end = datetime.now()
        ms = (end - start).seconds
        await borg.send_file(
            event.chat_id,
            required_file_name,
            # caption="**Completato {} ({}) in {} seconds!**".format(text[0:97], lan, ms),
            reply_to=event.message.reply_to_msg_id,
            allow_cache=False,
            voice_note=True
        )
        os.remove(required_file_name)
        await event.edit("**Completato {} ({}) in {} seconds!**".format(text[0:97], lan, ms))
        await asyncio.sleep(5)
        await event.delete()
    except Exception as e:
        await event.edit(str(e))

