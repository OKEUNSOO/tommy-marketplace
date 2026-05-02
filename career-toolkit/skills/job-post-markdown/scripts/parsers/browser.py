from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from playwright.sync_api import Browser, BrowserContext, Playwright, sync_playwright


DEFAULT_LAUNCH_ARGS = [
    "--log-level=3",
    "--disable-gpu",
    "--disable-logging",
    "--disable-blink-features=AutomationControlled",
    "--no-sandbox",
    "--disable-setuid-sandbox",
]
DEFAULT_VIEWPORT = {"width": 1280, "height": 1000}
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def open_context(
    *,
    headless: bool = True,
    args: Iterable[str] | None = None,
) -> tuple[Playwright, Browser, BrowserContext]:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=headless,
        args=list(args) if args is not None else DEFAULT_LAUNCH_ARGS,
    )
    context = browser.new_context(user_agent=DEFAULT_USER_AGENT, viewport=DEFAULT_VIEWPORT)
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return playwright, browser, context


def close_context(playwright: Playwright, browser: Browser, context: BrowserContext) -> None:
    try:
        context.close()
        browser.close()
        playwright.stop()
    except Exception:
        pass


def safe_text(page: Any, selector: str) -> str:
    locator = page.locator(selector)
    if locator.count() == 0:
        return ""
    return locator.first.inner_text().strip()


def all_texts(page: Any, selector: str) -> list[str]:
    try:
        return [text.strip() for text in page.locator(selector).all_text_contents() if text.strip()]
    except Exception:
        return []
