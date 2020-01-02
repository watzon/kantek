# kantek

kantek is a userbot written in Python using Telethon.

## Requirements

Python 3.6+ is required to run the bot.

## Setup

-   Copy the example config file to `config.py`
-   Put the Authentication data into the config file.
-   Run bot.py

## Plugin Example

```python
from telethon import events
from telethon.events import NewMessage

from config import cmd_prefix
from utils.pluginmgr import KantekPlugin


class Ping(KantekPlugin):
    name = 'Ping'
    help = 'A short help message for the entire plugin'

    @events.register(NewMessage(outgoing=True, pattern=f'{cmd_prefix}ping'))
    async def ping(event):
        """A long message about the command"""
        await event.reply('Pong 🏓')
```
