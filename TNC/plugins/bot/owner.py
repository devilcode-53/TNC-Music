from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from TNC import app
from config import BOT_USERNAME
from TNC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴧᴍᴇ - 7905552682
│├  ɴᴧᴍᴇ - к ᴧ ʀ м ᴧ › ᴏᴘ ⇢
│├ ᴜsᴇʀɴᴧᴍᴇ - @Swagger_Soul
│├─────────────────╯
├┼─────────────────⦿
├┤~ ᴏᴡɴᴇʀ » @Swagger_Soul
├┤~ ᴜᴘᴅᴧᴛᴇ » @AarumiBots
├┤~ sᴜᴘᴘᴏʀᴛ » @AarumiChat
├┼─────────────────⦿
│├─────────────────╮
│├ ᴏᴡɴᴇʀ│ @Swagger_Soul
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ʙᴏᴛ ᴏᴡɴᴇʀ", url=f"https://t.me/Swagger_Soul")
        ],
        [
          InlineKeyboardButton("ᴜᴘᴅᴧᴛᴇ", url="https://t.me/AarumiBots"),
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AarumiChat"),
          ],
               [
                InlineKeyboardButton("ʙᴏᴛ ʟɪsᴛ", url=f"https://t.me/AarumiBots/4"),
],
[
InlineKeyboardButton("ᴏꜰꜰɪᴄɪᴧʟ ᴍυꜱɪᴄ ʙᴏᴛ", url=f"https://t.me/AarumiSongBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/g74hbr.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
        has_spoiler=True
    )
