from utils.logger import get_logger


class LoginPage:
    def __init__(self, page, config):
        self.page = page
        self.config = config
        self.logger = get_logger(self.__class__.__name__)
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.submit_button = page.locator("button[type='submit']")
        self.error_message = page.locator(".error-message")
        self.success_message = page.locator(".login-success")

    def open(self):
        login_url = f"{self.config.BASE_URL}/login"
        self.logger.info(f"Navigating to login page: {login_url}")
        self.page.goto(login_url)

    def login(self, username: str, password: str):
        self.logger.info("Filling login credentials")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def wait_for_error(self):
        self.logger.info("Waiting for login error message")
        self.error_message.wait_for(state="visible", timeout=self.config.TIMEOUT)

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    def wait_for_success(self):
        self.logger.info("Waiting for login success state")
        self.success_message.wait_for(state="visible", timeout=self.config.TIMEOUT)
