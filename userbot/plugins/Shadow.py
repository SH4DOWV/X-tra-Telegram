import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot.utils import admin_cmd

@command(outgoing=True, pattern="^.shadowid$")
async def amireallyalive(shadow):
    """ For .alive command, check if the bot is running.  """
    await shadow.edit("**📖Ecco i miei ID**:\n\n"
                     "**📄Telegram:** @V_SHADOW_V\n\n"
                     "**Epic: V_SH4DOW_V**\n\n"
                     "**💣COD: Shadow#4654236**")
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     
