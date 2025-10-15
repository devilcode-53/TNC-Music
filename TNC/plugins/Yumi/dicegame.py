from pyrogram import Client, enums, filters
#from config import *
import asyncio
from TNC import app as app

from pyrogram.handlers import MessageHandler


@app.on_message(filters.command("ISdice"))
async def dice(bot, message):
    x=await bot.send_dice(message.chat.id)
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
  
@app.on_message(filters.command("ISdart"))
async def dart(bot, message):
    x=await bot.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)

@app.on_message(filters.command("ISbasket"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🏀")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
@app.on_message(filters.command("ISjackpot"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎰")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
@app.on_message(filters.command("ISball"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎳")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
@app.on_message(filters.command("ISfootball"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "⚽")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)
__help__ = """
 Play Game With Emojis:
/dice - Dice 🎲
/dart - Dart 🎯
/basket - Basket Ball 🏀
/ball - Bowling Ball 🎳
/football - Football ⚽
/jackpot - Spin slot machine 🎰
 """

__mod_name__ = "Dɪᴄᴇ"
