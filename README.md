# Twitch Chat Sentiment Analyzer

This Python script leverages Selenium and NLTK to analyze the sentiment of recent chat messages on a Twitch stream.

## Functionality

1. **Retrieves Chat Messages:**
   - Uses Selenium to automate the process of loading the specified Twitch channel's chat.
   - Extracts the latest chat messages from the chat log.

2. **Calculates Sentiment Scores:**
   - Employs NLTK's SentimentIntensityAnalyzer to assign a sentiment score (positive, negative, neutral) to each chat message.

3. **Determines Average Sentiment:**
   - Calculates the overall average sentiment of the collected chat messages. 

## Setup

1. **Prerequisites:**
   - Python 3 ([https://www.python.org/](https://www.python.org/))
   - Selenium ( `pip install selenium`)
   - NLTK ( `pip install nltk`)
   - A WebDriver for your browser (e.g., ChromeDriver for Chrome: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/))

2. **Download NLTK Data:**
   - After installing NLTK, run the following in your Python terminal:
     ```bash
     import nltk
     nltk.download('vader_lexicon')
     ```

## Usage

1. **Customize the Code:**
   - Replace `/usr/bin/chromedriver` with the correct path to your WebDriver.
   - Change `"https://twitch.tv/summit1g"` to the desired Twitch channel URL.

2. **Run the Script:**
   ```bash
   python twitch_sentiment_analyzer.py 
