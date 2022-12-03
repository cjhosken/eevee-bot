# This file contains all the nesscessary variables that are changed or are repeated
import os
from dotenv import load_dotenv
load_dotenv()

DEFAULT_PREFIX = '/'

MAIN_COLOR = 0xFFAE19
SECONDARY_COLOR = 0x4797dd
ERROR_COLOR = 0xff0000
BOT_TOKEN = os.getenv("BOT_TOKEN")

BOT_DESCRIPTION = 'EEVEE is a bot designed for the Blender Community Discord. Its purpose is to assist server users with blender-related topics, and provide some fun activities for them to use.'
INSTAGRAM_LINK = 'https://www.instagram.com/blender.community/'
SUPPORT_SERVER_LINK = 'https://discord.gg/hgzXbvU8CC'
BOT_GITHUB_LINK = 'https://github.com/Christopher-Hosken/eevee-bot'
EMPTY_CHAR = '‎‎‎'
WAITING_EMOJI = '⏱️'
DONE_EMOJI = '✔️'
ERROR_EMOJI = '❗'
THX_EMOJI = '🙏' 
UPVOTE_EMOJI = '👍'
DOWNVOTE_EMOJI = '👎'

#################################################################################################################

# Change log
CHANGE_LOG = '''

'''
BOT_VERSION = 'v1.0.0'

#################################################################################################################

COGS = [
	'bot.cogs.mod',
	'bot.cogs.status_task',
]

INPUTSTATUS = [
	'Blender',
	'with Donuts',
	'Maya',
	'Blendini',
	'Cinema BlenD',
	'Blender 4.1',
	"ZBlend",
]