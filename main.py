#senlenium imports

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#nltk  imports
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#default imports
import time

custom_lexixon = {
    "omegalul": 0.8,
    "pog": 0.9,
    "pepehands": -0.5,
    "widepeepohappy": 0.8,
    "lulw": 0.06,
    "pepega": -0.7,
    "kekw": 0.7,
    "monkaw": 0.3,
    "5head": 0.6,
    "poggers": 0.8,
    "monkas": -0.3,
    "ayayay": 0.1,
    "pepelaugh": 0.3,
    "widepeeposad": -0.8,
    "sadge": -0.6,
    "feelsbadman": -0.7,
    "hypers": 0.5,
    "yep": -0.3,
    "feelsokayman": 0.4,
    "kapp": -0.6,
    "ezy": 0.7,
    "handsup": 0.4,
    "3head": -0.5,
    "gachigasm": 0.3,
    "feelsweirdman": -0.4,
    "monkahmm": -0.2,
    "forsenCD": -0.8,
    "pepog": 0.1,
    "monkagun": -0.4,
    "peepoblanket": 0.6,
    "feelsstrongman": 0.8,
    "monkaeyes": -0.1,
    "peepohappy": 0.7,
    "hyperbruh": -0.2,
    "monkatos": -0.3,
    "peepolove": 0.8,
    "wesmart": 0.5,
    "feelsgoodman": 0.7,
    "kkonaW": 0.1,
    "feelsdankman": -0.4,
    "waytoodank": -0.9,
    "reeeee": -0.1,
    "minkah": 0.3,
    "feelsspcialman": -0.5,
    "4head": -0.2,
    "kekwait": 0.1,
    "monkamega": 0.1,
    "peeposad": -0.2,
}

def main():
    nltk.download("vader_lexicon")

    service = Service(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://twitch.tv/esfandTV")

    wait = WebDriverWait(driver, 10)

    chat_log = []
    wait_for_chat_load = 300  # Wait for chat to load (seconds)
    time_between_retrievals = 2  # Seconds between message checks

    try:
        # Wait for chat elements to become visible
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='chat-line__message']")))

        time.sleep(wait_for_chat_load)  # Additional wait after elements are visible

        while len(chat_log) < 200:
            try:
                chat_messages = driver.find_elements(By.XPATH, "//div[@class='chat-line__message']")
                for message in chat_messages:
                    message_text = message.find_element(By.XPATH, ".//span[@class='text-fragment']").text
                    chat_log.append(message_text)
            except NoSuchElementException:
                print("Chat messages not found, waiting...")

            time.sleep(time_between_retrievals)

    except TimeoutException:
        print("Chat did not load in time.")

    finally:
        driver.quit()
        print(chat_log)
        return chat_log

def analyze_sentiment(message_arr):
    sentiment_score_array = []
    sia = SentimentIntensityAnalyzer()

    for message in message_arr:
        scores = sia.polarity_scores(message)
        sentiment_score_array.append(scores)
        
    return sentiment_score_array

def get_average_sentiment(score_array):
    sentiment_score = 0.0
    list_length = 200

    for item in score_array:
        if item['compound'] == 0.0 or item['neu'] == 1.0:
            list_length -= 1
        sentiment_score += item['compound']  
    sentiment_avg = sentiment_score / list_length

    return sentiment_avg 

if __name__ == "__main__":
    chat_log = main()
    sentiment_score = analyze_sentiment(chat_log)
    average_sentiment = get_average_sentiment(sentiment_score)
    print("Average Chat Sentiment: ", average_sentiment)
if average_sentiment > 0.3:
    print("POSITIVE")
elif average_sentiment < -0.3:
    print("NEGATIVE")
else:
    print("NUTUAL")
