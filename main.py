from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

chat_log = []

def get_chat_messages():
    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://twitch.tv/lord_kebun")

    wait = WebDriverWait(driver, 10)
    chat_container = driver.find_element(By.CLASS_NAME, "simplebar-content")
    
    while len(chat_log) < 8:
        chatter = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "chat-author__display-name")))
        chat_message = wait.until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[2]/div[1]/div[1]/section[1]/div[1]/div[4]/div[2]/div[2]/div[3]/div[1]/div[1]/div[last()]//div[1]/div[2]/div[1]/div[1]/span[2]/span[1]")))
        chat_log.append(chat_message.text)
        print(chat_log)
        time.sleep(2)

    driver.quit()

get_chat_messages()
#def get_message_score(message_arr):
    
