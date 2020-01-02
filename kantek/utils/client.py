"""File containing the Custom TelegramClient"""
import logging
from typing import Optional, Union

import logzero
from telethon import TelegramClient, hints
from telethon.events import NewMessage
from telethon.tl.custom import Message

from utils.mdtex import FormattedBase, MDTeXDocument, Section
from utils.pluginmgr import PluginManager

logger: logging.Logger = logzero.logger


class KantekClient(TelegramClient):  # pylint: disable = R0901, W0223
    """Custom telethon client that has the plugin manager as attribute."""
    plugin_mgr: Optional[PluginManager] = None
    kantek_version: str = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parse_mode = 'html'

    async def respond(self, event: NewMessage.Event,
                      msg: Union[str, FormattedBase, Section, MDTeXDocument],
                      reply: bool = True) -> Message:
        """Respond to the message an event caused or to the message that was replied to

        Args:
            event: The event of the message
            msg: The message text
            reply: If it should reply to the message that was replied to

        Returns: None

        """
        msg = str(msg)
        if reply:
            return await event.respond(msg, reply_to=(event.reply_to_msg_id or event.message.id))
        else:
            return await event.respond(msg, reply_to=event.message.id)

    async def get_cached_entity(self, entity: hints.EntitiesLike):
        input_entity = await self.get_input_entity(entity)
        return await self.get_entity(input_entity)
