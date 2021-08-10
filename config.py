# This file contains all the nesscessary variables that are changed or are repeated
import os

DEFAULT_PREFIX       = '&'

MAIN_COLOR           = 0xFFAE19
SECONDARY_COLOR      = 0x4797dd
ERROR_COLOR          = 0xff0000
BOT_TOKEN           = os.environ['WORKBENCH_BOT_TOKEN']

BOT_DESCRIPTION      = 'Workbench is a bot designed for the Blender Community Discord. Its purpose is to assist server users with blender-related topics, and provide some fun activities for them to use.'
INSTAGRAM_LINK       = 'https://www.wewe.we'
SUPPORT_SERVER_LINK  = 'https://www.wewe.we'
BOT_GITHUB_LINK      = 'https://www.wewe.we'
EMPTY_CHAR           = '‎‎'
#################################################################################################################

# Change log
CHANGE_LOG = '''

'''
BOT_VERSION = 'v0.0.0'

#################################################################################################################

COGS = [
	'bot.cogs.activities',
	'bot.cogs.auto',
	'bot.cogs.core',
	'bot.cogs.emoji',
	'bot.cogs.mod',
	'bot.cogs.status_task',
	'bot.cogs.help',
]

INPUTSTATUS = [
	'Rendering stuff',
	'Creating Donuts',
	'Watching Blender tutorials',
	'Removing overlapped vertices',
	'Smooth shading',
	'ctrl+e , g , s'
]
