"""
This is example made for showing you how to report your data to the ChatWatch service
"""
from logging import basicConfig

from discord.ext.commands import Bot

from chatwatch import ChatWatchClient

basicConfig()

client = Bot("prefix")
chatwatch = ChatWatchClient("cw-token", client)

client.run("bot-token")
