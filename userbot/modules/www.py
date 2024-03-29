# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway(yes, Internet). """

from datetime import datetime

import speedtest
from telethon import functions
from userbot import HELPER
from userbot.events import register


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    if not spd.text[0].isalpha() and spd.text[0] not in ("/", "#", "@", "!"):
        await spd.edit("`Running speed test . . .`")
        test = speedtest.Speedtest()

        test.get_best_server()
        test.download()
        test.upload()
        test.results.share()
        result = test.results.dict()

    await spd.edit("__Started at__ "
                   f"{result['timestamp']} \n\n"
                   "__Download__"
                   f"{speed_convert(result['download'])} \n"
                   "__Upload__ "
                   f"{speed_convert(result['upload'])} \n"
                   "Ping pong"
                   f"{result['ping']} \n"
                   "Slow ISP ij "
                   f"{result['client']['isp']}")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {
        0: '',
        1: 'Kb/s',
        2: 'Mb/s',
        3: 'Gb/s',
        4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.nearestdc$")
async def neardc(event):
    """ For .nearestdc command, get the nearest datacenter information. """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(
        f"Country : `{result.country}` \n"
        f"Nearest Datacenter : `{result.nearest_dc}` \n"
        f"This Datacenter : `{result.this_dc}`"
    )


@register(outgoing=True, pattern="^.pingme$")
async def pingme(pong):
    """ FOr .pingme command, ping the userbot from any chat.  """
    if not pong.text[0].isalpha() and pong.text[0] not in ("/", "#", "@", "!"):
        start = datetime.now()
        await pong.edit("`Pong!`")
        end = datetime.now()
        duration = (end - start).microseconds / 1000
        await pong.edit("`Pong!\n%sms`" % (duration))

HELPER.update({
    "speed": ".speed\
    \nUsage: Does a speedtest and shows the results."
})
HELPER.update({
    "nearestdc": ".nearestdc\
    \nUsage: Finds the nearest datacenter from your server."
})
HELPER.update({
    "pingme": ".pingme\
    \nUsage: Shows how long it takes to ping your bot."
})
