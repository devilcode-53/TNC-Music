from TNC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **ʜᴇʏ ʙᴧʙʏ ᴋᴧʜᴧ ʜᴏ🤗🥱** ",
           " **ᴏʏᴇ sᴏ ɢᴧʏᴇ ᴋʏᴧ ᴏɴʟɪɴᴇ ᴧᴧᴏ😊** ",
           " **ᴠᴄ ᴄʜᴧʟᴏ ʙᴧᴛᴇ ᴋᴧʀᴛᴇ ʜᴧɪɴ ᴋᴜᴄʜ ᴋᴜᴄʜ😃** ",
           " **ᴋʜᴧɴᴧ ᴋʜᴧ ʟɪʏᴇ ᴊɪ..??🥲** ",
           " **ɢʜᴧʀ ᴍᴧɪ sᴧʙ ᴋᴧɪsᴇ ʜᴧɪɴ ᴊɪ🥺** ",
           " **ᴘᴛᴧ ʜᴧɪ ᴍᴇ ᴧᴘᴋᴏ ʙᴏʜᴏᴛ ᴍɪss ᴋᴧʀ ʀʜɪ ᴛʜɪ🤭** ",
           " **ᴏʏᴇ ʜᴧʟ ᴄʜᴧʟ ᴋᴇsᴧ ʜᴧɪ ᴧᴘᴋᴀ..??🤨** ",
           " **ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴧʀʙᴧ ᴅᴏɢᴇ ᴋʏᴧ..??🙂** ",
           " **ᴧᴘᴋᴧ ɴᴧᴍᴇ ᴋʏᴧ ʜᴧᴧ..??🥲** ",
           " **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋** ",
           " **𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐢𝐝𝐧𝐚𝐩 𝐊𝐫 𝐋𝐨😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐫𝐨𝐠𝐞..??🤔** ",
           " **𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
           " **𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.?** ",
           " **𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
           " **𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨 𝐁𝐚𝐛𝐲😇** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
           " **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺** ",
           " **𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲** ",
           " **sᴏɴᴧʟɪ ᴋᴏɴ ʜᴧɪ ᴅʜᴏᴋᴇʙᴧᴢ..??😅** ",
           " **ᴛᴜᴍʜᴧʀɪ ᴇᴋ ᴘɪᴄ ᴍɪʟᴇɢɪ ᴋʏᴧ ʙᴧ..?😅** ",
           " **ᴍᴜᴍᴍʏ ᴧᴧ ɢʏɪ ᴋʏᴧ😆😆😆** ",
           " **ᴏʀ ʙᴛᴧᴏ 😉** ",
           " **ɪ ʟᴏᴠᴇ ʏᴏᴜ 😁** ",
           " **ᴅᴏ ʏᴏᴜ ʟᴏᴠᴇ ᴍᴇ..?👀** ",
           " **ʀᴧᴋʜɪ ᴋʙ ʙᴧɴᴅʜ ʀʜɪ ʜᴏ ᴅɪᴅᴜᴜᴜ....??🙉** ",
           " **ᴇᴋ sᴏɴɢ sᴜɴᴧᴜ ..?😹** ",
           " **ᴏɴʟɪɴᴇ ᴧᴧ ᴊᴧ ʀᴇ sᴏɴɢ sᴜɴᴧ ʀᴧʜɪ ʜᴜ 😻** ",
           " **ɪɴsᴛᴧɢʀᴧᴍ ᴄʜᴧʟᴧᴛᴇ ʜᴏ ᴛᴜᴍ..?? 🙃** ",
           " **ᴡʜᴧᴛsᴧᴘᴘ ɴᴜᴍʙᴇʀ ᴅᴏɢᴇ ᴧᴘɴᴀ ᴛᴜᴍ ..?😕** ",
           " **ᴛᴜᴍʜᴇ ᴋᴏɴ sᴧ ᴍᴜsɪᴄ sᴜɴɴᴧ ᴘᴧsɴᴅ ʜᴧɪ..?🙃** ",
           " **sᴧʀᴧ ᴋᴧᴧᴍ ᴋʜᴧᴛᴍ ʜᴏ ɢʏᴧ ᴧᴧᴘᴋᴧ..?🙃** ",
           " **ᴋʜᴧ sᴇ ʜᴏ ᴧᴧᴘ 😊** ",
           " **sᴜɴᴏ ɴᴧ 🧐** ",
           " **ᴍᴇʀᴧ ᴇᴋ ᴋᴧᴧᴍ ᴋʀ ᴅᴏɢᴇ ᴛᴜᴍ.?** ",
           " **ʙʏ ᴛᴧᴛᴧ ᴍᴧᴛ ʙᴧᴛ ᴋʀɴᴧ ᴧᴧᴊ ᴋᴇ ʙᴧᴅ 😠** ",
           " **ᴍᴜᴍᴍʏ ᴘᴧᴘᴧ ᴋᴧɪsᴇ ʜᴧɪɴ..?** ",
           " **ᴋʏᴧ ʜᴜᴧ ʙᴧʙᴜ..?👱** ",
           " **ʙᴏʜᴏᴛ ʏᴧᴧᴅ ᴧᴧ ʀʜɪ ʜᴧɪ ᴛᴜᴍʜᴧʀɪ 🤧❣️** ",
           " **ʙʜᴜʟ ɢʏᴇ ᴍᴜᴊʜᴇ 😏😏** ",
           " **ᴊʜᴏᴏᴛʜ ɴᴧʜɪ ʙᴏʟɴᴧ ᴄʜᴧʜɪʏᴇ 🤐** ",
           " **ᴋʜᴧ ʟᴏ ʙʜᴧᴡ ᴍᴧᴛ ᴋʀᴏ ʙᴧᴧᴛ 😒** ",
           " **ᴋʏᴧ ʜᴜᴧ ᴊᴧɴᴜ 😮😮** "
           " **ʜᴇʏ ʙᴧʙʏ 👀** ",
           " **ᴧᴘᴋᴇ ᴊᴧɪsᴧ ᴅᴏsᴛ ʜᴏ sᴧᴛʜ ᴍᴇ ғɪʀ ɢᴜᴍ ᴋɪs ʙᴧᴛ ᴋᴧ 🙈** ",
           " **ᴧᴧᴊ ᴍᴧɪ sᴇᴅ ʜᴜ ☹️** ",
           " **ᴍᴜᴊʜsᴇ ʙʜɪ ʙᴧᴛ ᴋʀ ʟᴏ ɴᴧ 🥺🥺** ",
           " **ᴋʏᴧ ᴋᴧʀ ʀᴧʜᴇ ʜᴏ 👀** ",
           " **ᴋʏᴧ ʜᴧʟ ᴄʜᴧʟ ʜᴧɪ 🙂** ",
           " **ᴋᴧʜᴧ sᴇ ʜᴏ ᴧᴧᴘ..?🤔** ",
           " **ᴄʜᴧᴛᴛɪɴɢ ᴋʀ ʟᴏ ɴᴧ..🥺** ",
           " **ᴍᴇ ᴍᴀsᴏᴏᴍ ʜᴜ ɴᴧ🥺🥺** ",
           " **ᴋᴧʟ ᴍᴧᴊᴀ ᴧʏᴧ ᴛʜᴧ ɴᴧ🤭😅** ",
           " **ɢʀᴏᴜᴘ ᴍᴇ ʙᴧᴛ ᴋʏᴜ ɴᴧʜɪ ᴋᴧʀᴛᴇ ʜᴏ😕** ",
           " **ᴧᴧᴘ ʀᴇʟᴧᴛɪᴏɴsʜɪᴘ ᴍᴇ ʜᴏ..?👀** ",
           " **ᴋɪᴛɴᴧ ᴄʜᴜᴘ ʀᴇʜᴛᴇ ʜᴏ ʏʀʀ😼** ",
           " **ᴧᴘᴋᴏ ɢᴧɴᴧ ɢᴧɴᴇ ᴧᴧᴛᴧ ʜᴧɪ...?😸** ",
           " **ɢʜᴜᴍɴᴇ ᴄʜᴧʟᴇ ᴋʏᴧ..??🙈** ",
           " **ᴋʜᴜsʜ ʀᴇʜ ʟɪʏᴧ ᴋʀᴏ✌️🤞** ",
           " **ʜᴜᴍ ᴅᴏsᴛ ʙᴧɴ sᴧᴋᴛᴇ ʜᴧɪ...?🥰** ",
           " **ᴍᴇᴇᴛ ᴍʏ ᴏᴡɴᴇʀ:- [ @Swagger_Soul ]** ",
           " **ᴋᴜᴄʜ ᴍᴧᴍʙᴇʀs ᴧᴅᴅ ᴋʀ ᴅᴏ 🥲** ",
           " **ʙᴧʙʏ ᴛᴜᴍ sɪɴɢʟᴇ ʜᴏ ʏᴧ ᴍɪɴɢʟᴇ 😉** ",
           " **ᴧᴧᴏ ᴘᴧʀᴛʏ ᴋᴧʀᴛᴇ ʜᴧɪɴ😋🥳** ",
           " **ʜᴇᴍʟᴏᴏᴏ ʙᴧʙʏ..🧐** ",
           " **ᴍᴜᴊʜᴇ ʙʜᴜʟ ɢᴧʏᴇ ᴋʏᴧ🥺** ",
           " **ᴄᴏᴍᴇ ʜᴇʀᴇ ʙᴧʙʏ:- [ @AarumiChat ] ᴍᴧsᴛɪ ᴋᴧʀᴇɴɢᴇ 🤭🤭** ",
           " **ᴛʀᴜᴛʜ ᴧɴᴅ ᴅᴧʀᴇ ᴋʜᴇʟᴏɢᴇ..? 😊** ",
           " **ᴧᴧᴊ ᴍᴜᴍᴍʏ ɴᴇ ᴅᴧᴛᴧ ʏʀʀ🥺🥺** ",
           " **ᴊᴏɪɴ ᴋᴧʀ ʟᴏ:- [ @AarumiChat ] 🤗** ",
           " **ᴇᴋ ᴅɪʟ ʜᴧɪ ᴍᴇʀᴇ ᴘᴧᴧs ᴏʀ ᴛᴜᴍʜᴧʀᴇ ᴘᴧᴧs😗😗** ",
           " **ᴛᴜᴍʜᴧʀᴇ ᴅᴏsᴛ ᴋᴧʜᴧ ɢʏᴇ🥺** ",
           " **ᴍʏ ᴄᴜᴛᴇ ᴏᴡɴᴇʀ [ @Swagger_Soul ]🥰** ",
           " **ᴋᴧʜᴧ ᴋʜᴏʏᴇ ʜᴏ ᴊᴧɴᴜ😜** ",
           " **ɢᴏᴏᴅ ɴɪɢʜᴛ ᴊɪ ʙᴧʜᴜᴛ ʀᴧᴛ ʜᴏ ɢʏɪ🥰** ",
           ]

@app.on_message(filters.command(["tagall", "spam", "tagmember", "utag", "stag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP♦")
