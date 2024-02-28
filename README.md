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

* **Prerequisites:**
   - Python 3 ([https://www.python.org/](https://www.python.org/))
   - Selenium ( `pip install selenium`)
   - NLTK ( `pip install nltk`)
   - A WebDriver for your browser (e.g., ChromeDriver for Chrome: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/))

## Usage

1. **Customize the Code:**
   - Replace `/usr/bin/chromedriver` with the correct path to your WebDriver.
   - Change `"https://twitch.tv/summit1g"` to the desired Twitch channel URL.

2. **Run the Script:**
   ```bash
   python main.py

## Ideas for this project
**Using React to Update a Python Lexicon Database**

 **Conceptual Overview**

1. **React Frontend:** Design a user interface for lexicon management.
   * Input fields to add new words or phrases to the lexicon.
   * Editing areas to modify existing entries.
   * A display component to show the current lexicon contents.
   * Buttons to trigger actions (add, edit, delete)

2. **Python Backend (API):** Create a REST API using frameworks like Flask or Django to handle database interactions.
   * **Endpoints:**
      * `GET /lexicon` : Fetches the entire lexicon.
      * `POST /lexicon`: Adds a new entry.
      * `PUT /lexicon/<id>`: Updates an existing entry (where `<id>` is the entry's identifier).
      * `DELETE /lexicon/<id>`: Deletes an entry.

3. **Database:** Choose a database suitable for storing your lexicon.
   * SQLite 

