from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
import sys

import config
from ..logging import LOGGER


class TNC(Client):
    # [FIX 1] The constructor must be __init__
    def __init__(self, name="TNCxMUSIC"):
        # [FIX 2] Use the built-in __name__ variable for the logger
        LOGGER(__name__).info("Starting Bot...")
        # [FIX 3] Call the parent's __init__
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

        # [FIX 4] Use __name__
        LOGGER(__name__).info(f"Bot logged in as {self.name} (@{self.username})")

        log_chat_id = config.LOGGER_ID

        # ✅ Step 1: Try sending startup message
        try:
            await self.send_message(
                chat_id=log_chat_id,
                text=(
                    f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\n"
                    f"ɪᴅ : <code>{self.id}</code>\n"
                    f"ɴᴀᴍᴇ : {self.name}\n"
                    f"ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid, errors.ChatAdminRequired, ValueError):
            # [FIX 5] Use __name__
            LOGGER(__name__).warning("⚠️ Log group invalid or inaccessible. Creating a new one...")

            try:
                # ✅ Step 2: Create new log group
                new_group = await self.create_supergroup(
                    title="TNCxMUSIC Logs",
                    description="Auto-created log group for TNCxMUSIC bot."
                )

                new_chat_id = new_group.id
                # [FIX 6] Use __name__
                LOGGER(__name__).info(f"✅ New log group created: {new_group.title} ({new_chat_id})")

                # ✅ Step 3: Send confirmation inside new log group
                await self.send_message(
                    chat_id=new_chat_id,
                    text=(
                        f"✅ <b>Log Group Auto-Created</b>\n\n"
                        f"Please promote me as admin here for full functionality.\n\n"
                        f"<b>Bot:</b> {self.mention}\n"
                        f"<b>Chat ID:</b> <code>{new_chat_id}</code>"
                    ),
                )

                # ✅ Step 4: Update runtime config (does not modify file)
                config.LOGGER_ID = new_chat_id

            except Exception as ex:
                # [FIX 7] Use __name__
                LOGGER(__name__).error(
                    f"❌ Failed to create new log group: {type(ex).__name__} - {ex}"
                )
                LOGGER(__name__).error("Exiting due to logger failure.")
                sys.exit(1) # Bot can't run without a logger
        except Exception as ex:
            # [FIX 8] Use __name__
            LOGGER(__name__).error(
                f"❌ Unexpected error accessing log group/channel: {type(ex).__name__} - {ex}"
            )
            sys.exit(1) # Also a fatal error

        # ✅ Step 5: Check admin status in the (possibly new) log group
        try:
            member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                # [FIX 9] Use __name__
                LOGGER(__name__).warning(
                    "⚠️ Bot is not admin in the log group/channel. Some features may not work properly."
                )
        except Exception as e:
            # [FIX 10] Use __name__
            LOGGER(__name__).warning(
                f"Could not verify admin status in log group. Reason: {e}"
            )

        # [FIX 11] Use __name__
        LOGGER(__name__).info(f"✅ Music Bot Started Successfully as {self.name}")

    async def stop(self):
        await super().stop()
        # [FIX 12] Use __name__
        LOGGER(__name__).info("Bot stopped. Goodbye!")
