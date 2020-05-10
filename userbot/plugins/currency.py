"""command: .currency usd inr"""
from telethon import events
import asyncio
from datetime import datetime
import requests
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="currency (.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            number = float(input_sgra[0])
            currency_from = input_sgra[1].upper()
            currency_to = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(currency_from)
            current_response = requests.get(request_url).json()
            if currency_to in current_response["rates"]:
                current_rate = float(current_response["rates"][currency_to])
                rebmun = round(number * current_rate, 2)
                await event.edit("**Guardando le valute,**\n {} **{}** = {} **{}**\n \n●▬▬▬▬▬ஜ۩❀۩ஜ▬▬▬▬▬●\n\n**Valute correnti:**\n 1 **{}** = {} **{}**".format(number, currency_from, rebmun, currency_to, currency_from, current_rate, currency_to))
            else:
                await event.edit("Odioso dirlo, ma questa valuta non è usabile **per ora**.\n__Prova__ `.currencies` __per una lista di valute supportate.__")
        except e:
            await event.edit(str(e))
    else:
        await event.edit("**Syntax:**\n.currency numero da a\n**Esempio:**\n`.currency 10 usd inr`")
    end = datetime.now()
    ms = (end - start).seconds

 
@borg.on(admin_cmd(pattern="currencies (.*)"))
async def list(ups):
    if ups.fwd_from:
        return
    request_url = "https://api.exchangeratesapi.io/latest?base=USD"
    current_response = requests.get(request_url).json()
    dil_wale_puch_de_na_chaaa = current_response["rates"]
    for key, value in dil_wale_puch_de_na_chaaa.items():
        await borg.send_message(ups.chat_id, "**Lista delle valute supportate:**\n {}\n*Tip:** Usa `.gs` currency_code per più dettagli sulle valute.".format(key))
