# Copyright (C) 2021 CyberUserBot
# This file is a part of < https://github.com/FaridDadashzade/CyberUserBot/ >
# Please read the GNU General Public License v3.0 in
# <https://www.github.com/FaridDadashzade/CyberUserBot/blob/master/LICENSE/>.

from datetime import datetime
from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP, JARVIS, MYID
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("www")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ CYBER """
    await spd.edit(LANG['SPEED'])
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    result = test.results.dict()

    await spd.edit("`"
                   f"{LANG['STARTED_TIME']}"
                   f"{result['timestamp']} \n\n"
                   f"{LANG['DOWNLOAD_SPEED']}"
                   f"{speed_convert(result['download'])} \n"
                   f"{LANG['UPLOAD_SPEED']}"
                   f"{speed_convert(result['upload'])} \n"
                   "Ping: "
                   f"{result['ping']} \n"
                   f"{LANG['ISP']}"
                   f"{result['client']['isp']}"
                   "`")


def speed_convert(size):
    """
    Salam Cyber, baytları oxuya bilirsən?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.dc$")
async def neardc(event):
    """ .dc komutu en yakın datacenter bilgisini verir. """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"Şehir : `{result.country}`\n"
                     f"En yakın datacenter : `{result.nearest_dc}`\n"
                     f"Şu anki datacenter : `{result.this_dc}`")


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    start = datetime.now()
    await pong.edit("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`Pong!\n%sms`" % (duration))


CmdHelp('www').add_command(
    'speed', None, 'Bir speedtest nəticəsi göstərər.'
).add_command(
    'dc', None, 'Serverinizə ən yaxın datacenter\'ı göstərər.'
).add_command(
    'ping', None, 'Botun ping dəyərini göstərər.'
).add()
