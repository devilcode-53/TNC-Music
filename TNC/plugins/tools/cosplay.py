import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ChatAction
from TNC import app
from config import BOT_USERNAME

IVAN = [
    [
        InlineKeyboardButton(text="✙ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✙", url=f"https://t.me/sapna_x_robot?startgroup=true"),
    ],
    [
        InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/Il_4ST_FIGHTER_lI"),
    ],
]

@app.on_message(filters.command("cosplay"))
async def cosplay(_,msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"❅ ᴄᴏsᴘʟᴀʏ ʙʏ ➠ ๛s ᴀ ᴘ ɴ ᴀ ༗", reply_markup=InlineKeyboardMarkup(IVAN),)
