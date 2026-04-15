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
