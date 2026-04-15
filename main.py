import asyncio
import os
import random
from playwright.async_api import async_playwright

STATE_FILE = "ig_state.json"


# ---------------------------
# 🔐 LOGIN FLOW (FIRST TIME)
# ---------------------------
async def login_and_save():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        context = await browser.new_context()
        page = await context.new_page()

        print("👉 Opening Instagram login...")
        await page.goto("https://www.instagram.com/accounts/login/")

        print("👉 Please login manually...")

        # Wait until redirected after login
        await page.wait_for_url("https://www.instagram.com/*", timeout=0)

        # Ensure session fully initialized
        await page.wait_for_timeout(5000)

        # Save state
        await context.storage_state(path=STATE_FILE)

        print("✅ Login successful. State saved to ig_state.json")

        await browser.close()


# ---------------------------
# 📩 SEND MESSAGE FUNCTION
# ---------------------------
async def send_messages(name, message, count):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=STATE_FILE)
        page = await context.new_page()

        # 🔥 STEP 1: Open inbox
        await page.goto("https://www.instagram.com/direct/inbox/")

        # 🔥 STEP 2: Click "New message"
        chat_btn = page.locator("div[role='button']:has-text('Send message')").first
        await chat_btn.wait_for(timeout=10000)
        await chat_btn.click()

        # 🔥 STEP 3: Wait for popup dialog
        dialog = page.locator("div[role='dialog']")
        await dialog.wait_for(timeout=15000)

        # 🔥 STEP 4: Search by name
        search_box = dialog.locator("input, div[role='textbox']").first
        await search_box.click()
        await search_box.fill(name)

        await page.wait_for_timeout(2000)  # let results load

        # 🔥 STEP 5: Select person
        user_option = dialog.locator(f"text={name}").first
        await user_option.wait_for(timeout=10000)
        await user_option.click()

        # 🔥 STEP 6: Click "Chat"
        chat_btn = page.get_by_role("button", name="Chat")
        await chat_btn.wait_for(timeout=10000)
        await chat_btn.click()

        # 🔥 STEP 7: Wait for message box
        input_box = page.locator("textarea, div[role='textbox']")
        await input_box.first.wait_for(timeout=15000)

        # 🔁 SEND LOOP
        for i in range(count):
            print(f"📤 Sending message {i+1}/{count}")

            await input_box.first.click()

            await asyncio.sleep(random.uniform(0.3, 0.8))

            await page.keyboard.type(message, delay=random.randint(20, 60))
            await page.keyboard.press("Enter")

            delay = random.uniform(1.2, 2.5)
            print(f"⏳ Waiting {delay:.2f}s")
            await asyncio.sleep(delay)

        print("✅ All messages sent")

        await browser.close()


# ---------------------------
# 🧠 MAIN LOGIC
# ---------------------------
async def main():
    # Check if state file exists and is valid
    if not os.path.exists(STATE_FILE) or os.path.getsize(STATE_FILE) == 0:
        await login_and_save()
        print("🔄 Proceeding to messaging...")

    else:
        print("✅ Found existing login session")

    # 👉 Always run this after login (first or later)
    name = input("Enter Instagram Name: ").strip()
    message = input("Enter Message: ").strip()

    count_input = input("How many times to send (default 1): ").strip()
    count = int(count_input) if count_input else 1

    await send_messages(name, message, count)

# ---------------------------
# ▶️ RUN
# ---------------------------
if __name__ == "__main__":
    asyncio.run(main())