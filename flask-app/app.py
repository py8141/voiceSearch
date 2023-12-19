from flask import Flask, render_template, jsonify
import subprocess
import speech_recognition as sr
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pyttsx3
from flask_cors import CORS  # Import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/start_speech_recognition', methods=['GET'])
def start_speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        sentText = ''
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        print("Sentiment: {}".format(sentiment))

        if sentiment['pos'] >= sentiment['neg']:
            print("Sentiment: positive")
            sentText = 'Positive'
        else:
            print("Sentiment: negative")
            sentText = 'Negative'


        engine = pyttsx3.init()
        engine.say(sentiment)
        engine.runAndWait()
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.amazon.in')
        try:
            search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
            search_box.send_keys(text) 
            search_box.send_keys(Keys.RETURN)  
        except Exception as e:
            print(f"Error: {e}")
            
        

        result = {
            'text' : text,
            'sentiment' : sentText
        }
        # print(result)
        return jsonify(result)
    
    
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))


if __name__ == '__main__':
    app.run(debug=True)