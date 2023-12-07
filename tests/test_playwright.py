from playwright.sync_api import Page, expect

def test_create_account(db_connection, page, test_web_address):
    db_connection.seed("seeds/chitter.sql")
    page.goto(f"http://{test_web_address}/create_account")
    page.fill("input[name='email']", "test_email")
    page.fill("input[name='username']", "test username")
    page.fill("input[name='display_name']", "test display name")
    page.fill("input[name='password']", "test password")
    page.click("text=Create Account")
