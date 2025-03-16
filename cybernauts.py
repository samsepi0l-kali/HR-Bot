import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram.helpers import escape_markdown

logging.basicConfig(level=logging.INFO)

print("   _______     ______ ____  _____  ____   ___ _______    ")
print("  / ____\ \   / /  _ \___ \|  __ \|  _ \ / _ \__   __|   ")
print(" | |     \ \_/ /| |_) |__) | |__) | |_) | | | | | |      ")
print(" | |      \   / |  _ <|__ <|  _  /|  _ <| | | | | |      ")
print(" | |____   | |  | |_) |__) | | \ \| |_) | |_| | | |      ")
print("  \_____|  |_|  |____/____/|_|  \_\____/ \___/  |_|      ")
print("                                                         ") 
print("")
print("--------------------------------------By CYB3RN4UT5------")                                                            


TOKEN = str(input("Enter your Token Here: "))
CHAT_ID_FILE = "chat_ids.txt"


app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    user_name = update.message.from_user.full_name or "Unknown User"
    user_username = update.message.from_user.username or "No Username"


    if not os.path.exists(CHAT_ID_FILE):
        open(CHAT_ID_FILE, "w").close()

    with open(CHAT_ID_FILE, "r") as file:
        saved_chat_ids = file.read()

    user_entry = f"{user_username} | {user_name} | {chat_id}"

    if user_entry not in saved_chat_ids:
        with open(CHAT_ID_FILE, "a") as file:
            file.write(user_entry + "\n")

  
    message_text = f"Hello {user_name} (<code>{user_username}</code>)!\nYour Chat ID is: <code>{chat_id}</code>"

    await update.message.reply_text(
        message_text,
        parse_mode="HTML"
    )

app.add_handler(CommandHandler("start", start))

async def error_handler(update: Update, context: CallbackContext):
    logging.error(f"Update {update} caused error {context.error}")

app.add_error_handler(error_handler)

print("\n🚀 CYB3RB0T Server is now running...")
print("📡 Listening for messages...")
app.run_polling()