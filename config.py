# This file contains all the nesscessary variables that are changed or are repeated
import os

DEFAULT_PREFIX = '&'

MAIN_COLOR = 0xFFAE19

BOT_TOKEN = os.environ['WORKBENCH_BOT_TOKEN']

BOT_DESCRIPTION = ''

COGS = [
	'bot.cogs.activities',
	'bot.cogs.auto',
	'bot.cogs.core',
	'bot.cogs.emoji',
	'bot.cogs.mod',
	'bot.cogs.status_task',
]

INPUTSTATUS = [
	''
]
