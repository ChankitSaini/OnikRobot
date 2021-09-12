from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Onik

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) First, add me to your group.
2.) Then promote me as admin and give all permissions except anonymous admin.
3.) Add @{Onik.ASSISTANT_USERNAME} to your group.
4.) Turn on the voice chat first before start to stream video.
5.) Type /vstream (reply to video) to start streaming.
6.) Type /vstop to end the video streaming.

📝 **Note: `/vstream` & `/vstop` command can only be executed by group admin only!**

⚡ __Maintained by [Neurotic Association](https://t.me/NeuroticAssociation)__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ), disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"✨ **Hello there, I'm {Onik.BOT_NAME}.**\n\n💭 **I was created to stream videos in group "
        f"video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "📚 All Command List", callback_data="cblist")
            ], [
                InlineKeyboardButton(
                    "❔ HOW TO USE THIS BOT", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "🌐 Terms & Condition", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "💬 Group", url="https://t.me/NeuroticBotSupport"),
                InlineKeyboardButton(
                    "📣 Channel", url="https://t.me/NeuroticBots")
            ], [
                InlineKeyboardButton(
                    "👩🏻‍💻 Developer", url="https://t.me/NeuroticAssociation")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🌐 **Onik's information !**

🤖 __This bot was created to stream video in telegram group video chats using several methods from WebRTC.__

💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API 
Client Library and Framework in Pure Python for Users and Bots.__

👨🏻‍💻 __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__

🤵🏻 » [Chankit Saini](https://github.com/NeuroticCoders) - Owner
👩🏻‍✈️ » [Levina Shavila](https://github.com/levina-lab) - Dev
🤵🏻 » [Sammy-XD](https://github.com/Sammy-XD) - Dev

__This bot licensed under MIT License__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 All Command List:

» /vstream (reply to video or yt/live url) - to stream video
» /vend - stop the video streaming
» /song (song name) - download song from YT
» /vsong (video name) - download video from YT
» /lyrics (song name) - lyrics scrapper

🔰 EXTRA CMD:

» /alive - check bot alive status
» /ping - check bot ping status
» /uptime - check bot uptime status
» /sysinfo - check bot system information

⚡ __Maintained by [Neurotic Association](https://t.me/NeuroticAssociation)__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 Go Back", callback_data="cbstart")
            ]]
        ), disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
