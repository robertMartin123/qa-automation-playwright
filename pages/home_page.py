from utils.logger import get_logger

class HomePage:
    def __init__(self, page, config):
        self.page = page
        self.config = config
        self.logger = get_logger(self.__class__.__name__)

    def go_to(self):
        self.logger.info(f"Navigating to {self.config.BASE_URL}")
        self.page.goto(self.config.BASE_URL)

    def click_login(self):
        self.logger.info("Clicking login button")
        self.page.click("#login")

    def open(self):
        self.go_to()

    def is_loaded(self):
        assert self.page.locator("h1").is_visible()

    def get_main_heading_text(self):
        return self.page.locator("h1").inner_text()



