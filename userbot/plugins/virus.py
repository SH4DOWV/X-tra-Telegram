from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 11)
    input_str = event.pattern_match.group(1)
    if input_str == "novirus":
        await event.edit(input_str)
        animation_chars = [
        
            "`Scaricando il file..`",
            "`File Scaricato....`",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 84%\n█████████████████████▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 100%\n█████████████████████████ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nRegistro: 01 di 01 File Scannerizati...\n\nRisultati: Nessun virus trovato...`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "virus":

        await event.edit(input_str)

        animation_chars = [
        
            "`Scaricando il file..`",
            "`File Scaricato....`",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 84%\n█████████████████████▒▒▒▒ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nFile Scannerizato... 100%\n█████████████████████████ `",
            "`Rapido Controllo di Sicurezza Totale\n\n\nAbbonamento: Utente Pro\nValido sino al: 31/12/2099\n\nRegistro: 01 di 01 File Scannerizati...\n\nRisultati:⚠️Virus trovato⚠️\nMaggiori Info: Torzan, Spyware, Adware`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
