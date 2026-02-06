class LoginPage:
    def __init__(self, page):
        self.page = page

        #locators
        self.user_name = self.page.get_by_role('textbox', name='username')
        self.password = self.page.get_by_role('textbox', name='password')
        self.login_btn = self.page.get_by_role('button', name='Login')
        self.error_msg = self.page.get_by_text('Invalid credentials')

    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com", wait_until="domcontentloaded")

    def login(self, user, pwd):
        # self.page.wait_for_selector('button[type="submit"]')
        self.user_name.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
