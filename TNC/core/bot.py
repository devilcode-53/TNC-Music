import asyncio
import uvloop
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
import config
from ..logging import LOGGER

# Set uvloop as default event loop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class TNC(Client):
    def init(self):
        LOGGER(name).info("Starting Bot...")

        # Proper super init — MUST include 'name'
        super().init(
            name="TNC",  # Name for session (in-memory)
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.me = await self.get_me()

        self.id = self.me.id
        self.name = f"{self.me.first_name} {(self.me.last_name or '')}".strip()
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(name).error(
                "Bot cannot access the log group/channel. Please add it and promote as admin."
            )
        except Exception as ex:
            LOGGER(name).error(
                f"Bot failed to send startup message. Reason: {type(ex).name}: {ex}"
            )

        # Verify admin rights
        try:
            member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(name).error(
                    "Please promote your bot as an admin in your log group/channel."
                )
        except Exception as ex:
            LOGGER(name).warning(f"Unable to verify admin status: {ex}")

        LOGGER(name).info(f"Bot started successfully as {self.name}")

    async def stop(self):
        await super().stop()
        LOGGER(name).info("Bot stopped gracefully.")
