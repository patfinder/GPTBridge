# Start Selenium
import logging
from BrowserHandler import open_chrome, open_firefox
from RequestServer import run


# Config log
logging.basicConfig(filename='GPTBridge.log', encoding='utf-8', level=logging.DEBUG)

# Open browser driver
driver = open_firefox()

# Open ChatGPT
driver.get('https://chat.openai.com/')

# Start RequestServer
run(driver)
# run(None)
