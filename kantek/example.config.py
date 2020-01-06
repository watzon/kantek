"""File containing the settings for kantek."""
import os
from pathlib import Path
from typing import Union

api_id: Union[str, int] = ''
api_hash: str = ''
phone: str = ''
session_name: str = f'sessions/{os.environ.get("KANTEK_SESSION", "kantek-session")}'

log_bot_token: str = ''
log_channel_id: Union[str, int] = ''

# This is regex so make sure to escape the usual characters
cmd_prefix: str = r'\.'

# Where we should store installed plugins
plugins_dir: str = Path.joinpath(Path.home(), '.kantek/plugins')
