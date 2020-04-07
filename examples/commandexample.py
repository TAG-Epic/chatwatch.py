"""
This is example made for showing you how to report your data to the ChatWatch service
"""
from logging import basicConfig

from discord import Embed
from discord.ext.commands import Bot

from chatwatch import ChatWatchClient, MessageResponse

basicConfig()

client = Bot("gd/")
chatwatch = ChatWatchClient("cw-token", client)


@client.command()
async def stats(ctx):
    """
    Basic command example for ChatWatch.py
    """
    msg: MessageResponse = await chatwatch.wait_for_message(ctx.message.id)

    embed = Embed(title="ChatWatch userinfo", description="", color=0x00FFFF)
    embed.description += "__**Classifications**__:\n"
    for classification in msg.classifications:
        embed.description += "{}\n".format(classification)
    if msg.user.blacklisted:
        embed.description += "__**Blacklisted**__\n"
        embed.description += msg.user.blacklisted_reason
    embed.description += "__**Generic**__\n"
    embed.description += "Message score: {}\n".format(msg.message_score)
    embed.description += "User score: {}\n".format(msg.user_score)
    embed.description += "Common guild ids: {}\n".format(msg.user.guilds)

    # Crediting the library
    embed.set_footer(text="Powered by [ChatWatch.py](https://github.com/TAG-Epic/ChatWatch.py)")

    await ctx.send(embed=embed)


client.run("bot-token")
