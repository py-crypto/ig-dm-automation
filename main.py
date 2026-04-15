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
async def send_messages(thread_id, message, count):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        context = await browser.new_context(storage_state=STATE_FILE)
        page = await context.new_page()

        await page.goto(f"https://www.instagram.com/direct/t/{thread_id}/")

        # Wait for chat UI
        input_box = page.locator("textarea, div[role='textbox']")
        await input_box.first.wait_for(timeout=15000)

        for i in range(count):
            print(f"📤 Sending message {i+1}/{count}")

            await input_box.first.click()

            # 🔥 small human pause before typing
            await asyncio.sleep(random.uniform(0.3, 0.8))

            # 🔥 human-like typing
            await page.keyboard.type(message, delay=random.randint(20, 60))

            await page.keyboard.press("Enter")

            # 🔥 fixed internal random delay (FAST)
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
        return

    print("✅ Found existing login session")

    # Take user input (no delay input anymore)
    thread_id = input("Enter Thread ID: ").strip()
    message = input("Enter Message: ").strip()
    count = int(input("How many times to send: "))

    await send_messages(thread_id, message, count)


# ---------------------------
# ▶️ RUN
# ---------------------------
if __name__ == "__main__":
    asyncio.run(main())