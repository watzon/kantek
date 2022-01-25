"""File containing the settings for kantek."""
import os
from typing import Union

api_id: Union[str, int] = ''
api_hash: str = ''
phone: str = ''
session_name: str = f'sessions/{os.environ.get("KANTEK_SESSION", "kantek-session")}'

log_bot_token: str = ''
log_channel_id: Union[str, int] = ''

# This is regex so make sure to escape the usual characters
cmd_prefix: str = r'\.'
from telethon import events
from telethon.events import NewMessage

from config import cmd_prefix
from utils.pluginmgr import KantekPlugin


class Ping(KantekPlugin):
    """A short help message for the entire plugin"""
    name = 'Ping'

    @events.register(NewMessage(outgoing=True, pattern=f'{cmd_prefix}ping'))
    async def ping(event):
        """A long message about the command"""
        await event.reply('Pong 🏓')
