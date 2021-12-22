# Copyright (C) 2021 CyberUserBot
# This file is a part of < https://github.com/FaridDadashzade/CyberUserBot/ >
# PLease read the GNU General Public License v3.0 in
# <https://www.github.com/FaridDadashzade/CyberUserBot/blob/master/LICENSE/>.

from telethon import events
from userbot import *
from . import *
from userbot import ALIVE_LOGO, CYBER_VERSION, tgbot

alive_text = "Cyber Asistanı aktivdir."

@tgbot.on(events.NewMessage(pattern="^/alive"))
async def alive(event):
    await tgbot.send_file(event.chat_id, ALIVE_LOGO, caption=alive_text)