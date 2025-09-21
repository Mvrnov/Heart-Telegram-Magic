from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import emoji
from heart import heart_emoji


app = Client(
    "my_account",
    api_id=28756630,
    api_hash="ae56cd6e5d0ba9748c4b67b953a6e67b"
)

time_sleep = 0.325  # cooldown between frames


@app.on_message(filters.command("down", prefixes="") & filters.me)
def heart_f(_, message):
    end_message = "🔓" + "__" + \
        message.text.split("heart", maxsplit=1)[1] + "__"
    for i in range(len(heart_emoji)):
        message.edit(emoji.emojize(emoji.demojize(heart_emoji[i])))
        sleep(0.325)
    message.edit(end_message)


if __name__ == "__main__":
    print("Telegram Magic running!")
    app.run()
