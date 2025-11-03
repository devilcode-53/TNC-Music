import sys
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
from ..logging import LOGGER
import config

LOGGER_ID= "-1003128590255"


class TNC(Client):
    def __init__(self, name="TNCxMUSIC"):
        LOGGER(__name__).info("Starting Bot...")
        super().__init__(
            name=name,
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode="html",
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.me = await self.get_me()
        self.id = self.me.id
        self.name = f"{self.me.first_name} {self.me.last_name or ''}".strip()
        self.username = self.me.username or "NoUsername"
        self.mention = self.me.mention

        # Validate and normalize LOGGER_ID
        try:
            log_chat = int(config.LOGGER_ID)
        except Exception as e:
            LOGGER(__name__).error(
                f"Invalid LOGGER_ID in config. Must be a numeric chat ID (e.g., -100xxxxxxxxxx). Error: {e}"
            )
            sys.exit(1)

        # Try sending startup message
        try:
            await self.send_message(
                chat_id=log_chat,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid, ValueError):
            LOGGER(__name__).error(
                "❌ Bot failed to access the log group/channel.\n"
                "➡️ Make sure:\n"
                "  - LOGGER_ID is a valid -100 chat ID\n"
                "  - Bot is added to that group\n"
                "  - Bot is an admin there"
            )
            sys.exit(1)
        except Exception as ex:
            LOGGER(__name__).error(
                f"❌ Unexpected error accessing log group/channel: {type(ex).__name__} - {ex}"
            )
            sys.exit(1)

        # Confirm bot is admin in log group
        try:
            member = await self.get_chat_member(log_chat, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "❌ Please promote your bot as an admin in your log group/channel."
                )
                sys.exit(1)
        except Exception as e:
            LOGGER(__name__).error(
                f"Failed to verify bot's admin status in log group. Error: {e}"
            )
            sys.exit(1)

        LOGGER(__name__).info(f"✅ Music Bot Started Successfully as {self.name}")

    async def stop(self):
        await super().stop()
        LOGGER(__name__).info("Bot stopped. Goodbye!")
