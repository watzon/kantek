"""Helper functions to aid with different tasks that dont require a client."""
import logging
import re
from typing import Dict, List, Tuple, Union

import logzero
from telethon.events import NewMessage
from telethon.tl.types import Channel, Chat, User

from utils import parsers
from utils.mdtex import Italic

INVITELINK_PATTERN = re.compile(r'(?:joinchat|join)(?:/|\?invite=)(.*|)')

logger: logging.Logger = logzero.logger


async def get_full_name(entity: Union[Channel, Chat, User]) -> str:
    """Return first_name + last_name if last_name exists else just first_name

    Args:
        entity: The user

    Returns:
        The combined names
    """
    if isinstance(entity, User):
        if entity.deleted:
            return Italic('Deleted Account')
        elif entity.last_name and entity.first_name:
            return '{} {}'.format(entity.first_name, entity.last_name)
        elif entity.first_name:
            return entity.first_name
        elif entity.last_name:
            return entity.last_name
        else:
            return ''

    elif isinstance(entity, (Chat, Channel)):
        return entity.title

    return ''


async def get_args(event: NewMessage.Event) -> Tuple[Dict[str, str], List[str]]:
    """Get arguments from a event

    Args:
        event: The event

    Returns:
        Parsed arguments as returned by parser.parse_arguments()
    """
    _args = event.message.raw_text.split()[1:]
    return parsers.parse_arguments(' '.join(_args))
