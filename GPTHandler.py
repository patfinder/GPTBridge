import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


class GPTHandler:
    """
    ChatGPT web UI handler.
    """
    driver = None

    def __init__(self, driver) -> None:
        self.driver = driver

    def send_query(self, query):
        """
        Send a query to GPT and submit.
        Require: ChatGPT window must be openned and logged in.
        """
        
        try:
            # Enter prompt into input field
            self.query_input.send_keys(query)

            # Click submit button
            self.submit_btn.click()

        except Exception as ex:
            logger.error(f'send_query error: {ex}')

    def do_query(self, query):

        self.send_query(query)
        
        # Wait for response
        self.wait_for_response()

        # Retrieve result
        result = self.get_answer()
        return result.get_attribute('innerHTML')

    @property
    def query_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#prompt-textarea')

    @property
    def submit_btn(self):
        # TODO: cache this obj to improve performance?
        return self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="send-button"]')

    def wait_for_response(self):
        """
        Wait for the "Stop button" to go away.
        """

        # Wait 30s
        for i in range(30):
            d = self.submit_btn.find_element('svg>path').get_attribute('d')
            if not 'd'.startswith('M0 2a2 2 0 0'):
                return True
            time.sleep(1)
        
        return False
    
    def get_answer(self):
        """
        Retrieve last answer on ChatGPT web page.
        """

        try:
            els = self.driver.find_elements(By.CSS_SELECTOR, 'div.max-w-full')
            return els[-1]
        
        except Exception as ex:
            logger.error(f'get_answer error: {ex}')
