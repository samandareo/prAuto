from pyrogram import Client

from pyrogram import filters
api_id = 123456 #api_id yoziladi 
api_hash ="15551d5sd5s15ds5d15sd5sd18" # o'z api hash adresizzi yozasiz

APP = Client("tilonlike", api_id, api_hash)
@APP.on_message(filters.text)
def _(p,m):
  if m.text == "!s":
    m.delete()
    m.reply("Assalomu aleykum. Yaxshimisiz.")
  if m.text == "!r":
    m.delete()
    m.reply("Rahmat")
APP.run()
