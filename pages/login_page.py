from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        #locators
        self.user_name = self.page.get_by_role('textbox', name='username')
        self.password = self.page.get_by_role('textbox', name='password')
        self.login_btn = self.page.get_by_role('button', name='Login')
        self.error_msg = self.page.get_by_text('Invalid credentials')

    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com", wait_until="domcontentloaded")
        self.page.wait_for_timeout(5000)

    def login(self, user, pwd):
        # self.page.wait_for_selector('button[type="submit"]')
        self.user_name.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
        self.page.wait_for_timeout(10000)

    def is_login_visible(self):
        try:
            self.login_btn.wait_for(state='visible', timeout=5000)
            return True, None
        except TimeoutError:
            return False, 'Login Button did not appear within timeout'
        # return self.login_btn.is_visible()

    def is_login_error(self):
        return self.error_msg.is_visible()