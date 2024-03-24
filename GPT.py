from selenium.webdriver.common.by import By

def openAI(driver):
    input = driver.find_element(By.CSS_SELECTOR, '#prompt-textarea')
    input.send_keys("Hello GPT")

    submitBtn = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="send-button"]')
    submitBtn.click()

    # print('\n\n\n========================================')
    # print(f'Input {text1}')
