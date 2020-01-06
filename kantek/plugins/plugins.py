"""Plugin to interface with the plugin manager."""
from telethon import events
from telethon.events import NewMessage

from config import cmd_prefix, plugins_dir
from utils.helpers import get_args
from utils.pluginmgr import KantekPlugin, PluginManager

__version__ = '0.1.0'


class Plugins(KantekPlugin):
    """Manage and get help with plugins plugins"""
    name = 'Plugins'

    @events.register(NewMessage(outgoing=True, pattern=f'{cmd_prefix}plugins'))
    async def manage(event: NewMessage.Event):
        """Manage active plugins"""
        client = event.client
        pluginmgr: PluginManager = client.plugin_mgr
        msg = event.message
        args = msg.raw_text.split()[1:]
        response = False
        if not args:
            response = await _plugins_list(pluginmgr)
        else:
            cmd = args[0]
            if cmd in ['list', 'ls']:
                response = await _plugins_list(pluginmgr)
            elif cmd in ['unregister', 'ur']:
                response = await _plugins_unregister(event, pluginmgr)
            elif cmd in ['register', 're']
                response = await _plugins_register(event, pluginmgr)
        await client.respond(event, response)

    @events.register(NewMessage(outgoing=True, pattern=f'{cmd_prefix}help'))
    async def help(event: NewMessage.Event):
        """Get help on how to use a specific plugin"""
        client = event.client
        pluginmgr: PluginManager = client.plugin_mgr
        keyword_args, args = await get_args(event)
        plugin_name = keyword_args.get('plugin')
        if not plugin_name:
            await Plugins.manage(event)
            return
        callback_name = keyword_args.get('callback')
        response = await _plugins_help(event, plugin_name, callback_name, pluginmgr)
        await client.respond(event, response)


async def _plugins_help(event: NewMessage.Event, plugin_name, callback_name, pluginmgr: PluginManager):
    plugin = next(plugin for plugin in pluginmgr.active_plugins
                  if plugin.name == plugin_name)
    if not plugin:
        return '<b>No plugin found</b>'

    response = f'👥 <b>{plugin.name}</b>\n'
    if plugin.help:
        response += f'🗣 <em>{plugin.help}</em>\n'
    response += '\n'
    if callback_name:
        callback = next(callback for callback in plugin.callbacks
                        if callback.name == callback_name)
        if callback:
            response += f'👤 <b>{callback.name}</b>\n'
            if callback.help:
                response += f'🗣 <em>{callback.help.strip()}</em>\n'
    else:
        for callback in plugin.callbacks:
            response += f'👤 <b>{callback.name}</b>\n'
            if callback.help:
                response += f'🗣 <em>{callback.help.strip()}</em>\n\n'
    return response


async def _plugins_list(pluginmgr: PluginManager) -> str:
    """Get a list of plugins.

    Args:
        pluginmgr: The plugin manager instance

    Returns:

    """
    plugin_list = []
    for plugin in pluginmgr.active_plugins:
        plugin_list.append(f'<b>{plugin.path} [{plugin.version}]:</b>')
        if plugin.help:
            plugin_list.append(f'  <em>{plugin.help}</em>')
        for callback in plugin.callbacks:
            prefix = "[private]" if callback.private else "[public]"
            plugin_list.append(f'  {prefix} {callback.name}')
    if plugin_list:
        return '\n'.join(plugin_list)
    else:
        return 'No active plugins.'


async def _plugins_unregister(event: NewMessage.Event,
                              pluginmgr: PluginManager) -> str:
    """Get a list of plugins.

    Args:
        event: The event with the command
        pluginmgr: The plugin manager instance

    Returns:

    """
    args = event.message.raw_text.split()[2:]
    if not args:
        return 'No arguments specified.'
    if args[0] == 'all':
        pluginmgr.unregister_all()

async def _plugins_register(event: NewMessage.Event,
                            pluginmgr: PluginManager) -> str:
    """Install a new plugin from Telegram.
    
    Args:
        event: The event with the command
        pluginmgr: The plugin manager instance
        
    Returns:
    
    """
    args = get_args(event)
    activate = args[0]['activate']

    return 'Unregistered all non builtins.'
