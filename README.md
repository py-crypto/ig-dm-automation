# 🚀 Instagram DM Automation (Playwright)

A lightweight **UI automation tool** to send Instagram DMs using **Playwright + Python** with persistent login (no repeated authentication).

---

## ✨ Features

* 🔐 **One-time login** (saved in `ig_state.json`)
* 🤖 **Headless automation** after login
* 💬 Send messages using **name search (no thread ID needed)**
* 🔁 Send messages multiple times
* ⏱️ **Human-like behavior**

  * Random typing speed
  * Random delay between messages
* ⚡ Fast & minimal setup

---

## 🧠 How It Works

```text
First Run:
  Opens browser → You login → Click "Not Now" on popups → Session saved → Continue to messaging

Next Runs:
  Uses saved session → Runs headless → Sends messages automatically
```

---

## 📁 Project Structure

```bash
ig-dm-automation/
│
├── main.py           # Main script
├── ig_state.json     # Auto-generated session (after login)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/py-crypto/ig-dm-automation.git
cd ig-dm-automation
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

```bash
playwright install chromium
```

> ⏳ First-time browser download may take **5–10 minutes**

---

## ▶️ Usage

### 🔹 First Run (Login Required)

```bash
python main.py
```

### Steps:

1. Browser opens
2. Login manually to Instagram
3. When prompted:

   * Click **"Not Now"** on:

     * Save Login Info popup
     * Turn on Notifications popup
4. Wait ~5 seconds
5. Session is saved in `ig_state.json`
6. Program continues to messaging

---

### 🔹 Next Runs (Headless Mode)

```bash
python main.py
```

You’ll be prompted for:

```text
Enter Instagram Name:
Enter Message:
How many times to send (default 1):
```

---

## 📌 Example

```text
Enter Instagram Name: shubham kumar
Enter Message: Hello 👋
How many times to send: 3
```

---

## ⚡ Behavior

* Searches user by **name**
* Selects first matching result
* Opens chat
* Sends message
* Repeats with **random delay (1.2–2.5s)**

---

## ⚠️ Important Notes

* Always click **"Not Now"** after login to ensure session stability
* Name search picks the **first match**
* Works best with **unique names/usernames**
* If session expires → delete `ig_state.json` and login again
* UI automation depends on Instagram layout (may break if UI updates)

---

## 🛠️ Tech Stack

* Python 3.11+
* Playwright (Chromium)
* Asyncio

---

## 🚧 Limitations

* ❌ Not using official Instagram API
* ❌ No guarantee against rate limits
* ❌ UI changes can break selectors
* ❌ First-match selection may pick wrong user

---

## 🔮 Future Improvements

* 🎯 Exact user selection
* 📩 Read & reply to messages
* 🤖 AI auto-reply integration
* 🌐 Web dashboard (Streamlit)
* 📊 Logging & analytics

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Automating Instagram actions may violate their Terms of Service. Use responsibly.

---

## ⭐ Support

If you found this useful:

* ⭐ Star the repo
* 🍴 Fork it
* 🛠️ Improve it

---

## 👨‍💻 Author

Built by a developer exploring **automation + AI systems**

---

**Happy Coding 🚀**
