# Start Selenium
from BrowserHandler import open_chrome, open_firefox
from RequestServer import run


driver = open_firefox()

# Start RequestServer
run(driver)
