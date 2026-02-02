class LoginPage:
    def __init__(self, page):
        self.page = page

        #locators
        self.username = page.get_by_placeholder('Username')
        self.password = page.get_by_placeholder('Password')
        self.login_btn = page.locator('button[type="submit"]')

    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com", wait_until="domcontentloaded")

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
