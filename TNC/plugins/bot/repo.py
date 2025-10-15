from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from TNC import app
from config import BOT_USERNAME
from TNC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
:⧽  ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛᴇᴧᴍ ˹ᴧᴧʀᴜᴍɪ ꭙ ʙᴏᴛѕ˼ ʀᴇᴘᴏs
 
:⧽  ʀᴇᴘᴏ ᴛᴏ ɴʜɪ ᴍɪʟᴇɢᴧ ʙʜᴧɪ ʏʜᴧ
 
:⧽  ᴧɢᴧʀ ʀᴇᴘᴏ ᴄʜᴧʜɪʏᴇ ᴛᴏ ʙʜᴧɪ ʀᴇᴘᴏ ᴘᴧɪᴅ ᴍɪʟ ᴊᴀʏᴇɢᴧ
 
:⧽  ᴄᴏɴᴛᴧᴄᴛ : ㅤㅤ- к ᴧ ʀ м ᴧ › ᴏᴘ ⇢

:⧽  ʀᴜɴ 24x7 ʟᴧɢ ϝʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⊚ ᴧᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴧᴛ ⊚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ᴜᴘᴅᴧᴛᴇ", url="https://t.me/AarumiBots"),
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AarumiChat"),
          ],
               [
                InlineKeyboardButton("cᴧʀʟᴇss ᴋᴧʀᴍᴧ", url=f"https://t.me/ONE_WAS_KARMA"),
],
[
InlineKeyboardButton("ᴏꜰꜰɪᴄɪᴧʟ ᴍᴜsɪᴄ ʙᴏᴛ", url=f"https://t.me/AarumiSongBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/qv1oc1.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
        has_spoiler=True
    )
