import asyncio
import importlib
import sys
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from TNC import LOGGER, app, userbot
from TNC.core.call import DAXX
from TNC.misc import sudo
from TNC.plugins import ALL_MODULES
from TNC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if not any([config.STRING1, config.STRING2, config.STRING3, config.STRING4, config.STRING5]):
        LOGGER(__name__).error(
            "𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧"
        )
        sys.exit(1)

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for module in ALL_MODULES:
        importlib.import_module("TNC.plugins" + module)
    LOGGER("TNC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐃 🥳...")

    await userbot.start()

    # Initialize DAXX instance
    bot = DAXX()
    await bot.start()

    # Stream test file
    try:
        await bot.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("TNC").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧/𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗗𝗔𝗫𝗫 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        sys.exit(1)
    except Exception:
        pass

    await bot.decorators()

    LOGGER("TNC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗭𝗢𝗬𝗨 𝗠𝗨𝗦𝗜𝗖☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )

    await idle()

    await bot.stop()
    await app.stop()
    await userbot.stop()
    LOGGER("TNC").info("𝗦𝗧𝗢𝗣 𝗭𝗢𝗬𝗨 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())