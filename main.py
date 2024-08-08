import requests
from pyrogram import Client, filters

# Replace with your bot token and API ID, API hash from my.telegram.org
API_ID = "15122558"
API_HASH = "43042882a789e5c2e8526d2da740b9c1"
BOT_TOKEN = "6142796859:AAHJGvbQBOz1WJr1xGN0C01Y10qp0YjDiX4"

# Initialize the Pyrogram Client
app = Client("gofile_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document)
async def upload_to_gofile(client, message):
    # Download the file from Telegram
    file_path = await message.download()

    # Upload the file to Gofile
    with open(file_path, 'rb') as file:
        response = requests.post('https://api.gofile.io/uploadFile', files={'file': file})

    # Parse the JSON response
    response_data = response.json()

    if response_data["status"] == "ok":
        download_url = response_data["data"]["downloadPage"]
        await message.reply(f"File uploaded successfully! [Download Here]({download_url})")
    else:
        await message.reply("Failed to upload the file to Gofile.")

# Start the bot
app.run()
