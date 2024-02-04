import os
import pyrogram
from pyrogram import Client

api_id = 27378631
api_hash = "62b24cf4b91a87847b731a8d652cd859"

try:
   os.remove("techvj.session")
except:
     pass
with Client("techvj", api_id=api_id, api_hash=api_hash) as app:
    session = f"**🥀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 » 𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 💞**\n\n`{app.export_session_string()}`\n\n**💥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲: [MKV Server](https://t.me/Mkvmovie01) ✨**"
    app.send_message("me", session, disable_web_page_preview=True)
    try:
        app.join_chat("Mkvmovie01")
        app.join_chat("mkvbt")
        app.join_chat("Mkvmovie01")
        app.join_chat("mkvbt")
    except:
        pass
    print(f"✅ String Session Has 🌟 Been Sent\nTo Your 🔥 Saved Message ✨ ...")
    os.remove("techvj.session")

