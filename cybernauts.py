import os
import logging
import curses
import threading
import time
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

CHAT_ID_FILE = "chat_ids.txt"

TOKEN = input("Enter your Token Here: ").strip()

log_lines = []
max_logs = 10
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Application.builder().token(TOKEN).build()

known_users = set()

def log_message(message):
    global log_lines, known_users

    if message in known_users:
        return

    known_users.add(message)
    log_lines.append(message)
    
    if len(log_lines) > max_logs:
        log_lines.pop(0)

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

        log_message(f"✅ New user: {user_name} ({user_username}) - Chat ID: {chat_id}")

    message_text = f"Hello {user_name} (<code>{user_username}</code>)!\nYour Chat ID is: <code>{chat_id}</code>"

    await update.message.reply_text(message_text, parse_mode="HTML")

app.add_handler(CommandHandler("start", start))

async def error_handler(update: Update, context: CallbackContext):
    log_message(f"❌ ERROR: {context.error}")

app.add_error_handler(error_handler)

def check_internet():
    while True:
        try:
            response = requests.get("https://api.telegram.org", timeout=5)
            if response.status_code == 200:
                log_message("✅ Status 200 (OK)")
        except requests.exceptions.RequestException:
            log_message("❌ ERROR: No Internet Connection!")
        time.sleep(5)

def curses_ui(stdscr):
    global max_logs

    curses.curs_set(0)

    banner = [
        "   _______     ______ ____  _____  ____   ___ _______    ",
        "  / ____\ \   / /  _ \___ \|  __ \|  _ \ / _ \__   __|   ",
        " | |     \ \_/ /| |_) |__) | |__) | |_) | | | | | |      ",
        " | |      \   / |  _ <|__ <|  _  /|  _ <| | | | | |      ",
        " | |____   | |  | |_) |__) | | \ \| |_) | |_| | | |      ",
        "  \_____|  |_|  |____/____/|_|  \_\____/ \___/  |_|      ",
        "                                                         ",
        "--------------------------------------By CYB3RN4UT5------",
        "\n🚀 CYB3RB0T Server is now running...",
        "📡 Listening for messages...\n"
    ]

    max_logs = curses.LINES - len(banner) - 2

    while True:
        stdscr.clear()

        for i, line in enumerate(banner):
            stdscr.addstr(i, 0, line, curses.A_BOLD)

        log_y_start = len(banner) + 1
        for i, log in enumerate(log_lines[-max_logs:]):
            stdscr.addstr(log_y_start + i, 0, log)

        stdscr.refresh()

        curses.napms(1000)

def start_curses():
    curses.wrapper(curses_ui)

def start_bot():
    while True:
        try:
            app.run_polling()
        except Exception as e:
            log_message(f"❌ ERROR: Bot Disconnected! Retrying... ({e})")
            time.sleep(5)

curses_thread = threading.Thread(target=start_curses, daemon=True)
curses_thread.start()

internet_thread = threading.Thread(target=check_internet, daemon=True)
internet_thread.start()

start_bot()
