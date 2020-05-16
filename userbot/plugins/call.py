"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "**Connettendomi ai Server di Telegram...**",
            "**Chiamata avviata.**",
            "Telegram: Ciao, questo è Telegram HQ. Chi è?",
            "Me: Ciao, sono @V_SHADOW_V , Per favore collegami al mio bro",
            "Utente Autorizzato.",
            "Chiamando lo sviluppatore di Telegram..",
            "Chiamata Privata avviata...",
            "Me: Hey, ciao, per favore banna sto account.",    
            "Sviluppatore: Posso sapere, chi sei?",
            "Me: Sono @V_SHADOW_V, ti ricordi? ",
            "Sviluppatore: O mio Dio, da quanto tempo, com'è...\nMi assicurerò personalmente che questo account venga bannanto entro 24h.",
            "Me: Grazie tante",
            "Sviluppatore: Non ringraziarmi, Telegram è nostro, chiamami quando sei libero.",
            "Me: Perché? C'è qualche problema?",
            "Sviluppatore: Si, c'è un problema in Telegram v69.6.9.\nNon riesco a fixarlo. Mi serve aiuto.",
            "Me: Mandami l'app sul mio account Telegram, lo fixo e te lo mando.",
            "Sviluppatore: Sicuro, va bene \nCi vediamo, ciao :)",
            "**Chiamata Privata Disattivata**."
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
