# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Cmd= `.zombie`
Usage: Searches for deleted accounts in a groups and channels.
Use .zombies clean to remove deleted accounts from the groups and channels.
\nPorted by ©[NIKITA](t.me/kirito6969) and ©[EYEPATCH](t.me/NeoMatrix90)"""

from telethon import events
from userbot.utils import admin_cmd
#
from asyncio import sleep
from os import remove

from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.types import (ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto)


# =================== CONSTANT ===================

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================



@borg.on(admin_cmd(pattern=f"zombies", allow_sudo=True))
@borg.on(events.NewMessage(pattern="^.zombies(?: |$)(.*)", outgoing=True))
async def rm_deletedacc(show):
    """ For .zombies command, list all the ghost/deleted/zombie accounts in a chat. """

    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "Nessun account eliminato, trovato qui."

    if con != "clean":
        await show.edit("Cercando fanntasmi/account eliminati...")
        async for user in show.client.iter_participants(show.chat_id):

            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = f"Trovato/i **{del_u}** account eliminato/i in questo gruppo,\
            \nRipulisci usando .zombies clean`"
        await show.edit(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit("Non sono admin qui!")
        return

    await show.edit("Rimuovendo gli account eliminati...\nOh, posso farlo?!?!")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.edit("Non ho i permessi di bannare qui!")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1


    if del_u > 0:
        del_status = f"Ripulito/i da **{del_u}** account eliminati."

    if del_a > 0:
        del_status = f"Ripulito/i da **{del_u}** account eliminati \
        \n**{del_a}** account Admin eliminati non rimossi."


    await show.edit(del_status)
    await sleep(2)
    await show.delete()


    if Config.G_BAN_LOGGER_GROUP is not None:
        await show.client.send_message(
            Config.G_BAN_LOGGER_GROUP, "#CLEANUP\n"
            f"Ripulito/i da  **{del_u}** account eliminati !!\
            \nCHAT: {show.chat.title}(`{show.chat_id}`)")

