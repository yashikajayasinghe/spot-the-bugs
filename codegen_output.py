import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa-practice.netlify.app/bugs-form")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("test")
    page.get_by_role("textbox", name="Last Name* Phone nunber*").click()
    page.get_by_role("textbox", name="Last Name* Phone nunber*").fill("test2")
    page.get_by_role("textbox", name="Enter phone number").click()
    page.get_by_role("textbox", name="Enter phone number").fill("12345")
    page.locator("#countries_dropdown_menu").select_option("Azerbaijan")
    page.get_by_role("textbox", name="Enter email").click()
    page.get_by_role("textbox", name="Enter email").fill("abc@abc.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("abc123")
    page.get_by_role("button", name="Register").click()
    page.get_by_role("textbox", name="Enter phone number").click()
    page.get_by_role("textbox", name="Enter phone number").fill("1234512345")
    page.get_by_role("button", name="Register").click()
    page.get_by_text("First Name: test").click()
    page.get_by_text("Last Name: test").click()
    page.get_by_text("Phone Number:").click()
    page.get_by_text("Country: Azerbaijan").click()
    page.get_by_text("Email: abc@abc.com").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
