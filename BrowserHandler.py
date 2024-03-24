import logging
from selenium import webdriver


logger = logging.getLogger(__name__)


def open_chrome():

    try:
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.add_argument('user-data-dir=/home/vuong/tmp/ChromeProfile')
         # /home/vuong/.config/google-chrome/Default
        # options.add_argument('user-data-dir=/home/vuong/.config/google-chrome')
        options.add_argument('profile-directory=Default')

        # To attach to an existing browser window: detach, remote-debugging-port
        options.add_experimental_option('detach', True)

        # binary_location is the location of chrome executable file.
        options.binary_location = '/opt/google/chrome/chrome'
        # options.binary_location = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

        # options.add_experimental_option('debuggerAddress', '127.0.0.1:9122')
        # options.add_experimental_option('debuggerAddress', '127.0.0.1')

        options.add_argument("--log-path=/home/vuong/tmp/ChromeProfile/chromedriver.log")
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

        # browser = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
        return webdriver.Chrome(options)

        # driver.close()

    except Exception as ex:
        logger.error(f'Exception: {ex}')
        raise ex


def open_firefox():

    try:
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

        options = Options()
        options.profile = FirefoxProfile('/home/vuong/tmp/FirefoxProfile/')

        # options.add_argument('profile=/home/vuong/tmp/FirefoxProfile/')
        # options.add_argument("--log-path=/home/vuong/tmp/ChromeProfile/chromedriver.log")
        # options.add_argument("--log-path=d:/tmp/chromedriver.log")
        # options.add_argument("--log-path=d:/tmp/chromedriver.log")

        # options.add_experimental_option('detach', True)

        # binary_location is the location of firefox executable file.
        options.binary_location = '/snap/firefox/3600/usr/lib/firefox/firefox'

        # options.add_argument("--disable-extensions")
        # options.add_argument('--disable-application-cache')
        # options.add_argument('--disable-gpu')
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-setuid-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument('--profile-directory="Profile 3"')

        # And try to running in headless:
        # options.add_argument("--headless")

        # browser = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
        return webdriver.Firefox(options)

        # driver.close()

    except Exception as ex:
        logger.error(f'Exception: {ex}')
        raise ex
