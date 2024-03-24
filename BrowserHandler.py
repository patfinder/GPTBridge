import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


logger = logging.getLogger(__name__)


def launch_browser():
    options = Options()
    options.add_argument('user-data-dir=~/tmp/ChromeProfile')
    # options.add_argument('profile-directory="Profile 3"')

    # To attach to an existing browser window: detach, remote-debugging-port
    # options.add_experimental_option('detach', True)


    # binary_location is the location of chrome executable file.
    # options.binary_location = '/usr/bin/google-chrome-stable'
    # options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

    # options.add_experimental_option('debuggerAddress', '127.0.0.1:9122')
    # options.add_experimental_option('debuggerAddress', '127.0.0.1')

    options.add_argument("--log-path=~/tmp/ChromeProfile/chromedriver.log")
    # options.add_argument("--log-path=d:/tmp/chromedriver.log")
    # options.add_argument("--log-path=d:/tmp/chromedriver.log")


    # options.add_argument("--disable-extensions")
    # options.add_argument('--disable-application-cache')
    # options.add_argument('--disable-gpu')
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-setuid-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument('--profile-directory="Profile 3"')

    # And try to running in headless:
    # options.add_argument("--headless")

    try:
        # browser = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
        driver = webdriver.Chrome(options)
        # open_page(driver)

        # alpremium.process_site(driver)
        # nofrills.process_site(driver)
        openAI(driver)

        # driver.close()
    except Exception as ex:
        logger.error(f'Exception: {ex}')
