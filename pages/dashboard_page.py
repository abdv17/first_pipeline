from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        #locators
        self.dashboard = self.page.get_by_role('heading', name='Dashboard')

    def is_dashboard(self):
        try:
            self.dashboard.wait_for(state='visible', timeout=5000)
            return True, None
        except TimeoutError:
            return False, 'Dashboard did not appear within timeout'