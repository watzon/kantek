"""Plugin to get information about kantek."""
import logging
import platform

import telethon
from telethon import events
from telethon.events import NewMessage

from config import cmd_prefix
from utils.client import KantekClient
from utils.mdtex import Bold, KeyValueItem, MDTeXDocument, Section
from utils.pluginmgr import KantekPlugin

__version__ = '0.3.0'

tlog = logging.getLogger('kantek-channel-log')


class Kantek(KantekPlugin):
    """Show information about kantek"""
    name = 'Kantek'

    @events.register(events.NewMessage(outgoing=True, pattern=f'{cmd_prefix}kantek'))
    async def tag(event: NewMessage.Event) -> None:
        """Show information about kantek."""
        client: KantekClient = event.client
        message = MDTeXDocument(
            Section(f"{Bold('kantek')} userbot",
                    KeyValueItem(Bold('source'), ''),
                    KeyValueItem(Bold('version'), client.kantek_version),
                    KeyValueItem(Bold('telethon version'), telethon.__version__),
                    KeyValueItem(Bold('python version'), platform.python_version()),
                    KeyValueItem(Bold('plugins loaded'), len(client.plugin_mgr.active_plugins))))

        await client.respond(event, message, link_preview=False)
