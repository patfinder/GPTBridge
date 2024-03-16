from selenium.webdriver.common.by import By

def openAI(driver):
    # Enter prompt into input field
    input = driver.find_element(By.CSS_SELECTOR, '#prompt-textarea')
    input.send_keys("Hello GPT")

    # Click submit button
    submitBtn = driver.find_elements(By.CSS_SELECTOR, 'button[data-testid="send-button"]')
    submitBtn.click()

    # print('\n\n\n========================================')
    # print(f'Input {text1}')
