# HR-Bot

This Telegram bot retrieves and stores employee Chat IDs for HR use. It runs as a server, collecting IDs when users interact with it. These IDs can be used in systems like TrueTabs to send automated notifications via Telegram API. The bot itself does not send messages, only retrieves IDs. 🚀

---

## 📌 Overview
This is a Telegram bot designed to retrieve employee Chat IDs. It allows the HR system to send notifications about leave approvals, disapprovals, new task assignments, and other important updates using Telegram API.

## ✨ Features
- Retrieves employee Chat IDs via Telegram bot.
- Stores Chat IDs in a text file for later use.
- Can be integrated with external systems like TrueTabs for automated notifications.

## 🛠 How It Works
1. The Python script (`cybernauts.py`) acts as a server, retrieving and storing Chat IDs when users interact with the bot.
2. These Chat IDs are stored in `chat_ids.txt`.
3. The TrueTabs HR system includes a button in relevant sheets (e.g., leave requests, task assignments) that triggers a Telegram API request.
4. When pressed, the button constructs a URL request that sends a formatted notification to the respective employee’s Telegram account.

## 🔗 Telegram API Request Format
The TrueTabs button triggers a URL request structured as follows:
```plaintext
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage?chat_id={Chat_ID}&parse_mode=HTML&text=
<b>New Task Assigned</b>%0A%0A
<b>Task ID:</b> {Task_ID}%0A
<b>Task Name:</b> {Task_Name}%0A
<b>Assigned To:</b> {Assigned_To}%0A
<b>Priority:</b> {Priority_Level}%0A
<b>Start Date:</b> {Start_Date}%0A
<b>Deadline:</b> {Deadline}%0A%0A
{Comments}
```

## 📷 Screenshot
![Bot Screenshot](Bot%20Screenshot.png)

## 📌 Steps to Set Up:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/samsepi0l-kali/HR-Bot.git
   ```
2. **Install Dependencies:**
   ```bash
   pip install -U python-telegram-bot
   ```
3. **Run the Script:**
   ```bash
   python cybernauts.py
   ```
4. **Enter Telegram Bot Token when prompted.**
5. **Get Chat ID by sending `/start` to the bot.**
6. **Use the retrieved Chat ID in the TrueTabs HR system for sending notifications.**
7. **Use TrueTabs Buttons to send real-time notifications via Telegram API.**

## ⚠️ Notes
- Ensure your bot token is secure and not included in public repositories.
- Update the TrueTabs button query with correct field names as per your HR system.
- The bot runs continuously, listening for updates and storing chat IDs automatically.

---

### 🚀 Developed by **CYB3RN4UT5**

