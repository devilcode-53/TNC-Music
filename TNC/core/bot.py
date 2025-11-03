from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
from ..logging import LOGGER
import config


class TNC(Client):
    def init(self):
        LOGGER(name).info("Starting Bot...")
        super().init(
            name="TNCxMUSIC",  # ✅ REQUIRED when in_memory=True
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

        LOGGER(name).info(f"Bot logged in as {self.name} (@{self.username})")

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
        except (errors.ChannelInvalid, errors.PeerIdInvalid, errors.ChatAdminRequired):
            LOGGER(name).warning("⚠️ Log group invalid or inaccessible. Creating a new one...")

            try:
                new_group = await self.create_supergroup(
                    title="TNCxMUSIC Logs",
                    description="Auto-created log group for TNCxMUSIC bot."
                )

                new_chat_id = new_group.id
                LOGGER(name).info(f"✅ New log group created: {new_group.title} ({new_chat_id})")

                await self.send_message(
                    chat_id=new_chat_id,
                    text=(
                        f"✅ <b>Log Group Auto-Created</b>\n\n"
                        f"Please promote me as admin here for full functionality.\n\n"
                        f"<b>Bot:</b> {self.mention}\n"
                        f"<b>Chat ID:</b> <code>{new_chat_id}</code>"
                    ),
                )

                config.LOGGER_ID = new_chat_id

            except Exception as ex:
                LOGGER(name).error(
                    f"❌ Failed to create new log group: {type(ex).name} - {ex}"
                )
        except Exception as ex:
            LOGGER(name).error(
                f"❌ Unexpected error accessing log group/channel: {type(ex).name} - {ex}"
            )

        # ✅ Step 2: Check admin status
        try:
            member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(name).warning(
                    "⚠️ Bot is not admin in the log group/channel. Some features may not work properly."
                )
        except Exception as e:
            LOGGER(name).warning(
                f"Could not verify admin status in log group. Reason: {e}"
            )

        LOGGER(name).info(f"✅ Music Bot Started Successfully as {self.name}")

    async def stop(self):
        await super().stop()
        LOGGER(name).info("Bot stopped. Goodbye!")
