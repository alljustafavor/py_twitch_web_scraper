from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://twitch.tv/lord_kebun")

time.sleep(10)

wait = WebDriverWait(driver, 10) # Timeout after 10 seconds
chat_container = driver.find_element(By.CLASS_NAME, "simplebar-content")
chat_log = []

while True:
    chatter = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "chat-author__display-name")))
    chat_message = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[4]/div[2]/div[2]/div[3]/div[1]/div[1]/div[last()]//div[1]/div[2]/div[1]/div[1]/span[2]/span[1]")))
    chat_log.append(chat_message.text)
    print(chat_log)
    time.sleep(4)

driver.quit()
