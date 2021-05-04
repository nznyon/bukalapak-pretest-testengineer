from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.bukalapak.com/login")
driver.maximize_window()

driver.find_element_by_id("user_session_username").send_keys("rebeccavom@gmail.com")
driver.find_element_by_id("user_session_password").send_keys("B3b3k23121986")
driver.find_element_by_name("commit").click()

time.sleep(5)

driver.find_element(By.XPATH,"//div[@id='vm__white-header-dweb']/section/header/div[3]/div/div/div[2]/div/span[6]/div/div/a/div/div").click()
driver.find_element_by_xpath("//p[contains(.,'Logout')]").click()
driver.quit()
