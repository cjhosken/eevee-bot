# This file contains all the nesscessary variables that are changed or are repeated
import os

DEFAULT_PREFIX       = '&'

MAIN_COLOR           = 0xFFAE19
SECONDARY_COLOR      = 0x4797dd
ERROR_COLOR          = 0xff0000
BOT_TOKEN           = os.environ['WORKBENCH_BOT_TOKEN']

BOT_DESCRIPTION      = 'Workbench is a bot designed for the Blender Community Discord. Its purpose is to assist server users with blender-related topics, and provide some fun activities for them to use.'
INSTAGRAM_LINK       = 'https://www.instagram.com/blender.community/'
SUPPORT_SERVER_LINK  = 'https://discord.gg/blendercommunity'
BOT_GITHUB_LINK      = 'https://github.com/Christopher-Hosken/workbench-bot'
EMPTY_CHAR           = '‎‎'
WAITING_EMOJI        = '⏱️'
DONE_EMOJI           = '✅'
ERROR_EMOJI          = '‼️'
THX_EMOJI            = '🙏' 
UPVOTE_EMOJI         = '👍'
DOWNVOTE_EMOJI       = '👎'
API_BASE_LINK        = 'https://denzven.pythonanywhere.com'

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
	'bot.cogs.NQN',
	'bot.cogs.mod',
	'bot.cogs.status_task',
	'bot.cogs.help',
 
	'bot.cogs.graphs.3dgrem',
	'bot.cogs.graphs.fgrem',
	'bot.cogs.graphs.pgrem',
	'bot.cogs.graphs.derivative_embed',
]

INPUTSTATUS = [
	'Rendering',
	'Making Donuts',
	'Watching Tutorials',
	'Removing Overlapped Vertices',
	'Subdividing',
	'Chilling with the Devs'
]
