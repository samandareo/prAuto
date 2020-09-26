from pyrogram import Client

from pyrogram import filters
api_id =1074334
api_hash ="cc60986b51f899ed64095de24279723f"

APP = Client("tilonlike", api_id, api_hash)
@APP.on_message(filters.text)
def _(p,m):
  if m.text == "!s":
    m.delete()
    m.reply("Assalomu aleykum. Yaxshimisiz.")
APP.run()