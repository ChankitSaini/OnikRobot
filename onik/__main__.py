import asyncio
from pyrogram import Client, idle
from config import Onik 
from onik.videoplayer import app
from onik.videoplayer import call_py

bot = Client(
    ":memory:",
    Onik.API_ID,
    Onik.API_HASH,
    bot_token=Onik.BOT_TOKEN,
    plugins=dict(root="onik"),
)

bot.start()
print("[STATUS]:✅ »» BOT CLIENT STARTED ««")
app.start()
print("[STATUS]:✅ »» USERBOT CLIENT STARTED ««")
call_py.start()
print("[STATUS]:✅ »» PYTGCALLS CLIENT STARTED ««")
idle()
print("[STATUS]:❌ »» BOT STOPPED ««")
