# Lots of lub to @r4v4n4 for gibing the base <3
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd,register

@borg.on(admin_cmd("scan ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Rispondi a qualunque messaggio.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```rispondi ad un messaggio contenente media```")
       return
    chat = "@DrWebBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Rispondi a messaggi di persone attuali.```")
       return
    await event.edit(" `Facendomi scivolare la punta delle dita sopra`")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Per favore, sblocca @sangmatainfo_bot.```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```Per favore, puoi disattivare la privacy di inoltro, per piacere?```")
          else:
          	if response.text.startswith("Select"):
          		await event.edit("`Per favore, vai da @DrWebBot e seleziona un linguaggio.`") 
          	else: 
          			await event.edit(f"**Scansione AntiVirus completata. Ho i risultati finali.**\n {response.message.message}")
