# HR-Bot 🚀  
A **Telegram bot** that retrieves and stores employee Chat IDs for HR use. It runs as a **server**, collecting IDs when users interact with it. These IDs can be used in systems like **TrueTabs** to send automated notifications via **Telegram API**.  

🔹 **The bot does not send messages—it only retrieves Chat IDs.**  

---

## 📌 Overview  
This bot helps HR teams collect employee **Chat IDs**, enabling automated notifications for:  
- ✅ **Leave approvals & rejections**  
- 📌 **New task assignments**  
- 🏢 **Other important HR updates**  

---

## ⚡ Features  
✔️ Retrieves employee **Chat IDs** via Telegram bot.  
✔️ Stores Chat IDs in a text file (`chat_ids.txt`) for later use.  
✔️ Can be **integrated with TrueTabs** for automated notifications.  

---

## 🛠 How It Works  
1️⃣ The **Python script (`cybernauts.py`)** retrieves **Chat IDs** when employees interact with the bot.  
2️⃣ The Chat IDs are **stored in `chat_ids.txt`** for HR use.  
3️⃣ The **TrueTabs HR system** includes a **button in relevant sheets** (e.g., leave requests, task assignments) that triggers a **Telegram API request**.  
4️⃣ When pressed, this button **sends a formatted notification** to the employee’s Telegram account.  

---

## 📩 Telegram API Request Format  
The **TrueTabs** button sends a structured **URL request**:  
```
https://api.telegram.org/bot<TOKEN>/sendMessage?chat_id={Chat_ID}&parse_mode=HTML&text=
<b>New Task Assigned</b>%0A%0A
<b>Task ID:</b> {Task_ID}%0A
<b>Task Name:</b> {Task_Name}%0A
<b>Assigned To:</b> {Assigned_To}%0A
<b>Priority:</b> {Priority_Level}%0A
<b>Start Date:</b> {Start_Date}%0A
<b>Deadline:</b> {Deadline}%0A%0A
{Comments}
```

---

## 📝 Steps to Set Up  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/samsepi0l-kali/HR-Bot.git
```

### 2️⃣ Install Dependencies  
```sh
pip install --upgrade python-telegram-bot
```

### 3️⃣ Run the Script  
```sh
python cybernauts.py
```

### 4️⃣ Enter Telegram Bot Token  
When prompted, enter your **Telegram Bot Token**.

### 5️⃣ Get Chat ID  
Send `/start` to the bot and retrieve your **Chat ID**.

### 6️⃣ Use Chat ID in TrueTabs  
Enter it in **TrueTabs** to enable **automated notifications**.

### 7️⃣ Send Notifications  
Use **TrueTabs buttons** to send **real-time alerts** via **Telegram API**.

---

## 🖼 Screenshot  
Here’s how the bot works in action:  
![Bot Screenshot](images/bot_screenshot.png)  

---

## ⚠️ Notes  
❗ **Keep your bot token secure** (do not expose it in public repositories).  
❗ Update **TrueTabs button fields** to match your **HR system**.  
❗ The bot **runs continuously**, listening for updates & storing **Chat IDs** automatically.  

---

### 👨‍💻 Developed by **CYB3RN4UT5**  

