from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


usernameStr = 'YourUser'
passwordStr = 'Pssword'



browser = webdriver.Chrome()
browser.get(('url'))



username = browser.find_element_by_id('user')
username.send_keys(usernameStr)


username.send_keys(Keys.TAB)
# nextButton = browser.find_element_by_id('next')
# nextButton.click()



password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'pass')))
password.send_keys(passwordStr)



signInButton = browser.find_element_by_id('login_submit')
signInButton.click()