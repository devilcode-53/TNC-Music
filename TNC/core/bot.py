# TNC/core/bot.py

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
import sys

# config.py is no longer imported
from ..logging import LOGGER


# ---!! FILL YOUR VALUES HERE !! ---
MY_API_ID = 24727770  # <-- Put your API_ID here
MY_API_HASH = "b29e54a12450d2bf91e23b5d90d5378e"  # <-- Put your API_HASH here
MY_BOT_TOKEN = "8469011170:AAGfldtzgZV1qS-YxKs35We7X1KZiH3K8NU"  # <-- Put your BOT_TOKEN here
MY_LOGGER_ID = -1003128590255  # <-- Put your LOGGER_ID here
# ------------------------------------


class TNC(Client):
    def __init__(self, name="ZoyuXmusicRobot"):
        LOGGER(__name__).info("Starting Bot...")
        super().__init__(
            name=name,
            api_id=MY_API_ID,  # <-- Using hardcoded value
            api_hash=MY_API_HASH,  # <-- Using hardcoded value
            bot_token=MY_BOT_TOKEN,  # <-- Using hardcoded value
            in_memory=True,
            max_concurrent_transmissions=7,
            parse_mode="html",
        )

    async def start(self):
        await super().start()
        self.me = await self.get_me()
        self.id = self.me.id
        self.name = self.me.first_name + (" " + self.me.last_name if self.me.last_name else "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=MY_LOGGER_ID,  # <-- Using hardcoded value
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid, ValueError):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure the bot is added as admin."
            )
            sys.exit(1)
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel. Reason: {type(ex).__name__}"
            )
            sys.exit(1)

        member = await self.get_chat_member(MY_LOGGER_ID, self.id)  # <-- Using hardcoded value
        if member.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
            sys.exit(1)

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
