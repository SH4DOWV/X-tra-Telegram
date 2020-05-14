""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd("warn1"))
async def _(event):
    if event.fwd_from:
        return
    mentions = f"`📕Hai  1/3  warn.`\n**⚠️Attenzione!\n📝Motivo del warn:** `{}`".format(event.pattern_match.group(1))
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("warn2"))
async def _(event):
    if event.fwd_from:
        return
    mentions = f"`📕Hai 2/3  warn.`\n**⚠️ Attenzione!\n📝Motivo del warn:** `{}`".format(event.pattern_match.group(1))
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("warn3"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`📕Hai  3/3  warn.`\n**🚫Bannato!\n📝Motivo del ban:** `{}`".format(event.pattern_match.group(1))
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

""".admin Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("warn0"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`🗒️Warn resettati dall'Admin.`\n**📕Hai  0/3  warn.**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@borg.on(admin_cmd("ocb"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**⚠️Attenzione⚠️\n\n🔋Batteria sotto il 10%, Per Favore metti a ricaricare il tuo telefono 📲**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

@borg.on(admin_cmd("fw"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`🔈Sei stato mutato per Flood`\n**📝Motivo del mute: Mutato perché flood di cazzate⚠️**"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
