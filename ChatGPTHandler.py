from selenium.webdriver.common.by import By


def query_GPT(driver, query):
    """
    Send a query to GPT and submit.
    Require: ChatGPT window must be openned and logged in.
    """
    
    # Enter prompt into input field
    input = driver.find_element(By.CSS_SELECTOR, '#prompt-textarea')
    input.send_keys(query)

    # Click submit button
    submitBtn = driver.find_elements(By.CSS_SELECTOR, 'button[data-testid="send-button"]')
    submitBtn.click()

    # print('\n\n\n========================================')
    # print(f'Input {text1}')


def get_answer():
    """
    Retrieve last answer on ChatGPT web page.
    """

    return None

